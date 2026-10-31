# Specification: Dedicated Cinematic Gallery Page & Video Reorganization

```yaml
feature_id: "003-cinematic-gallery-page"
feature_name: "Dedicated Cinematic Gallery Page & Home Video Extraction"
status: "in-progress"
owner: "Emran Hosen"
last_updated: "2026-10-30"
tech_stack:
  framework: "HTML5 / Tailwind CSS CDN / Three.js WebGL / Swiper JS"
  design_system: "Cinematic Dark Noir (#121E27, #FF715B coral accent, Montserrat & Inter typography)"
  embed_apis:
    - "Facebook Reels Plugin API"
    - "LinkedIn UGC Post Embed API"
```

## 1. Context & Business Intent
The user requested removing the video gallery from the homepage (`index.html`) so videos do not appear on initial page load, and moving all videos to a dedicated `gallery.html` page. In this dedicated gallery, Facebook Reels and LinkedIn featured posts must be organized separately in their own serials (Facebook Reels first, followed by LinkedIn posts), sized with professional dimensions, and styled with high-fidelity cinematic UI.

---

## 2. Behavioral Specifications (Gherkin BDD)

### Scenario 1: Clean Homepage View without Video Clutter
```gherkin
Given a visitor navigates to the homepage "http://localhost:5225/"
When the homepage is rendered
Then the "#gallery" section must not appear on the homepage
And clicking the "Gallery" navigation link must direct the visitor to "gallery.html"
```

### Scenario 2: Serialized Media Layout on Dedicated Gallery Page
```gherkin
Given a visitor navigates to "http://localhost:5225/gallery.html"
When the gallery page loads
Then Facebook Reels must be grouped together in Serial 1 (4 vertical cards)
And LinkedIn Posts must be grouped together in Serial 2 (3 feed cards)
And the YouTube upcoming channel must be displayed in Serial 3
And all cards must maintain proper aspect ratios without distortion
```

### Scenario 3: Platform Filtering and Responsive Design
```gherkin
Given a visitor is on "gallery.html"
When the visitor clicks "Facebook (4)"
Then only the Facebook Reels serial is highlighted and shown
When the visitor clicks "LinkedIn (3)"
Then only the LinkedIn Posts serial is highlighted and shown
When the visitor clicks "All Content (7)"
Then all serialized sections are displayed
And on mobile viewports (<= 768px), cards stack vertically or swipe seamlessly
```

---

## 3. Tasks Breakdown

- [ ] T001 Remove gallery section (`#gallery`, lines 430-815) from `index.html`
- [ ] T002 Update `Gallery` navigation links in `index.html` desktop navbar and mobile drawer to `gallery.html`
- [ ] T003 Create `gallery.html` with Three.js deep-sea WebGL background, cinematic navbar, and Montserrat styling
- [ ] T004 Implement Serial 1: 4 Facebook Reels in dedicated 4-column responsive grid with 9:16 vertical aspect ratio
- [ ] T005 Implement Serial 2: 3 LinkedIn Posts in dedicated 3-column responsive grid with readable feed dimensions
- [ ] T006 Implement Serial 3: YouTube Masterclass channel banner with CTA
- [ ] T007 Implement interactive platform filter pills (`All`, `Facebook`, `LinkedIn`, `YouTube`) and smooth transitions
- [ ] T008 Add footer, communication buttons, and email copy toast in `gallery.html`
- [ ] T009 Visually verify both `index.html` and `gallery.html` via headless Chrome screenshots
- [ ] T010 Update `notes/PROJECT_STATE.md` and `notes/AGENT_HANDOVER.md`
