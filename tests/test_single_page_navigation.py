#!/usr/bin/env python3
"""
Test Suite: Spec 023 Unified Single-Page Architecture & Navigation Integrity
Validates:
1. "Gallery" link is strictly absent from desktop navigation across index.html and contact.html
2. "Gallery" link is strictly absent from mobile drawer across index.html and contact.html
3. "Gallery" is absent from the executive footer Navigation column across index.html and contact.html
4. Single-page navigation anchors (#, #about, #works, contact) are present and properly configured
5. In-page sections (#hero, #about, #works) exist in index.html matching navigation targets
"""

import os
import sys
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_file(rel_path):
    path = os.path.join(ROOT_DIR, rel_path)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def run_tests():
    print("=" * 75)
    print("🧭 RUNNING SPEC 023 UNIFIED SINGLE-PAGE NAVIGATION TEST SUITE")
    print("=" * 75)

    index_html = read_file("index.html")
    contact_html = read_file("contact.html")

    # 1. Check Desktop Navigation on index.html
    nav_desktop_match = re.search(r'<div class="hidden md:flex[^>]*>(.*?)</div>', index_html, re.DOTALL)
    assert nav_desktop_match, "index.html missing desktop navigation container!"
    nav_desktop = nav_desktop_match.group(1)
    assert "gallery" not in nav_desktop.lower(), "index.html desktop navigation must not contain gallery link!"
    assert "home" in nav_desktop.lower(), "index.html desktop navigation missing Home link"
    assert "#about" in nav_desktop, "index.html desktop navigation missing #about anchor"
    assert "#works" in nav_desktop, "index.html desktop navigation missing #works anchor"
    assert "contact" in nav_desktop.lower(), "index.html desktop navigation missing Contact link"
    print("✅ 1. index.html desktop navigation verified: Gallery absent, Home/About/Project/Contact present")

    # 2. Check Mobile Drawer on index.html
    drawer_match = re.search(r'<div id="mobile-drawer"[^>]*>(.*?)</div>', index_html, re.DOTALL)
    assert drawer_match, "index.html missing mobile drawer container!"
    drawer = drawer_match.group(1)
    assert "gallery" not in drawer.lower(), "index.html mobile drawer must not contain gallery link!"
    assert "#about" in drawer, "index.html mobile drawer missing #about anchor"
    assert "#works" in drawer, "index.html mobile drawer missing #works anchor"
    assert "contact" in drawer.lower(), "index.html mobile drawer missing Contact link"
    print("✅ 2. index.html mobile drawer verified: Gallery absent, clean single-page items present")

    # 3. Check Footer Navigation Column on index.html
    footer_nav_match = re.search(r'Navigation</h4>\s*<ul[^>]*>(.*?)</ul>', index_html, re.DOTALL)
    assert footer_nav_match, "index.html missing footer navigation list!"
    footer_nav = footer_nav_match.group(1)
    assert "gallery" not in footer_nav.lower(), "index.html footer navigation must not contain gallery link!"
    print("✅ 3. index.html footer navigation column verified: Gallery link completely eliminated")

    # 4. Check contact.html Navigation Parity
    contact_desktop_match = re.search(r'<div class="hidden md:flex[^>]*>(.*?)</div>', contact_html, re.DOTALL)
    assert contact_desktop_match, "contact.html missing desktop navigation container!"
    contact_desktop = contact_desktop_match.group(1)
    assert "gallery" not in contact_desktop.lower(), "contact.html desktop navigation must not contain gallery link!"

    contact_drawer_match = re.search(r'<div id="mobile-drawer"[^>]*>(.*?)</div>', contact_html, re.DOTALL)
    assert contact_drawer_match, "contact.html missing mobile drawer container!"
    contact_drawer = contact_drawer_match.group(1)
    assert "gallery" not in contact_drawer.lower(), "contact.html mobile drawer must not contain gallery link!"

    contact_footer_match = re.search(r'Navigation</h4>\s*<ul[^>]*>(.*?)</ul>', contact_html, re.DOTALL)
    assert contact_footer_match, "contact.html missing footer navigation list!"
    contact_footer = contact_footer_match.group(1)
    assert "gallery" not in contact_footer.lower(), "contact.html footer navigation must not contain gallery link!"
    print("✅ 4. contact.html navigation parity verified: Gallery completely eliminated from nav and footer")

    # 5. In-Page Section Anchors Exist in index.html
    assert 'id="hero"' in index_html or 'id="hero-metrics-strip"' in index_html, "Hero section ID missing"
    assert 'id="about"' in index_html, "About section ID missing for #about anchor"
    assert 'id="works"' in index_html, "Works section ID missing for #works anchor"
    print("✅ 5. Single-page in-page section anchors (#about, #works) verified in index.html")

    print("=" * 75)
    print("🎉 ALL SPEC 023 SINGLE-PAGE NAVIGATION TESTS PASSED (100% GREEN)")
    print("=" * 75)

if __name__ == "__main__":
    run_tests()
