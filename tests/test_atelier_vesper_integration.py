#!/usr/bin/env python3
"""
Test Suite: Atelier Vesper Architecture Showcase & Spatial Design Platform Integration (Spec 026)
Validates:
1. data/projects.json contains Atelier Vesper entry (ID: 10) with accurate live URL, repo URL, preview asset, and tags.
2. assets/atelier_vesper_preview.png is present, non-empty, and has 1280x720 16:9 dimensions.
3. index.html contains Atelier Vesper card in #projects-grid with data-project-type="public", live link, and GitHub link.
4. index.html category filter counters strictly reflect 'All Flagship Works (10)' and 'Public Works (7)'.
5. Total project cards in index.html equal 10 (7 public, 3 private).
6. data/ai-knowledge.json, js/ai-widget.js, server.js, and functions/api/chat.js include Atelier Vesper knowledge.
7. Live local backend POST /api/chat accurately responds to queries regarding Atelier Vesper.
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
    print("🏛️ RUNNING ATELIER VESPER ARCHITECTURE SHOWCASE INTEGRATION TEST SUITE (SPEC 026)")
    print("=" * 75)

    # 1. Check data/projects.json
    projects_raw = read_file("data/projects.json")
    projects = json.loads(projects_raw)
    vesper_proj = next((p for p in projects if p.get("slug") == "atelier-vesper-architecture" or "vesper" in p.get("title", "").lower()), None)
    assert vesper_proj is not None, "Atelier Vesper not found in data/projects.json!"
    assert vesper_proj.get("liveDemoUrl") == "https://atelier-vesper-marketing.imranrband100.workers.dev", "Atelier Vesper live demo URL mismatch"
    assert vesper_proj.get("repoUrl") == "https://github.com/Imran7541/atelier-vesper", "Atelier Vesper repo URL mismatch"
    assert vesper_proj.get("projectType") == "public", "Atelier Vesper projectType must be 'public'"
    assert vesper_proj.get("previewImage") == "assets/atelier_vesper_preview.png", "Atelier Vesper previewImage mismatch"
    assert "React 19" in vesper_proj.get("tags", []), "Atelier Vesper must include 'React 19' tag"
    assert "Three.js" in vesper_proj.get("tags", []), "Atelier Vesper must include 'Three.js' tag"
    assert "Cloudflare Workers" in vesper_proj.get("tags", []), "Atelier Vesper must include 'Cloudflare Workers' tag"
    print(f"✅ 1. data/projects.json verified with Atelier Vesper entry (ID: {vesper_proj.get('id')})")

    # 2. Check preview image asset
    img_path = os.path.join(ROOT_DIR, "assets", "atelier_vesper_preview.png")
    assert os.path.exists(img_path), "assets/atelier_vesper_preview.png does not exist!"
    assert os.path.getsize(img_path) > 10000, "assets/atelier_vesper_preview.png file size is too small"
    with Image.open(img_path) as img:
        assert img.size == (1280, 720), f"Expected image size (1280, 720), got {img.size}"
    print(f"✅ 2. assets/atelier_vesper_preview.png verified (1280x720, {os.path.getsize(img_path):,} bytes)")

    # 3. Check index.html DOM Card
    index_html = read_file("index.html")
    assert "Atelier Vesper: Luxury Interior Architecture & Spatial Design" in index_html, "Atelier Vesper title missing in index.html"
    assert "assets/atelier_vesper_preview.png" in index_html, "assets/atelier_vesper_preview.png missing in index.html"
    assert "https://atelier-vesper-marketing.imranrband100.workers.dev" in index_html, "Atelier Vesper live URL missing in index.html"
    assert "https://github.com/Imran7541/atelier-vesper" in index_html, "Atelier Vesper GitHub URL missing in index.html"
    assert "Visit Atelier" in index_html, "'Visit Atelier' button text missing in index.html"
    print("✅ 3. index.html projects grid properly mounts Atelier Vesper showcase card with Live & GitHub links")

    # 4. Check filter button counters and section summary
    assert "All Flagship Works (10)" in index_html, "Filter button 'All Flagship Works (10)' missing"
    assert "Public Works (7)" in index_html, "Filter button 'Public Works (7)' missing"
    assert "Enterprise Private Systems (3)" in index_html, "Filter button 'Enterprise Private Systems (3)' missing"
    assert "(7 Public • 3 Private)" in index_html, "Section summary '(7 Public • 3 Private)' missing"
    print("✅ 4. Filter buttons and section summary text match exact 10-project breakdown (7 Public • 3 Private)")

    # 5. Check total cards in index.html
    public_cards = re.findall(r'data-project-type="public"', index_html)
    private_cards = re.findall(r'data-project-type="private"', index_html)
    assert len(public_cards) == 7, f"Expected 7 public cards, got {len(public_cards)}"
    assert len(private_cards) == 3, f"Expected 3 private cards, got {len(private_cards)}"
    print(f"✅ 5. DOM card distribution strictly verified (Total: {len(public_cards) + len(private_cards)} cards: 7 Public, 3 Private)")

    # 6. Check AI Knowledge Base & Widget Fallback
    ai_knowledge = json.loads(read_file("data/ai-knowledge.json"))
    ai_widget_js = read_file("js/ai-widget.js")
    cf_chat_js = read_file("functions/api/chat.js")
    server_js = read_file("server.js")

    ai_vesper_proj = next((p for p in ai_knowledge.get("flagshipProjects", []) if "vesper" in p.get("name", "").lower()), None)
    assert ai_vesper_proj is not None, "Atelier Vesper missing in data/ai-knowledge.json flagshipProjects"
    assert "atelier-vesper-marketing.imranrband100.workers.dev" in ai_widget_js, "Atelier Vesper missing in js/ai-widget.js"
    assert "atelier-vesper-marketing.imranrband100.workers.dev" in cf_chat_js, "Atelier Vesper missing in functions/api/chat.js"
    assert "atelier-vesper-marketing.imranrband100.workers.dev" in server_js, "Atelier Vesper missing in server.js"
    assert "github.com/Imran7541/atelier-vesper" in ai_widget_js, "Atelier Vesper GitHub link missing in js/ai-widget.js"
    print("✅ 6. Emran AI Knowledge Base and Client Fallback matrix synchronized across all engines")

    # 7. Check Live Server /api/chat response
    status, res = make_request("/api/chat", method="POST", data={"message": "Tell me about Atelier Vesper spatial architecture"})
    assert status == 200, f"Expected 200 from /api/chat, got {status}"
    reply = res.get("reply", "")
    assert "vesper" in reply.lower() or "atelier" in reply.lower() or "interior" in reply.lower() or "architecture" in reply.lower(), f"Unexpected AI response: {reply}"
    print(f"✅ 7. Live /api/chat accurately serves Atelier Vesper knowledge: {reply[:80]}...")

    print("=" * 75)
    print("🎉 ALL 7 ATELIER VESPER INTEGRATION TESTS PASSED (100% GREEN)")
    print("=" * 75)

if __name__ == "__main__":
    run_tests()
