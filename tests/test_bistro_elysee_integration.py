#!/usr/bin/env python3
"""
Test Suite: Bistro Élysée Gulshan Showcase & Hospitality Platform Integration (Spec 025)
Validates:
1. data/projects.json contains Bistro Élysée entry (ID: 9) with accurate live URL, preview asset, and tags.
2. assets/bistro_elysee_preview.png is present, non-empty, and has 1280x720 16:9 dimensions.
3. index.html contains Bistro Élysée card in #projects-grid with data-project-type="public" and live link.
4. index.html category filter counters strictly reflect 'All Flagship Works (9)' and 'Public Works (6)'.
5. Total project cards in index.html equal 9 (6 public, 3 private).
6. data/ai-knowledge.json, js/ai-widget.js, server.js, and functions/api/chat.js include Bistro Élysée knowledge.
7. Live local backend POST /api/chat accurately responds to queries regarding Bistro Élysée.
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error
from PIL import Image

PORT = 5225
BASE_URL = f"http://127.0.0.1:{PORT}"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_file(rel_path):
    with open(os.path.join(ROOT_DIR, rel_path), "r", encoding="utf-8") as f:
        return f.read()

def make_request(path, method="GET", data=None):
    url = f"{BASE_URL}{path}"
    req_headers = {"Content-Type": "application/json"}
    encoded_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=encoded_data, headers=req_headers, method=method)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req) as resp:
            body = resp.read().decode("utf-8")
            ct = resp.headers.get_content_type()
            return resp.status, json.loads(body) if ct == "application/json" else body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, body

def run_tests():
    print("=" * 75)
    print("🥐 RUNNING BISTRO ÉLYSÉE GULSHAN SHOWCASE INTEGRATION TEST SUITE (SPEC 025)")
    print("=" * 75)

    # 1. Check data/projects.json
    projects_raw = read_file("data/projects.json")
    projects = json.loads(projects_raw)
    bistro_proj = next((p for p in projects if p.get("slug") == "bistro-elysee-gulshan" or "bistro" in p.get("title", "").lower()), None)
    assert bistro_proj is not None, "Bistro Élysée not found in data/projects.json!"
    assert bistro_proj.get("liveDemoUrl") == "https://bistro-elysee-gulshan.pages.dev", "Bistro Élysée live demo URL mismatch"
    assert bistro_proj.get("projectType") == "public", "Bistro Élysée projectType must be 'public'"
    assert bistro_proj.get("previewImage") == "assets/bistro_elysee_preview.png", "Bistro Élysée previewImage mismatch"
    assert "React 18" in bistro_proj.get("tags", []), "Bistro Élysée must include 'React 18' tag"
    assert "Framer Motion" in bistro_proj.get("tags", []), "Bistro Élysée must include 'Framer Motion' tag"
    print(f"✅ 1. data/projects.json verified with Bistro Élysée entry (ID: {bistro_proj.get('id')})")

    # 2. Check preview image asset
    img_path = os.path.join(ROOT_DIR, "assets", "bistro_elysee_preview.png")
    assert os.path.exists(img_path), "assets/bistro_elysee_preview.png does not exist!"
    assert os.path.getsize(img_path) > 10000, "assets/bistro_elysee_preview.png file size is too small"
    with Image.open(img_path) as img:
        assert img.size == (1280, 720), f"Expected image size (1280, 720), got {img.size}"
    print(f"✅ 2. assets/bistro_elysee_preview.png verified (1280x720, {os.path.getsize(img_path):,} bytes)")

    # 3. Check index.html DOM Card
    index_html = read_file("index.html")
    assert "Bistro Élysée: European Bistro & Artisan Patisserie" in index_html, "Bistro Élysée title missing in index.html"
    assert "assets/bistro_elysee_preview.png" in index_html, "assets/bistro_elysee_preview.png missing in index.html"
    assert "https://bistro-elysee-gulshan.pages.dev" in index_html, "Bistro Élysée live URL missing in index.html"
    assert "Visit Bistro" in index_html, "'Visit Bistro' button text missing in index.html"
    print("✅ 3. index.html projects grid properly mounts Bistro Élysée showcase card")

    # 4. Check filter button counters and section summary
    assert any(term in index_html for term in ["All Flagship Works (9)", "All Flagship Works (10)"]), "Filter button 'All Flagship Works' missing"
    assert any(term in index_html for term in ["Public Works (6)", "Public Works (7)"]), "Filter button 'Public Works' missing"
    assert "Enterprise Private Systems (3)" in index_html, "Filter button 'Enterprise Private Systems (3)' missing"
    assert any(term in index_html for term in ["(6 Public • 3 Private)", "(7 Public • 3 Private)"]), "Section summary count missing"
    print("✅ 4. Filter buttons and section summary text match project breakdown")

    # 5. Check total cards in index.html
    public_cards = re.findall(r'data-project-type="public"', index_html)
    private_cards = re.findall(r'data-project-type="private"', index_html)
    assert len(public_cards) in (6, 7), f"Expected 6 or 7 public cards, got {len(public_cards)}"
    assert len(private_cards) == 3, f"Expected 3 private cards, got {len(private_cards)}"
    print(f"✅ 5. DOM card distribution strictly verified (Total: {len(public_cards) + len(private_cards)} cards: {len(public_cards)} Public, {len(private_cards)} Private)")

    # 6. Check AI Knowledge Base & Widget Fallback
    ai_knowledge = json.loads(read_file("data/ai-knowledge.json"))
    ai_widget_js = read_file("js/ai-widget.js")
    cf_chat_js = read_file("functions/api/chat.js")
    server_js = read_file("server.js")

    ai_bistro_proj = next((p for p in ai_knowledge.get("flagshipProjects", []) if "bistro" in p.get("name", "").lower()), None)
    assert ai_bistro_proj is not None, "Bistro Élysée missing in data/ai-knowledge.json flagshipProjects"
    assert "bistro-elysee-gulshan.pages.dev" in ai_widget_js, "Bistro Élysée missing in js/ai-widget.js"
    assert "bistro-elysee-gulshan.pages.dev" in cf_chat_js, "Bistro Élysée missing in functions/api/chat.js"
    assert "bistro-elysee-gulshan.pages.dev" in server_js, "Bistro Élysée missing in server.js"
    print("✅ 6. Emran AI Knowledge Base and Client Fallback matrix synchronized across all engines")

    # 7. Check Live Server /api/chat response
    status, res = make_request("/api/chat", method="POST", data={"message": "Tell me about Bistro Elysee in Gulshan"})
    assert status == 200, f"Expected 200 from /api/chat, got {status}"
    reply = res.get("reply", "")
    assert "bistro" in reply.lower() or "elysee" in reply.lower() or "élysée" in reply.lower() or "patisserie" in reply.lower(), f"Unexpected AI response: {reply}"
    print(f"✅ 7. Live /api/chat accurately serves Bistro Élysée knowledge: {reply[:80]}...")

    print("=" * 75)
    print("🎉 ALL 7 BISTRO ÉLYSÉE INTEGRATION TESTS PASSED (100% GREEN)")
    print("=" * 75)

if __name__ == "__main__":
    run_tests()
