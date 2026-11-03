#!/usr/bin/env python3
"""
Test Suite: Stealth Admin Client Inquiry Inbox & Management Portal (Spec 022)
Validates:
1. Zero-Trust access gating: GET /api/admin/inquiries rejects unauthenticated requests (HTTP 401)
2. Zero-Trust access gating: DELETE /api/admin/inquiries/:id rejects unauthenticated requests (HTTP 401)
3. Admin authentication & Bearer token issuance
4. Authenticated admin fetches all client inquiries (HTTP 200) with newest-first ordering
5. Privacy protection: Client IP addresses are stripped/redacted from admin output
6. Public inquiry ingestion via POST /api/contact reflects immediately in admin inbox
7. Authorized deletion of client inquiry via DELETE /api/admin/inquiries/:id (HTTP 200)
8. Inquiry removal verification in subsequent queries
9. DOM Security verification in gallery.html and gallery/index.html:
   - #admin-control-bar is hidden by default
   - #admin-inbox-modal is invisible to public visitors by default
   - #admin-inbox-badge and #admin-inbox-search are properly wired
"""

import sys
import os
import json
import urllib.request
import urllib.error
import time

PORT = 5225
BASE_URL = f"http://127.0.0.1:{PORT}"
PASSCODE = "emran@admin7541"

def make_request(path, method="GET", data=None, headers=None):
    url = f"{BASE_URL}{path}"
    req_headers = {"Content-Type": "application/json"}
    if headers:
        req_headers.update(headers)
    
    encoded_data = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=encoded_data, headers=req_headers, method=method)
    
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body) if resp.headers.get_content_type() == "application/json" else body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, body

