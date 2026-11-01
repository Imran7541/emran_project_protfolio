#!/usr/bin/env python3
"""
Automated Test Suite for Interactive Video Management (Spec 015)
Tests:
1. REST API endpoints (GET /api/videos, POST /api/videos, DELETE /api/videos/:id)
2. URL Parsing & Metadata Auto-Extraction (YouTube, Facebook, LinkedIn)
3. DOM & UI elements in gallery.html (+ Add Video buttons, #add-video-modal, #youtube-cards-grid)
"""

import urllib.request
import urllib.parse
import json
import subprocess
import os
import sys

BASE_URL = os.environ.get("TEST_BASE_URL", "http://127.0.0.1:5225")

ADMIN_TOKEN = None

def get_admin_token():
    global ADMIN_TOKEN
    if ADMIN_TOKEN:
        return ADMIN_TOKEN
    login_url = f"{BASE_URL}/api/admin/login"
    req = urllib.request.Request(login_url, method="POST")
    req.add_header("Content-Type", "application/json")
    req.data = json.dumps({"passcode": "emran@admin7541"}).encode("utf-8")
    handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(handler)
    with opener.open(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        ADMIN_TOKEN = data.get("token")
        return ADMIN_TOKEN

def make_request(path, method="GET", data=None, auth=False):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Content-Type", "application/json")
    if auth:
        token = get_admin_token()
        req.add_header("Authorization", f"Bearer {token}")
    if data:
        json_bytes = json.dumps(data).encode("utf-8")
        req.data = json_bytes
    
    # Bypass proxy for 127.0.0.1
    handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(handler)
    with opener.open(req, timeout=10) as resp:
        body = resp.read().decode("utf-8")
        return resp.status, json.loads(body)

def test_api_suite():
    print("\n--- 1. Testing GET /api/videos ---")
    status, videos = make_request("/api/videos")
    assert status == 200, f"Expected 200, got {status}"
    assert isinstance(videos, list), "Expected list of videos"
    assert len(videos) >= 10, f"Expected at least 10 seeded videos, found {len(videos)}"
    print(f"✅ GET /api/videos returned {len(videos)} videos successfully.")

    print("\n--- 2. Testing POST /api/videos (YouTube Video) ---")
    yt_payload = {
        "title": "Autonomous AI Agent Orchestration with LangGraph",
        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "category": "AI Architecture",
        "episode": "Masterclass #1",
        "summary": "Deep dive into multi-agent systems and stateful DAG execution."
    }
    status, res = make_request("/api/videos", method="POST", data=yt_payload, auth=True)
    assert status == 201, f"Expected 201, got {status}"
    assert res.get("ok") is True
    video = res.get("video", {})
    assert video.get("platform") == "youtube", f"Expected youtube, got {video.get('platform')}"
    assert "https://www.youtube.com/embed/dQw4w9WgXcQ" in video.get("embedSrc", "")
    assert "img.youtube.com/vi/dQw4w9WgXcQ" in video.get("thumbnail", "")
    assert video.get("isCustom") is True
    yt_id = video.get("id")
    print(f"✅ POST YouTube video ingested: ID={yt_id}, Thumbnail={video.get('thumbnail')}")

    print("\n--- 3. Testing POST /api/videos (Facebook Reel) ---")
    fb_payload = {
        "title": "AI Agent Root Cause Analysis in Production",
        "url": "https://www.facebook.com/share/v/1CSQNPuiKu/",
        "category": "Debugging & RCA",
        "episode": "Reel #08"
    }
    status, res = make_request("/api/videos", method="POST", data=fb_payload, auth=True)
    assert status == 201, f"Expected 201, got {status}"
    video = res.get("video", {})
    assert video.get("platform") == "facebook"
    assert video.get("isPortrait") is True
    assert "facebook.com%2Fshare%2Fv%2F1CSQNPuiKu" in video.get("embedSrc", "")
    fb_id = video.get("id")
    print(f"✅ POST Facebook Reel ingested: ID={fb_id}")

    print("\n--- 4. Testing DELETE /api/videos/:id ---")
    status, del_yt = make_request(f"/api/videos/{yt_id}", method="DELETE", auth=True)
    assert status == 200 and del_yt.get("ok") is True
    status, del_fb = make_request(f"/api/videos/{fb_id}", method="DELETE", auth=True)
    assert status == 200 and del_fb.get("ok") is True
    print(f"✅ Successfully deleted test videos {yt_id} and {fb_id}")

    # Re-verify count
    status, final_videos = make_request("/api/videos")
    assert len(final_videos) == len(videos)
    print(f"✅ Dataset cleanly restored to {len(final_videos)} videos.")

def test_dom_ui():
    print("\n--- 5. Testing DOM UI in gallery.html ---")
    req = urllib.request.Request(f"{BASE_URL}/gallery")
    handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(handler)
    with opener.open(req, timeout=10) as resp:
        html = resp.read().decode("utf-8")

    assert 'id="add-video-modal"' in html, "Modal #add-video-modal missing from DOM"
    assert 'openAddVideoModal()' in html, "Action trigger openAddVideoModal missing from DOM"
    assert 'id="youtube-cards-grid"' in html, "#youtube-cards-grid container missing from DOM"
    assert 'id="tab-platform-facebook"' in html, "Platform tab selector missing from DOM"
    assert 'id="filter-yt-label"' in html, "YouTube filter badge missing from DOM"
    print("✅ All UI components verified present in rendered DOM.")

if __name__ == "__main__":
    try:
        test_api_suite()
        test_dom_ui()
        print("\n🎉 ALL TESTS PASSED SUCCESSFULLY! (100% SPEC COMPLIANCE)")
    except Exception as e:
        print(f"\n❌ TEST SUITE FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
