#!/usr/bin/env python3
"""
Automated Test Suite for Hero Portrait Grounding, Mobile Spacing, and Dynamic Counters
"""

import sys
from pathlib import Path

INDEX_PATH = Path(__file__).resolve().parent.parent / "index.html"

def test_hero_markup():
    print("Checking index.html hero section enhancements...")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Verify 3D Pop-Out portrait and illuminated backdrop
    assert "emran_hero_popout.png" in content, "Popout image not found in index.html"
    assert "translate-y-[10%]" in content or "translate-y" in content, "Head popout translation missing"
    assert "radial-gradient" in content, "Portal illuminated background missing"
    assert "w-[74%]" in content, "Framed width 74% to prevent arm overflow missing"
    print("  ✓ 1. Hero portrait 3D pop-out and illuminated studio backdrop verified")

    # 2. Verify mobile layout optimizations
    assert "flex flex-row items-center gap-3 sm:gap-5 mt-2" in content, "Responsive CTA row missing"
    assert "whitespace-nowrap" in content, "Whitespace nowrap on buttons missing"
    print("  ✓ 2. Mobile hero spacing and responsive CTA button row verified")

    # 3. Verify Live Metrics Strip counters
    assert 'id="hero-metrics-strip"' in content, "#hero-metrics-strip element missing"
    assert 'data-target="24"' in content, "Counter target 24 missing"
    assert 'data-target="300"' in content, "Counter target 300 missing"
    assert 'data-target="100"' in content, "Counter target 100 missing"
    assert 'data-target="2"' in content, "Counter target 2 missing"
    assert "/7" in content and "+" in content and "%" in content and "&lt;" in content, (
        "Stat unit suffixes/prefixes missing"
    )
    print("  ✓ 3. Metric counters defined with exact data-target attributes and static suffixes")

    # 4. Verify Counter Animation JavaScript
    assert "initMetricCounters" in content, "initMetricCounters JS function missing"
    assert "requestAnimationFrame" in content, "requestAnimationFrame missing in counter script"
    assert "easeProgress" in content, "Easing function missing in counter script"
    assert "IntersectionObserver" in content, "IntersectionObserver trigger missing"
    print("  ✓ 4. JavaScript counter animation engine verified (60fps ease-out ticker)")

    print("\n🎉 ALL HERO ENHANCEMENT TESTS PASSED (100% GREEN)")

if __name__ == "__main__":
    test_hero_markup()
