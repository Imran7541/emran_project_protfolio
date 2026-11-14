#!/usr/bin/env python3
"""
Test Suite: Ember Cafe Gulshan Showcase & Hospitality Platform Integration (Spec 024)
Validates:
1. data/projects.json contains Ember Cafe entry (ID: 8) with accurate live URL, preview asset, and tags.
2. assets/ember_cafe_preview.png is present, non-empty, and has 1280x720 16:9 dimensions.
3. index.html contains Ember Cafe card in #projects-grid with data-project-type="public" and live link.
4. index.html category filter counters strictly reflect 'All Flagship Works (8)' and 'Public Works (5)'.
5. Total project cards in index.html equal 8 (5 public, 3 private).
6. data/ai-knowledge.json, js/ai-widget.js, and functions/api/chat.js include Ember Cafe knowledge.
7. Live local backend POST /api/chat accurately responds to queries regarding Ember Cafe.
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
    print("☕ RUNNING EMBER CAFE GULSHAN SHOWCASE INTEGRATION TEST SUITE (SPEC 024)")
    print("=" * 75)

    # 1. Check data/projects.json
    projects_raw = read_file("data/projects.json")
    projects = json.loads(projects_raw)
    ember_proj = next((p for p in projects if p.get("slug") == "ember-cafe-gulshan" or "ember" in p.get("title", "").lower()), None)
    assert ember_proj is not None, "Ember Cafe not found in data/projects.json!"
    assert ember_proj.get("liveDemoUrl") == "https://ember-cafe-gulshan.pages.dev", "Ember Cafe live demo URL mismatch"
    assert ember_proj.get("projectType") == "public", "Ember Cafe projectType must be 'public'"
    assert ember_proj.get("previewImage") == "assets/ember_cafe_preview.png", "Ember Cafe previewImage mismatch"
    assert "Next.js 15" in ember_proj.get("tags", []), "Ember Cafe must include 'Next.js 15' tag"
    print(f"✅ 1. data/projects.json verified with Ember Cafe entry (ID: {ember_proj.get('id')})")

    # 2. Check preview image asset
    img_path = os.path.join(ROOT_DIR, "assets", "ember_cafe_preview.png")
    assert os.path.exists(img_path), "assets/ember_cafe_preview.png does not exist!"
    assert os.path.getsize(img_path) > 10000, "assets/ember_cafe_preview.png file size is too small"
    with Image.open(img_path) as img:
        assert img.size == (1280, 720), f"Expected image size (1280, 720), got {img.size}"
    print(f"✅ 2. assets/ember_cafe_preview.png verified (1280x720, {os.path.getsize(img_path):,} bytes)")

    # 3. Check index.html DOM Card
    index_html = read_file("index.html")
    assert "EMBER CAFE: 22-Hour Rooftop Dining & Specialty Steaks" in index_html, "Ember Cafe title missing in index.html"
    assert "assets/ember_cafe_preview.png" in index_html, "assets/ember_cafe_preview.png missing in index.html"
    assert "https://ember-cafe-gulshan.pages.dev" in index_html, "Ember Cafe live URL missing in index.html"
    assert 'data-project-type="public"' in index_html, "data-project-type attribute missing"
    print("✅ 3. index.html projects grid properly mounts Ember Cafe showcase card")

    # 4. Check filter button counters and section summary
    assert "All Flagship Works (8)" in index_html, "Filter button 'All Flagship Works (8)' missing"
    assert "Public Works (5)" in index_html, "Filter button 'Public Works (5)' missing"
    assert "Enterprise Private Systems (3)" in index_html, "Filter button 'Enterprise Private Systems (3)' missing"
    assert "(5 Public • 3 Private)" in index_html, "Section summary '(5 Public • 3 Private)' missing"
    print("✅ 4. Filter buttons and section summary text match exact 8-project breakdown (5 Public • 3 Private)")

    # 5. Check total cards in index.html
    public_cards = re.findall(r'data-project-type="public"', index_html)
    private_cards = re.findall(r'data-project-type="private"', index_html)
    assert len(public_cards) == 5, f"Expected 5 public cards, got {len(public_cards)}"
    assert len(private_cards) == 3, f"Expected 3 private cards, got {len(private_cards)}"
    print(f"✅ 5. DOM card distribution strictly verified (Total: {len(public_cards) + len(private_cards)} cards: 5 Public, 3 Private)")

    # 6. Check AI Knowledge Base & Widget Fallback
    ai_knowledge = json.loads(read_file("data/ai-knowledge.json"))
    ai_widget_js = read_file("js/ai-widget.js")
    cf_chat_js = read_file("functions/api/chat.js")

    ai_ember_proj = next((p for p in ai_knowledge.get("flagshipProjects", []) if "ember" in p.get("name", "").lower()), None)
    assert ai_ember_proj is not None, "Ember Cafe missing in data/ai-knowledge.json flagshipProjects"
    assert "ember-cafe-gulshan.pages.dev" in ai_widget_js, "Ember Cafe missing in js/ai-widget.js"
    assert "ember-cafe-gulshan.pages.dev" in cf_chat_js, "Ember Cafe missing in functions/api/chat.js"
    print("✅ 6. Emran AI Knowledge Base and Client Fallback matrix synchronized across all engines")

    # 7. Check Live Server /api/chat response
    status, res = make_request("/api/chat", method="POST", data={"message": "Tell me about Ember Cafe in Gulshan"})
    assert status == 200, f"Expected 200 from /api/chat, got {status}"
    reply = res.get("reply", "")
    assert "ember" in reply.lower() or "cafe" in reply.lower() or "gulshan" in reply.lower() or "rooftop" in reply.lower(), f"Unexpected AI response: {reply}"
    print(f"✅ 7. Live /api/chat accurately serves Ember Cafe knowledge: {reply[:80]}...")

    print("=" * 75)
    print("🎉 ALL 7 EMBER CAFE INTEGRATION TESTS PASSED (100% GREEN)")
    print("=" * 75)

if __name__ == "__main__":
    run_tests()
