#!/usr/bin/env python3
"""
Test Suite: Real Contact Channels & OpenGraph / Favicon SEO Integrity
Validates:
1. Favicon SVG existence, validity, and inclusion in all HTML pages
2. OpenGraph & Twitter Card metadata across index.html, gallery.html, and contact.html
3. Verified Direct Channels across contact.html, index.html, and gallery.html:
   - WhatsApp (+880 1706-754148 / https://wa.me/8801706754148)
   - Discord Community (https://discord.gg/VxDzexfEN)
   - Primary Email (imrandt2001@gmail.com)
   - Absence of placeholder contact numbers (+880 1900-000000)
4. AI Knowledge Base & Fallback Widget channel parity
5. Live API chat endpoint returns verified contact details
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error

PORT = 5225
BASE_URL = f"http://127.0.0.1:{PORT}"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_file(rel_path):
    path = os.path.join(ROOT_DIR, rel_path)
    with open(path, "r", encoding="utf-8") as f:
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
    print("🌐 RUNNING REAL CONTACT CHANNELS & OPENGRAPH SEO TEST SUITE")
    print("=" * 75)

    # 1. Favicon SVG Check
    favicon_path = os.path.join(ROOT_DIR, "favicon.svg")
    assert os.path.exists(favicon_path), "favicon.svg does not exist in root!"
    favicon_content = read_file("favicon.svg")
    assert "<svg" in favicon_content and "</svg>" in favicon_content, "favicon.svg is not a valid SVG!"
    assert "#FF715B" in favicon_content, "favicon.svg should use accent coral #FF715B"
    print("✅ 1. favicon.svg is present, valid SVG, and branded with coral #FF715B")

    # 2. Check Favicon Tag in All HTML Files
    html_files = ["index.html", "gallery.html", "contact.html", "404.html"]
    for f in html_files:
        content = read_file(f)
        assert 'rel="icon"' in content and 'favicon.svg' in content, f"{f} missing favicon.svg link tag!"
    print("✅ 2. All HTML files (index, gallery, contact, 404) properly declare favicon.svg")

    # 3. OpenGraph and Twitter Card Metadata Verification
    seo_pages = {
        "index.html": "https://emran-portfolio.pages.dev/",
        "gallery.html": "https://emran-portfolio.pages.dev/gallery",
        "contact.html": "https://emran-portfolio.pages.dev/contact"
    }
    for f, canonical in seo_pages.items():
        content = read_file(f)
        assert f'<link rel="canonical" href="{canonical}"' in content or f"href='{canonical}'" in content, f"{f} missing canonical link {canonical}"
        assert 'property="og:title"' in content, f"{f} missing og:title"
        assert 'property="og:description"' in content, f"{f} missing og:description"
        assert 'property="og:image"' in content, f"{f} missing og:image"
        assert 'property="og:url"' in content, f"{f} missing og:url"
        assert 'name="twitter:card"' in content, f"{f} missing twitter:card"
        assert 'name="twitter:title"' in content, f"{f} missing twitter:title"
    print("✅ 3. OpenGraph & Twitter Card metadata strictly verified on index, gallery, and contact")

    # 4. Verified WhatsApp, Discord, and Email Channels in contact.html
    contact_html = read_file("contact.html")
    assert "01706754148" in contact_html or "8801706754148" in contact_html, "contact.html missing user's WhatsApp number!"
    assert "https://wa.me/8801706754148" in contact_html, "contact.html missing verified WhatsApp link https://wa.me/8801706754148"
    assert "https://discord.gg/VxDzexfEN" in contact_html, "contact.html missing verified Discord link https://discord.gg/VxDzexfEN"
    assert "imrandt2001@gmail.com" in contact_html, "contact.html missing primary email imrandt2001@gmail.com"
    assert "8801900000000" not in contact_html, "contact.html still contains old placeholder WhatsApp number!"
    assert "+880 1900-000000" not in contact_html, "contact.html still contains old placeholder display number!"
    print("✅ 4. contact.html Direct Channels completely updated with real WhatsApp, Discord, and Email")

    # 5. Footer Channels Parity across index.html & gallery.html
    for f in ["index.html", "gallery.html"]:
        c = read_file(f)
        assert "https://wa.me/8801706754148" in c, f"{f} footer missing real WhatsApp link"
        assert "https://discord.gg/VxDzexfEN" in c, f"{f} footer missing real Discord link"
        assert "imrandt2001@gmail.com" in c, f"{f} footer missing real email"
        assert "8801900000000" not in c, f"{f} footer still contains placeholder WhatsApp number"
    print("✅ 5. Executive footers across index.html and gallery.html match real communication channels")

    # 6. AI Knowledge Base and Fallback Widget Parity
    ai_knowledge = json.loads(read_file("data/ai-knowledge.json"))
    contact_channels = ai_knowledge.get("profile", {}).get("contactChannels", {})
    assert contact_channels.get("email") == "imrandt2001@gmail.com", "ai-knowledge email mismatch"
    assert "1706-754148" in contact_channels.get("whatsapp", ""), "ai-knowledge whatsapp mismatch"
    assert contact_channels.get("discordCommunity") == "https://discord.gg/VxDzexfEN", "ai-knowledge discord mismatch"

    ai_widget_js = read_file("js/ai-widget.js")
    assert "8801706754148" in ai_widget_js, "ai-widget.js fallback missing real WhatsApp link"
    assert "discord.gg/VxDzexfEN" in ai_widget_js, "ai-widget.js fallback missing real Discord link"
    assert "imrandt2001@gmail.com" in ai_widget_js, "ai-widget.js fallback missing real email"
    print("✅ 6. AI Knowledge Base & Widget Fallback matrix updated with verified contact credentials")

    # 7. Live Server Integration & API Chat Verification
    status, res = make_request("/api/chat", method="POST", data={"message": "What is your WhatsApp and Discord?"})
    assert status == 200, f"Expected 200 from /api/chat, got {status}"
    reply = res.get("reply", "")
    assert "1706-754148" in reply or "discord.gg" in reply or "imrandt2001" in reply, f"AI Chat response missing contact info: {reply}"
    print(f"✅ 7. Live /api/chat accurately serves real communication channels: {reply[:80]}...")

    print("=" * 75)
    print("🎉 ALL 7 REAL CHANNELS & OPENGRAPH SEO TESTS PASSED (100% GREEN)")
    print("=" * 75)

if __name__ == "__main__":
    run_tests()
