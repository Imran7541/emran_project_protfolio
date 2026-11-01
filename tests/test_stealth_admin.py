#!/usr/bin/env python3
"""
Test Suite: Stealth Admin Portal, Authentication Gates & Curated Project Showcase
Validates:
1. Admin login rejecting invalid passcode and issuing crypto session tokens for valid passcode
2. Admin token verification and session termination (logout)
3. Protection of video ingestion and deletion APIs (401 Unauthorized for unauthenticated requests)
4. Public DOM sanitization in gallery.html (zero add buttons or delete triggers visible to public visitors)
5. Flagship works curation in index.html (3 Public Open Source + 3 Enterprise Private Systems)
"""

import sys
import os
import json
import urllib.request
import urllib.error
import re

PORT = 5225
BASE_URL = f"http://127.0.0.1:{PORT}"
PASSCODE = "emran@admin7541"
WRONG_PASSCODE = "wrong_test_passcode"

def make_request(path, method="GET", data=None, headers=None):
    url = f"{BASE_URL}{path}"
    req_headers = {"Content-Type": "application/json"}
    if headers:
        req_headers.update(headers)
    
    encoded_data = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=encoded_data, headers=req_headers, method=method)
    
    # Configure opener with empty proxy handler to bypass localhost proxy
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
    print("🔍 RUNNING STEALTH ADMIN & PROJECT SHOWCASE TEST SUITE")
    print("=" * 70)

    # 1. Test Health Endpoint
    status, res = make_request("/api/health")
    assert status == 200, f"Expected 200 from /api/health, got {status}"
    assert res.get("status") == "healthy", "Expected healthy status"
    print("✅ 1. Backend Server is HEALTHY on port 5225")

    # 2. Test Admin Login with Invalid Passcode (Should Reject with 401)
    status, res = make_request("/api/admin/login", method="POST", data={"passcode": WRONG_PASSCODE})
    assert status == 401, f"Expected 401 for wrong passcode, got {status}"
    assert res.get("ok") is False, "Expected ok: false for wrong passcode"
    print("✅ 2. Admin Login correctly REJECTS invalid master passcode (HTTP 401)")

    # 3. Test Admin Login with Valid Passcode (Should Return 200 and Token)
    status, res = make_request("/api/admin/login", method="POST", data={"passcode": PASSCODE})
    assert status == 200, f"Expected 200 for valid passcode, got {status}"
    assert res.get("ok") is True, "Expected ok: true"
    token = res.get("token")
    assert token and len(token) == 64, f"Expected 64-char crypto hex token, got {token}"
    print(f"✅ 3. Admin Login GRANTED session token: {token[:12]}... (HTTP 200)")

    # 4. Test Admin Verify Endpoint with Valid Token
    status, res = make_request("/api/admin/verify", headers={"Authorization": f"Bearer {token}"})
    assert status == 200, f"Expected 200 from verify, got {status}"
    assert res.get("authenticated") is True, "Expected authenticated: true"
    print("✅ 4. Admin Session VERIFIED successfully via Bearer token")

    # 5. Test Admin Verify Endpoint without Token (Should Reject with 401)
    status, res = make_request("/api/admin/verify")
    assert status == 401, f"Expected 401 without token, got {status}"
    print("✅ 5. Admin Verify REJECTS unauthenticated requests (HTTP 401)")

    # 6. Test Video Ingestion without Token (Should Reject with 401)
    test_video_payload = {
        "title": "Stealth Security Audit Test Video",
        "url": "https://youtu.be/dQw4w9WgXcQ",
        "category": "Security Engineering"
    }
    status, res = make_request("/api/videos", method="POST", data=test_video_payload)
    assert status == 401, f"Expected 401 for unauthenticated video post, got {status}"
    assert "Unauthorized" in res.get("error", ""), "Expected Unauthorized error message"
    print("✅ 6. Video Ingestion BLOCKED for unauthenticated requests (HTTP 401)")

    # 7. Test Video Ingestion with Valid Token (Should Ingest with 201)
    status, res = make_request("/api/videos", method="POST", data=test_video_payload, headers={"Authorization": f"Bearer {token}"})
    assert status == 201, f"Expected 201 for authenticated video post, got {status}"
    assert res.get("ok") is True, "Expected ok: true"
    new_video = res.get("video")
    test_video_id = new_video.get("id")
    assert test_video_id, "Expected generated video ID"
    print(f"✅ 7. Video Ingestion GRANTED for authenticated admin (ID: {test_video_id})")

    # 8. Test Video Deletion without Token (Should Reject with 401)
    status, res = make_request(f"/api/videos/{test_video_id}", method="DELETE")
    assert status == 401, f"Expected 401 for unauthenticated video deletion, got {status}"
    print("✅ 8. Video Deletion BLOCKED for unauthenticated requests (HTTP 401)")

    # 9. Test Video Deletion with Valid Token (Should Delete with 200)
    status, res = make_request(f"/api/videos/{test_video_id}", method="DELETE", headers={"Authorization": f"Bearer {token}"})
    assert status == 200, f"Expected 200 for authenticated video deletion, got {status}"
    assert res.get("ok") is True, "Expected ok: true"
    assert res.get("deletedId") == test_video_id, "Expected deleted ID match"
    print(f"✅ 9. Video Deletion SUCCESSFUL for authenticated admin (Deleted ID: {test_video_id})")

    # 10. Test Admin Logout
    status, res = make_request("/api/admin/logout", method="POST", headers={"Authorization": f"Bearer {token}"})
    assert status == 200, f"Expected 200 for logout, got {status}"
    status, res = make_request("/api/admin/verify", headers={"Authorization": f"Bearer {token}"})
    assert status == 401, f"Expected 401 after logout, got {status}"
    print("✅ 10. Admin Logout TERMINATES session token cleanly")

    # 11. Test Public DOM Sanitization in gallery.html
    gallery_path = os.path.join(os.path.dirname(__file__), "..", "gallery.html")
    with open(gallery_path, "r", encoding="utf-8") as f:
        gallery_html = f.read()

    # Check 11a: Admin quick add button has 'hidden' class
    assert 'id="admin-quick-add-btn" class="mt-6 flex items-center justify-center hidden"' in gallery_html, \
        "admin-quick-add-btn must be hidden by default"
    # Check 11b: Section add buttons have 'admin-only-control hidden'
    admin_only_matches = re.findall(r'class="[^"]*admin-only-control hidden[^"]*"', gallery_html)
    assert len(admin_only_matches) >= 3, f"Expected at least 3 admin-only section buttons, found {len(admin_only_matches)}"
    # Check 11c: Admin control bar has 'hidden'
    assert 'id="admin-control-bar" class="hidden' in gallery_html, "admin-control-bar must be hidden by default"
    # Check 11d: Admin auth modal exists with master passcode input
    assert 'id="admin-auth-modal"' in gallery_html, "admin-auth-modal must exist in gallery.html"
    assert 'id="admin-passcode-input"' in gallery_html, "admin-passcode-input must exist in gallery.html"
    # Check 11e: Stealth hotkey listener exists (Ctrl + Shift + A)
    assert 'e.ctrlKey && e.shiftKey && (e.key === \'A\' || e.key === \'a\')' in gallery_html, \
        "Ctrl + Shift + A hotkey listener must exist"
    # Check 11f: Delete button gated by isAdminSessionActive()
    assert 'isAdminSessionActive()' in gallery_html, "Delete button must be gated by isAdminSessionActive()"
    print("✅ 11. Public gallery.html DOM is 100% SANITIZED (Zero edit triggers visible to public)")

    # 12. Test Flagship Works Showcase in index.html
    index_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()

    # Check 12a: Filter buttons exist
    assert 'btn-filter-proj-all' in index_html, "Filter button All must exist"
    assert 'btn-filter-proj-public' in index_html, "Filter button Public must exist"
    assert 'btn-filter-proj-private' in index_html, "Filter button Private must exist"
    # Check 12b: Project count (3 public, 3 private)
    public_cards = re.findall(r'data-project-type="public"', index_html)
    private_cards = re.findall(r'data-project-type="private"', index_html)
    assert len(public_cards) == 3, f"Expected 3 public cards, found {len(public_cards)}"
    assert len(private_cards) == 3, f"Expected 3 private cards, found {len(private_cards)}"
    # Check 12c: Private badges & confidentiality
    assert 'Enterprise Private System' in index_html, "Enterprise Private System badge must be present"
    assert 'Client Confidential (NDA)' in index_html, "Client Confidential (NDA) indicator must be present"
    # Check 12d: Telemetry ribbon updated
    assert '3 OSS • 3 Private' in index_html, "Telemetry ribbon must reflect 3 OSS • 3 Private"
    print("✅ 12. Index.html Showcase correctly represents 3 Public OSS + 3 Enterprise Private projects")

    print("=" * 70)
    print("🎉 ALL 12 VERIFICATION CHECKS PASSED WITH ZERO ERRORS!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
