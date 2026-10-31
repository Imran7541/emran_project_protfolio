# Specification: Bidirectional Infinite Motion Marquee for Technology Stack

```yaml
feature_id: "007-motion-tech-stack-marquee"
feature_name: "Bidirectional Dual-Lane Infinite Motion Marquee for Technical Skills"
status: "completed"
owner: "Emran Hosen"
last_updated: "2026-10-31"
tech_stack:
  framework: "HTML5 / Tailwind CSS / Hardware-Accelerated CSS3 Animations"
  animation_engine: "Motion & UI-UX Pro Max Marquee Architecture"
  performance: "120fps GPU-composited (translate3d & will-change)"
  ux_enhancements: "Alternating bidirectional motion, gradient edge masks, pause-on-hover"
```

---

## 1. Context & User Intent
The user requested: *"vai opurer line ta right site thke left site a ar nicher ta left site thke right site emon koro tahole aro better lagbe"* (Brother, make the upper line go from right side to left side, and the lower line go from left side to right side, that will look even better).

This bidirectional alternating marquee structure creates dynamic visual balance (popularized by Linear, Vercel, and Raycast design systems) where Lane 1 streams Right-to-Left and Lane 2 streams Left-to-Right.

---

## 2. Behavioral Specifications (Gherkin BDD)

### Scenario 1: Bidirectional Dual-Lane Continuous Motion
```gherkin
Given a visitor views the "#stack" (Tooling) section on "index.html"
When the section renders
Then the upper lane (Lane 1: Frontend & UI) must stream continuously from Right to Left
And the lower lane (Lane 2: Backend, Systems & AI) must stream continuously from Left to Right
And both lanes must feature zero visible seams, gaps, or stutters during loop resets
And all transforms must utilize "translate3d" on the GPU compositor thread for 120fps smoothness
```

### Scenario 2: Cinematic Edge Masking & Aesthetic Polish
```gherkin
Given the moving technology badge tracks
When badges approach the viewport boundaries
Then both left and right edges must feature soft linear gradient alpha masks (fade out to transparent)
And badges must smoothly emerge from the side voids and dissolve into the opposite abyss
```

### Scenario 3: Interactive Inspection (Pause on Hover)
```gherkin
Given either marquee track is actively streaming
When a user hovers a mouse or touches any badge on a track
Then that track must immediately pause ("animation-play-state: paused")
And the hovered badge must elevate slightly with a coral accent border glow (#FF715B)
When the user moves the pointer away
Then the track must resume its motion seamlessly from its exact paused position
```

---

## 3. Tasks Breakdown (`speckit-tasks`)

### Phase 1: Animation Mechanics
- [x] T001 Implement `@keyframes marquee-scroll-left` (`0% { translate3d(0,0,0) }` to `100% { translate3d(-50%,0,0) }`) for Lane 1 (Right to Left)
- [x] T002 Implement `@keyframes marquee-scroll-right` (`0% { translate3d(-50%,0,0) }` to `100% { translate3d(0,0,0) }`) for Lane 2 (Left to Right)
- [x] T003 Bind `animate-marquee-lane1` (32s linear infinite) to upper track
- [x] T004 Bind `animate-marquee-lane2` (34s linear infinite) to lower track

### Phase 2: Visual & Interaction Polish
- [x] T005 Preserve soft gradient edge vignettes via `.marquee-mask`
- [x] T006 Ensure pause-on-hover works independently per track
- [x] T007 Verify responsive rendering on mobile and desktop viewports

### Phase 3: Verification & Evidence
- [x] T008 Capture live headless Chrome screenshot of bidirectional motion
- [x] T009 Update `notes/PROJECT_STATE.md` and `notes/AGENT_HANDOVER.md`
