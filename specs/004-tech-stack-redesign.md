# Specification: Modern Visual Tech Stack with Brand Icons & Compact Proportions

```yaml
feature_id: "004-tech-stack-redesign"
feature_name: "Visual Technology Stack with Colored Brand SVGs"
status: "in-progress"
owner: "Emran Hosen"
last_updated: "2026-10-31"
tech_stack:
  framework: "HTML5 / Tailwind CSS / Inline Vector SVGs"
  design_system: "Cinematic Dark Noir (#121E27, #FF715B coral accent, Montserrat typography)"
  target_reference: "Image 1 (Brand colored logos with labels, compact executive sizing)"
```

## 1. Context & Business Intent
The user requested upgrading the plain text-only `#stack` tooling section on the homepage (`index.html`) to match the visual technology badge design shown in reference Image 1 (featuring official colored brand icons/logos for HTML5, CSS3, JavaScript, TypeScript, React, Node.js, Git, etc.). The user explicitly specified: *"amer ta tee design dao tbe size ta ektu soto koro"* (apply the design to mine, but make the size a bit smaller / compact).

---

## 2. Behavioral Specifications (Gherkin BDD)

### Scenario 1: Visual Brand Icon Presentation
```gherkin
Given a visitor navigates to the "#stack" section on "index.html"
When the section renders
Then every technology item must display an authentic brand-colored vector SVG icon alongside its label
And the icons must include HTML5, CSS3, JavaScript, TypeScript, React, Next.js, Node.js, Python, Three.js, Tailwind CSS, PostgreSQL, Docker, Git, and AI Agents
```

### Scenario 2: Compact & Professional Proportions
```gherkin
Given the technology badges are displayed
When viewed on desktop (1440px) or mobile (390px)
Then the icon dimensions must remain compact (20px to 24px) without visual distortion
And each badge must feature glassmorphic styling (rounded-xl, subtle border, smooth hover elevation)
And badges must wrap fluidly and remain balanced and centered
```

---

## 3. Tasks Breakdown
- [ ] T001 Craft high-precision brand SVGs for all core technologies (HTML5, CSS3, JS, TS, React, Next.js, Node.js, Python, Three.js, Tailwind, Postgres, Docker, Git, AI Agents)
- [ ] T002 Replace plain text pills in `index.html` with compact, glassmorphic icon badges
- [ ] T003 Verify responsive layout and compact sizing via headless Chrome screenshots
- [ ] T004 Update `notes/PROJECT_STATE.md` and `notes/AGENT_HANDOVER.md`
