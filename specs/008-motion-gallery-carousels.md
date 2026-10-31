# Specification: Bidirectional Motion Carousels & Video Modal for Gallery

```yaml
feature_id: "008-motion-gallery-carousels"
feature_name: "Bidirectional Motion Carousels & Modal Player for Gallery"
status: "completed"
owner: "Emran Hosen"
last_updated: "2026-10-31"
tech_stack:
  framework: "HTML5 / Tailwind CSS / Hardware-Accelerated CSS3 Animations / Vanilla JS"
  animation_engine: "Motion & UI-UX Pro Max Bidirectional Carousels"
  ux_enhancements:
    - "Serial 1 (Facebook Reels): Right-to-Left continuous stream with modal preview"
    - "Serial 2 (LinkedIn Posts): Left-to-Right continuous stream with modal preview"
    - "Cinematic zero-friction Video Modal Player"
    - "Edge gradient masks, pause-on-hover, and drag-friendly layout"
    - "Massive vertical footprint reduction from ~1600px to ~420px per serial"
```

---

## 1. Context & User Intent
The user reported that the current `gallery.html` layout looks unprofessional and bulky due to oversized 2x2 static cards and heavy embedded iframes:
*"vai amer gallery site ta khub unprofessonal lagce soo ekhane video gulo right site thke left site a jabe ar linkedin videogulo same hobe left thke right site a jabe ar fb er too aro video add korbo tai motion hoile jaiga kom laglo ar sob video gulo dekher option pailo jeta valo lagbe click kore dokhbe thik ace bro"*

**Solution**:
1. Transform Serial 1 (Facebook Reels) into a sleek continuous carousel gliding **Right to Left**.
2. Transform Serial 2 (LinkedIn Insights) into a complementary continuous carousel gliding **Left to Right**.
3. Drastically compress vertical height so dozens of videos can be added without overwhelming the page.
4. Integrate an instant, lightweight **Cinematic Video Modal Player** so visitors can click any video card to watch it in full resolution with audio controls, without loading 20 heavy iframes on initial load.

---

## 2. Behavioral Specifications (Gherkin BDD)

### Scenario 1: Facebook Reels Continuous Right-to-Left Motion
```gherkin
Given a visitor navigates to "gallery.html"
When the page loads
Then the Facebook Reels cards in Serial 1 must stream continuously from Right to Left
And the carousel must display vertical 9:16 aspect ratio video cards with episode badges, titles, and play buttons
And both edges of the carousel must have soft linear gradient alpha masks
And hovering over any card must pause the animation and illuminate the card with a coral glow
```

### Scenario 2: LinkedIn Articles Continuous Left-to-Right Motion
```gherkin
Given a visitor scrolls to Serial 2 (LinkedIn Articles & Case Studies)
When the section renders
Then the LinkedIn cards must stream continuously from Left to Right (opposing flow to Serial 1)
And hovering over any card must pause the animation
And visitors must have direct links to read full articles on LinkedIn
```

### Scenario 3: Instant Cinematic Modal Playback
```gherkin
Given a visitor is watching the moving carousel
When the visitor clicks "Watch Reel" or the play button on any video card
Then an elegant full-screen modal with dark backdrop blur must appear instantly
And the selected Facebook Reel or LinkedIn embed must load and play inside the modal
And the visitor can close the modal via the "✕" button, pressing ESC, or clicking the backdrop
```

---

## 3. Tasks Breakdown (`speckit-tasks`)

### Phase 1: CSS Animation & Layout Foundation
- [x] T001 Implement `@keyframes gallery-scroll-left` and `@keyframes gallery-scroll-right` with GPU composited transforms (`translate3d`)
- [x] T002 Implement `.gallery-mask` gradient edge fading for 100% organic boundary transitions
- [x] T003 Implement card hover states (`hover:pause`, card elevation, coral border glow)

### Phase 2: Facebook Reels Carousel Redesign
- [x] T004 Restructure Serial 1 into compact executive video cards (280px x 400px) with play icons, episode badges, and metadata
- [x] T005 Duplicate cards for a seamless 100% infinite mathematical loop
- [x] T006 Add support for Episodes 01 through 06+

### Phase 3: LinkedIn Case Studies Carousel Redesign
- [x] T007 Restructure Serial 2 into compact executive landscape cards (360px x 320px)
- [x] T008 Configure Left-to-Right continuous infinite stream (`gallery-scroll-right`)
- [x] T009 Duplicate cards for 100% seamless looping

### Phase 4: Cinematic Video Modal Player
- [x] T010 Build `<div id="video-modal">` with backdrop blur, responsive 9:16 container, and dynamic iframe loader
- [x] T011 Implement `openVideoModal(embedUrl, title)` and `closeVideoModal()` with keyboard `Escape` support
- [x] T012 Connect all video cards in Serial 1 and Serial 2 to the modal player

### Phase 5: Verification & Documentation
- [x] T013 Verify live rendering at `http://localhost:5225/gallery.html` using headless Chrome CDP
- [x] T014 Capture preview screenshots of bidirectional carousels and modal player
- [x] T015 Update `notes/PROJECT_STATE.md` and `notes/AGENT_HANDOVER.md`
