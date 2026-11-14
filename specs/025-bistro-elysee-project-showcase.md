# Spec 025: Bistro Élysée Project Showcase & European Fine Dining Integration

## 1. Metadata & Context
```yaml
feature_id: "025-bistro-elysee-project-showcase"
title: "Bistro Élysée Gulshan Flagship Project Integration"
author: "Hermes Agent & Emran Hosen"
status: "Draft -> In-Progress"
created_at: "2026-11-14T20:41:00+06:00"
category: "Commercial European Fine Dining & Artisan Patisserie Platform"
live_url: "https://bistro-elysee-gulshan.pages.dev"
tech_stack:
  - "React 18"
  - "Vite"
  - "Framer Motion"
  - "Tailwind CSS"
  - "Lucide Icons"
  - "Cloudflare Pages Edge Runtime"
  - "PWA Responsive Layout"
```

## 2. Executive Overview
Emran Hosen has engineered and deployed **Bistro Élysée | Contemporary European Bistro & Artisan Patisserie** ([https://bistro-elysee-gulshan.pages.dev](https://bistro-elysee-gulshan.pages.dev)), an upscale contemporary European dining and luxury bakery platform situated along the Gulshan 2 Lakeside Promenade in Dhaka. Overlooking Gulshan Lake with curated fine art ambiance, the platform features artisanal French & European pastry showcases, single-origin coffee, an interactive table booking system, and dynamic culinary menu cards with sub-50ms Cloudflare Edge delivery.

This specification governs the seamless ingestion of Bistro Élysée as a premier flagship project on Emran's portfolio website (`index.html`), updating project data models (`data/projects.json`), filter categories (total projects: 9, public works: 6, private systems: 3), and the "Emran AI" conversational knowledge base (`data/ai-knowledge.json`, `js/ai-widget.js`, `server.js`, and `functions/api/chat.js`).

## 3. Architecture & Data Contracts

### 3.1 Data Model: `data/projects.json`
```json
{
  "id": 9,
  "slug": "bistro-elysee-gulshan",
  "title": "Bistro Élysée: European Bistro & Artisan Patisserie",
  "category": "Commercial European Fine Dining & Artisan Patisserie Platform",
  "projectType": "public",
  "period": "2026 Production",
  "badge": "Production Platform",
  "badgeColor": "amber",
  "status": "Cloudflare Edge Live",
  "statusColor": "amber",
  "previewImage": "assets/bistro_elysee_preview.png",
  "description": "Contemporary European fine dining and artisanal patisserie along Gulshan-2 Lakeside Promenade. Engineered with React 18, Vite, Tailwind CSS, Framer Motion, and sub-50ms Cloudflare Edge delivery with PWA offline-ready dining catalog.",
  "tags": ["React 18", "Vite", "Framer Motion", "Tailwind CSS", "Cloudflare Pages", "Lucide Icons", "PWA"],
  "repoUrl": null,
  "hasPublicRepo": false,
  "confidentiality": "Commercial Client Production • Live in Gulshan-2",
  "liveDemoUrl": "https://bistro-elysee-gulshan.pages.dev",
  "liveTelemetry": {
    "location": "Gulshan-2 Lakeside Promenade",
    "architecture": "React 18 + Vite + Framer Motion",
    "deployment": "Cloudflare Pages Edge",
    "speed": "Sub-50ms Edge Response"
  }
}
```

### 3.2 UI Integration in `index.html`
- **Location**: Injected as the third card in `#projects-grid` alongside `Familio Bazar` and `EMBER CAFE`.
- **Card Aesthetics**:
  - Gradient glow: `amber-400/10` with hover glow `amber-400/20`
  - 16:9 Aspect Video Preview Window containing `assets/bistro_elysee_preview.png`
  - Top-Right Floating Action Tag: `Visit Bistro` (`https://bistro-elysee-gulshan.pages.dev`)
  - Bottom-Left Telemetry Pill: `Lakeside Promenade Live` with emerald pulse indicator
  - Header Chips: `Production Platform` and `2026 Production`
  - Tech Pills: `React 18`, `Vite`, `Framer Motion`, `Tailwind CSS`, `Cloudflare Edge`, `PWA Ready`
  - Footer Action: `Live Platform` button with external launch icon, `Gulshan 2 Lakeside` location chip, and `Live on Cloudflare Edge` green pulse badge.
- **Category Filter Counters**:
  - All Flagship Works: `9`
  - Public Works: `6`
  - Enterprise Private Systems: `3`
  - Section Summary: `(6 Public • 3 Private)`

### 3.3 AI Knowledge Ingestion
- `data/ai-knowledge.json`, `js/ai-widget.js`, `server.js`, and `functions/api/chat.js` are updated with full answers and FAQ triggers for questions regarding:
  - Bistro Élysée
  - Gulshan-2 European restaurant / bistro
  - French bakery / artisan patisserie
  - React 18 & Framer Motion commercial web apps

## 4. BDD Scenarios (Gherkin)

```gherkin
Feature: Bistro Élysée Gulshan Project Showcase Integration

  Scenario: Visitor discovers Bistro Élysée in Flagship Works
    Given a visitor browses the "#works" section on "index.html"
    When the projects grid renders
    Then the visitor should see "Bistro Élysée: European Bistro & Artisan Patisserie"
    And the card should display the high-resolution 16:9 preview "assets/bistro_elysee_preview.png"
    And clicking "Live Platform" should open "https://bistro-elysee-gulshan.pages.dev" in a new tab

  Scenario: Visitor filters projects by category
    Given the visitor is on the "#works" section
    When the visitor clicks "Public Works (6)"
    Then the Bistro Élysée card should remain visible
    And the card dataset "data-project-type" should equal "public"
    When the visitor clicks "Enterprise Private Systems (3)"
    Then the Bistro Élysée card should be hidden
    When the visitor clicks "All Flagship Works (9)"
    Then all 9 projects should be visible

  Scenario: Visitor asks AI Assistant about Bistro Élysée
    Given the visitor opens the "Emran AI" chat widget
    When the visitor asks "Tell me about Bistro Elysee in Gulshan"
    Then the AI assistant should respond with details about the European fine dining, artisan patisserie, React 18 stack, and the live link "https://bistro-elysee-gulshan.pages.dev"
```
