# Spec 024: Ember Cafe Gulshan Project Showcase & Hospitality Platform Integration

## 1. Metadata & Context
```yaml
feature_id: "024-ember-cafe-project-showcase"
title: "Ember Cafe Gulshan Flagship Project Integration"
author: "Hermes Agent & Emran Hosen"
status: "Draft -> In-Progress"
created_at: "2026-11-14T18:10:00+06:00"
category: "Commercial Hospitality & High-End Food-Tech Platform"
live_url: "https://ember-cafe-gulshan.pages.dev"
tech_stack:
  - "Next.js 15 (App Router)"
  - "Tailwind CSS"
  - "Cloudflare Pages Edge Runtime"
  - "Lucide Icons"
  - "PWA Responsive Layout"
```

## 2. Executive Overview
Emran Hosen has engineered and deployed **EMBER CAFE | Gulshan Rooftop Dining & Specialty Steaks** ([https://ember-cafe-gulshan.pages.dev](https://ember-cafe-gulshan.pages.dev)), a high-end commercial 22-hour rooftop cafe and steakhouse web platform in Gulshan-1, Dhaka. The platform features single-origin artisan coffee, charcoal-grilled steaks, a real-time live hours tracker (7:00 AM – 5:00 AM), interactive table reservation modal, and an online culinary menu ordering engine.

This specification governs the seamless ingestion of Ember Cafe as a premier flagship project on Emran's portfolio website (`index.html`), updating project data models (`data/projects.json`), filter categories (total projects: 8), and the "Emran AI" conversational knowledge base (`data/ai-knowledge.json` and `js/ai-widget.js`).

## 3. Architecture & Data Contracts

### 3.1 Data Model: `data/projects.json`
```json
{
  "id": 8,
  "slug": "ember-cafe-gulshan",
  "title": "EMBER CAFE: 22-Hour Rooftop Dining & Specialty Steaks",
  "category": "Commercial Hospitality & High-End Food-Tech Platform",
  "projectType": "public",
  "period": "2026 Production",
  "badge": "Production Platform",
  "badgeColor": "amber",
  "status": "Cloudflare Edge Live",
  "statusColor": "amber",
  "previewImage": "assets/ember_cafe_preview.png",
  "description": "Dhaka's premier 22-hour rooftop dining and steakhouse web platform in Gulshan-1. Built with Next.js 15 App Router, Tailwind CSS, real-time live hours tracker, table reservation booking engine, and artisan menu ordering with sub-50ms Cloudflare Edge delivery.",
  "tags": ["Next.js 15", "Tailwind CSS", "Cloudflare Pages", "Lucide Icons", "Edge Runtime", "PWA"],
  "repoUrl": null,
  "hasPublicRepo": false,
  "confidentiality": "Commercial Client Production • Live in Gulshan-1",
  "liveDemoUrl": "https://ember-cafe-gulshan.pages.dev",
  "liveTelemetry": {
    "hours": "22-Hour Daily (7 AM – 5 AM)",
    "architecture": "Next.js 15 App Router",
    "deployment": "Cloudflare Pages Edge",
    "speed": "Sub-50ms Edge Response"
  }
}
```

### 3.2 UI Integration in `index.html`
- **Location**: Injected as the second card in `#projects-grid` alongside `Familio Bazar`.
- **Card Aesthetics**:
  - Gradient glow: `amber-500/10` with hover glow `amber-500/20`
  - 16:9 Aspect Video Preview Window containing `assets/ember_cafe_preview.png`
  - Top-Right Floating Action Tag: `Live Experience` (`https://ember-cafe-gulshan.pages.dev`)
  - Bottom-Left Telemetry Pill: `22-Hour Rooftop Live` with emerald pulse indicator
  - Header Chips: `Production Platform` and `2026 Production`
  - Tech Pills: `Next.js 15`, `Tailwind CSS`, `Cloudflare Edge`, `Lucide Icons`, `Edge Runtime`
  - Footer Action: `Live Platform` button with external launch icon, Gulshan-1 location chip, and `Live on Cloudflare Edge` green pulse badge.
- **Category Filter Counters**:
  - All Flagship Works: `8`
  - Public Works: `5`
  - Enterprise Private Systems: `3`

### 3.3 AI Knowledge Ingestion
- `data/ai-knowledge.json` and `js/ai-widget.js` are updated with full answers and FAQ triggers for questions regarding:
  - Ember Cafe
  - Gulshan rooftop cafe
  - Restaurant/hospitality projects
  - Next.js 15 commercial web apps

## 4. BDD Scenarios (Gherkin)

```gherkin
Feature: Ember Cafe Gulshan Project Showcase Integration

  Scenario: Visitor discovers Ember Cafe in Flagship Works
    Given a visitor browses the "#works" section on "index.html"
    When the projects grid renders
    Then the visitor should see "EMBER CAFE: 22-Hour Rooftop Dining & Specialty Steaks"
    And the card should display the high-resolution 16:9 preview "assets/ember_cafe_preview.png"
    And clicking "Live Platform" should open "https://ember-cafe-gulshan.pages.dev" in a new tab

  Scenario: Visitor filters projects by category
    Given the visitor is on the "#works" section
    When the visitor clicks "Public Works (5)"
    Then the Ember Cafe card should remain visible
    And the card dataset "data-project-type" should equal "public"
    When the visitor clicks "Enterprise Private Systems (3)"
    Then the Ember Cafe card should be hidden
    When the visitor clicks "All Flagship Works (8)"
    Then all 8 projects should be visible

  Scenario: Visitor asks AI Assistant about Ember Cafe
    Given the visitor opens the "Emran AI" chat widget
    When the visitor asks "Tell me about Ember Cafe Gulshan"
    Then the AI assistant should respond with details about the 22-hour rooftop dining, steaks, Next.js 15, and the link "https://ember-cafe-gulshan.pages.dev"
```
