# Spec 026: Atelier Vesper Luxury Interior Architecture & Spatial Design Platform Showcase Ingestion

## 1. Executive Summary
- **Project Name**: Atelier Vesper — Luxury Interior Architecture & Spatial Design Platform
- **Live URL**: `https://atelier-vesper-marketing.imranrband100.workers.dev`
- **GitHub Repository**: `https://github.com/Imran7541/atelier-vesper`
- **Category**: High-End Architectural WebGL, Spatial Design & Turnkey Estimator
- **Type**: Public Open Source (`projectType: "public"`)
- **Key Technologies**: React 19, TypeScript 5.7, Vite 6, Three.js (WebGL Procedural Atrium), Framer Motion 12, Tailwind CSS, Cloudflare Workers, Node.js + Express, SQLite.

---

## 2. Architecture & Design Specification

### 2.1 Project Metadata (`data/projects.json`)
```json
{
  "id": 10,
  "slug": "atelier-vesper-architecture",
  "title": "Atelier Vesper: Luxury Interior Architecture & Spatial Design",
  "category": "Architectural WebGL, Spatial 3D & Turnkey Estimator Platform",
  "projectType": "public",
  "period": "2026 Production",
  "badge": "Public Open Source",
  "badgeColor": "accent",
  "status": "Cloudflare Workers Live",
  "statusColor": "emerald",
  "previewImage": "assets/atelier_vesper_preview.png",
  "description": "High-performance editorial platform engineered for luxury interior architecture, bespoke millwork, and turnkey residential spaces. Combines procedural Three.js WebGL architectural modeling, scroll-scrubbed camera choreography, an instant turnkey investment estimator, and sub-50ms Cloudflare Workers edge delivery.",
  "tags": ["React 19", "Three.js", "TypeScript", "Framer Motion", "Tailwind CSS", "Cloudflare Workers", "SQLite"],
  "repoUrl": "https://github.com/Imran7541/atelier-vesper",
  "hasPublicRepo": true,
  "confidentiality": null,
  "liveDemoUrl": "https://atelier-vesper-marketing.imranrband100.workers.dev",
  "liveTelemetry": {
    "rendering": "Three.js Procedural Atrium",
    "framework": "React 19 + Vite 6",
    "deployment": "Cloudflare Workers Edge",
    "speed": "Sub-50ms Global Response",
    "repo": "Public Open Source"
  }
}
```

### 2.2 Visual Preview Asset
- **File**: `assets/atelier_vesper_preview.png`
- **Resolution**: Exactly `1280x720` (16:9 standard aspect ratio).
- **Quality**: Crystal clear, captures the luxury architectural hero section and procedural 3D elements.

### 2.3 UI Integration (`index.html`)
- **Location**: In `#projects-grid` after Bistro Élysée.
- **Card Type**: `data-project-type="public"`.
- **Theme Accents**: Warm architectural travertine / bronze glow (`rgba(197, 160, 115, 0.15)` and `#FF715B` coral accents).
- **Actions**:
  - Live preview action: `Visit Atelier` -> `https://atelier-vesper-marketing.imranrband100.workers.dev`
  - Bottom actions: `Live Platform` and `GitHub` link to `https://github.com/Imran7541/atelier-vesper`.
  - Telemetry badge: `Cloudflare Workers Live`.
- **Counters & Filters**:
  - `All Flagship Works (10)`
  - `Public Works (7)`
  - `Enterprise Private Systems (3)`
  - Section summary: `(7 Public • 3 Private)`

### 2.4 Conversational AI Coverage
- `data/ai-knowledge.json`: Add Atelier Vesper to `flagshipProjects` and `faqMatchers`.
- `js/ai-widget.js`: Add Atelier Vesper keywords and rich HTML answer with links to live platform and GitHub repo.
- `server.js`: Include Atelier Vesper in `queryEmranAI` systemPrompt and flagship works list.
- `functions/api/chat.js`: Include Atelier Vesper in `KNOWLEDGE_FAQ` and systemPrompt for Cloudflare Edge parity.

---

## 3. Gherkin BDD Scenarios

```gherkin
Feature: Atelier Vesper Luxury Architecture Flagship Ingestion
  Scenario: Visitor explores Flagship Works on the Portfolio
    Given the portfolio homepage "index.html" is loaded
    When the visitor scrolls to "#works"
    Then they should see "Atelier Vesper: Luxury Interior Architecture & Spatial Design"
    And the card should display both "Live Platform" and "GitHub" repository links
    And the filter counters should display "All Flagship Works (10)" and "Public Works (7)"

  Scenario: Visitor filters for Public Works
    Given the visitor is at the "#works" section
    When the visitor clicks "Public Works (7)"
    Then the Atelier Vesper card should remain visible
    And exactly 7 public cards should be displayed

  Scenario: Visitor queries Emran AI about architecture or 3D interior design
    Given the visitor opens the Emran AI chat widget
    When the visitor submits "Tell me about Atelier Vesper" or "What interior architecture projects has Emran built?"
    Then the assistant should provide detailed information about Atelier Vesper
    And include links to https://atelier-vesper-marketing.imranrband100.workers.dev and GitHub
```
