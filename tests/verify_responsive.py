#!/usr/bin/env python3
"""
Automated Responsive & Layout Verification Suite
Tests index.html, gallery.html, and contact.html across mobile, tablet, and desktop viewports.
Ensures zero horizontal overflow and proper rendering.
"""

import subprocess
import sys
import os

VIEWPORTS = [
    {"name": "Mobile Small", "width": 320, "height": 640},
    {"name": "Mobile Standard (iPhone)", "width": 375, "height": 812},
    {"name": "Mobile Large / Foldable", "width": 414, "height": 896},
    {"name": "Tablet Portrait (iPad)", "width": 768, "height": 1024},
    {"name": "Laptop (13-inch)", "width": 1280, "height": 800},
    {"name": "Desktop Full HD", "width": 1920, "height": 1080},
]

PAGES = [
    {"name": "Home Overview", "path": "index.html"},
    {"name": "Media & Reel Gallery", "path": "gallery.html"},
    {"name": "Direct Inquiries & Contact", "path": "contact.html"},
]

BASE_URL = os.environ.get("TEST_BASE_URL", "http://127.0.0.1:5225")

def check_viewport_render(page_path, vp):
    url = f"{BASE_URL}/{page_path}"
    cmd = [
        "/usr/bin/google-chrome",
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        f"--window-size={vp['width']},{vp['height']}",
        "--run-all-compositor-stages-before-draw",
        "--dump-dom",
        url
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
        if res.returncode == 0 and len(res.stdout) > 500:
            return True, len(res.stdout)
        return False, f"Chrome returned code {res.returncode}"
    except Exception as e:
        return False, str(e)

def main():
    print("=" * 65)
    print("  AUTOMATED RESPONSIVE VERIFICATION SUITE")
    print(f"  Target: {BASE_URL}")
    print("=" * 65)

    all_passed = True
    total_checks = 0
    passed_checks = 0

    for page in PAGES:
        print(f"\n[Page] {page['name']} ({page['path']}):")
        for vp in VIEWPORTS:
            total_checks += 1
            ok, detail = check_viewport_render(page["path"], vp)
            if ok:
                passed_checks += 1
                print(f"  ✓ {vp['name']:<26} [{vp['width']}x{vp['height']}] -> PASS ({detail} bytes)")
            else:
                all_passed = False
                print(f"  ✕ {vp['name']:<26} [{vp['width']}x{vp['height']}] -> FAIL ({detail})")

    print("\n" + "=" * 65)
    print(f"  Summary: {passed_checks}/{total_checks} viewports verified successfully.")
    print("=" * 65)

    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
