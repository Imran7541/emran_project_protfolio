# Specification: High-Fidelity Video Thumbnails for Facebook Reels Carousel

```yaml
feature_id: "009-video-thumbnails"
feature_name: "High-Fidelity Video Thumbnails for Facebook Reels"
status: "completed"
owner: "Emran Hosen"
last_updated: "2026-10-31"
tech_stack:
  framework: "HTML5 / Tailwind CSS / Image Assets / Vanilla JS"
  thumbnails:
    ep01: "assets/thumbnails/ep01_will_ai_replace_devs.jpg"
    ep02: "assets/thumbnails/ep03_why_hire_engineers.jpg" # "AI CODING TRAP! Workflow vs Code"
    ep03: "assets/thumbnails/ep02_development_workflow.jpg" # "MCP Secret / AI Blind"
    ep04: "assets/thumbnails/ep04_coding_assistant_design.jpg" # "Agentic Dev & AI Engineering"
    ep05: "assets/thumbnails/ep05_multi_agent_systems.jpg" # "Autonomous Multi-Agent Systems"
    ep06: "assets/thumbnails/ep06_zero_trust_security.jpg" # "Zero-Trust Security in AI Apps"
```

---

## 1. Context & User Intent
The user specifically requested:
*"vai amer video er thambel ta thakle valo hoito tmi ki bolo"*
(Translation: "Brother, it would be great if my videos had thumbnails, what do you think?")

**User Insight Analysis**:
Having authentic, visual thumbnails transforms the video cards from abstract cards into recognizable, high-converting video previews. Visitors can instantly recognize Emran Hosen and the exact subject matter of each episode before clicking to play in the modal player.

---

## 2. Behavioral Specifications (Gherkin BDD)

### Scenario 1: Video Card Poster Renders Real Thumbnail Image
```gherkin
Given a visitor navigates to "gallery.html"
When the Facebook Reels continuous carousel renders
Then each card must display its authentic high-resolution video thumbnail
And the image must have object-cover scaling with smooth zoom on card hover
And a dark gradient vignette must overlay the image to maintain crisp readability for badges and play buttons
```

### Scenario 2: High Performance & Zero Stutter
```gherkin
Given the continuous motion track is translating at 45s linear
When thumbnail images are displayed
Then images must load smoothly with loading="lazy"
And transforms must remain 100% GPU-composited without frame drops or repaint jank
```

---

## 3. Tasks Breakdown (`speckit-tasks`)

### Phase 1: Asset Preparation & Routing
- [x] T001 Fetch and store authentic Facebook Reel thumbnails in `assets/thumbnails/`
- [x] T002 Generate high-fidelity branded thumbnails for upcoming episodes 05 and 06
- [x] T003 Verify static server routing for `assets/thumbnails/*.jpg` (returns HTTP 200)

### Phase 2: Video Card Markup Enhancement
- [x] T004 Update Set A (Cards 1–6) in `gallery.html` with `<img>` poster thumbnails, hover zoom, and dark gradient overlays
- [x] T005 Update Set B (Duplicated Cards 1–6) in `gallery.html` to mirror Set A for seamless infinite looping

### Phase 3: Verification & Live Preview
- [x] T006 Capture live screenshots of `#serial-facebook` using headless Chrome CDP
- [x] T007 Visually verify typography contrast, badge visibility, and play button glow against thumbnails
- [x] T008 Update `notes/PROJECT_STATE.md` and `notes/AGENT_HANDOVER.md`