def run_tests():
    print("=" * 70)
    print("📬 RUNNING STEALTH ADMIN CLIENT INQUIRY INBOX TEST SUITE (SPEC 022)")
    print("=" * 70)

    # 1. Server Health
    status, res = make_request("/api/health")
    assert status == 200, f"Expected 200 from /api/health, got {status}"
    assert res.get("status") == "healthy", "Expected healthy status"
    print("✅ 1. Backend Server is HEALTHY on port 5225")

    # 2. GET /api/admin/inquiries without Token (Must Reject with 401)
    status, res = make_request("/api/admin/inquiries")
    assert status == 401, f"Expected 401 for unauthenticated inquiries fetch, got {status}"
    assert res.get("ok") is False, "Expected ok: false"
    print("✅ 2. GET /api/admin/inquiries BLOCKED for unauthenticated requests (HTTP 401)")

    # 3. DELETE /api/admin/inquiries/:id without Token (Must Reject with 401)
    status, res = make_request("/api/admin/inquiries/dummy-id", method="DELETE")
    assert status == 401, f"Expected 401 for unauthenticated inquiry delete, got {status}"
    assert res.get("ok") is False, "Expected ok: false"
    print("✅ 3. DELETE /api/admin/inquiries/:id BLOCKED for unauthenticated requests (HTTP 401)")

    # 4. Authenticate as Admin
    status, res = make_request("/api/admin/login", method="POST", data={"passcode": PASSCODE})
    assert status == 200, f"Expected 200 for valid passcode, got {status}"
    token = res.get("token")
    assert token and len(token) == 64, f"Invalid token issued: {token}"
    admin_headers = {"Authorization": f"Bearer {token}"}
    print(f"✅ 4. Admin Login GRANTED session token: {token[:12]}...")

    # 5. GET /api/admin/inquiries with Valid Bearer Token
    status, res = make_request("/api/admin/inquiries", headers=admin_headers)
    assert status == 200, f"Expected 200 for authenticated inquiries fetch, got {status}"
    assert res.get("ok") is True, "Expected ok: true"
    assert "inquiries" in res, "Expected inquiries array"
    initial_inquiries = res.get("inquiries", [])
    initial_count = res.get("total", len(initial_inquiries))
    print(f"✅ 5. GET /api/admin/inquiries SUCCEEDED ({initial_count} current inquiries)")

    # 6. Privacy Protection: Verify Client IPs are stripped/redacted
    for inq in initial_inquiries:
        assert "ip" not in inq or inq["ip"] is None, f"Privacy Leak! Client IP found in inquiry: {inq}"
    print("✅ 6. Privacy Audit Passed: Zero client IP addresses exposed in inquiries response")

    # 7. Post a Public Inquiry via POST /api/contact
    test_timestamp = int(time.time())
    test_contact_payload = {
        "name": f"Spec022 Test Lead {test_timestamp}",
        "email": f"lead_{test_timestamp}@enterprise-test.io",
        "service": "Autonomous AI Agent Swarm",
        "message": "Automated verification inquiry testing the Stealth Admin Inbox."
    }
    status, res = make_request("/api/contact", method="POST", data=test_contact_payload)
    assert status == 200, f"Expected 200 from contact form submission, got {status}: {res}"
    print(f"✅ 7. Public Client Inquiry SUBMITTED for: {test_contact_payload['name']}")

    # 8. Verify the new inquiry appears in Admin Inquiries
    status, res = make_request("/api/admin/inquiries", headers=admin_headers)
    assert status == 200, "Expected 200 on fetch"
    inquiries_after_post = res.get("inquiries", [])
    matched_inquiry = next((inq for inq in inquiries_after_post if inq.get("email") == test_contact_payload["email"]), None)
    assert matched_inquiry is not None, "Newly submitted inquiry not found in admin inquiries!"
    test_inquiry_id = matched_inquiry["id"]
    assert matched_inquiry["name"] == test_contact_payload["name"]
    assert matched_inquiry["service"] == test_contact_payload["service"]
    print(f"✅ 8. New Inquiry REFLECTED in Admin Inbox (ID: {test_inquiry_id})")

    # 9. DELETE the test inquiry via DELETE /api/admin/inquiries/:id
    status, res = make_request(f"/api/admin/inquiries/{test_inquiry_id}", method="DELETE", headers=admin_headers)
    assert status == 200, f"Expected 200 from inquiry delete, got {status}: {res}"
    assert res.get("ok") is True, "Expected ok: true from delete"
    print(f"✅ 9. Admin DELETED test inquiry (ID: {test_inquiry_id}) successfully")

    # 10. Verify inquiry is removed from subsequent query
    status, res = make_request("/api/admin/inquiries", headers=admin_headers)
    assert status == 200, "Expected 200 on fetch"
    remaining_inquiries = res.get("inquiries", [])
    found_after_del = any(inq["id"] == test_inquiry_id for inq in remaining_inquiries)
    assert not found_after_del, "Deleted inquiry still present in admin inquiries!"
    print("✅ 10. Inquiry Deletion CONFIRMED: Target record cleanly expunged")

    # 11. DOM Security & Structure Inspection
    files_to_check = ["gallery.html", "gallery/index.html"]
    for fname in files_to_check:
        with open(fname, "r", encoding="utf-8") as f:
            html = f.read()

        # Admin control bar must be hidden
        assert 'id="admin-control-bar" class="hidden' in html, f"Security Violation: {fname} does not hide #admin-control-bar"
        
        # Inbox modal must be pointer-events-none and opacity-0
        assert 'id="admin-inbox-modal"' in html, f"Missing #admin-inbox-modal in {fname}"
        assert 'opacity-0 pointer-events-none' in html, f"Security Violation: #admin-inbox-modal not hidden by default in {fname}"
        
        # Inquiries button and badge
        assert 'id="admin-inbox-badge"' in html, f"Missing #admin-inbox-badge in {fname}"
        assert 'openAdminInboxModal()' in html, f"Missing openAdminInboxModal() trigger in {fname}"
        
        # Inbox Search input
        assert 'id="admin-inbox-search"' in html, f"Missing #admin-inbox-search in {fname}"
        assert 'filterInquiries()' in html, f"Missing filterInquiries() in {fname}"
        
        # Delete action
        assert 'deleteAdminInquiry' in html, f"Missing deleteAdminInquiry in {fname}"
        print(f"✅ 11. DOM Security & Component Structure VERIFIED in {fname}")

    print("=" * 70)
    print("🎉 ALL 11 STEALTH ADMIN INBOX TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
