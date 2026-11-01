# Spec 016: Stealth Admin Portal, Protected Media Ingestion & Curated Project Showcase

## 1. Executive Summary & Problem Statement
The Emran Hosen portfolio currently exposes public "+ Add Video to Gallery" and "+ Add Reel" triggers to ordinary visitors, undermining professional credibility. Furthermore, private GitHub repositories cannot be browsed by clients without structured presentation. 

This specification establishes:
1. **Stealth Executive Admin Portal**: Completely concealed from public visitors. Accessible exclusively via secure hotkey (`Ctrl + Shift + A`) or protected route (`/admin`), guarded by a Master Passcode / JWT session.
2. **Read-Only Public Gallery**: Seamless, high-performance showcase with zero edit controls visible to ordinary clients or recruiters.
3. **Dual Project Architecture (Public + Private GitHub Repositories)**: Presentation of open-source GitHub projects combined with curated Enterprise Case Studies representing private repositories (with client NDA badges, architecture diagrams, live demo URLs, and metric impacts).
4. **Coolify Container & Worldwide Ingress Architecture**: Production hosting using containerized Node.js runtime on Coolify with Traefik ingress and automated Cloudflare Tunnel routing.

---

## 2. Technical Architecture & Component Specification

```yaml
system_architecture:
  runtime: "Node.js 20+ Express Full-Stack Server"
  container_orchestration: "Coolify v4.5.3 (Container UUID: 3lolil9okyxy5wz6ophjozt1)"
  ingress_routing: "Traefik v3.7 / Cloudflare Zero-Trust Tunnel"
  auth_model: "Zero-Trust Session Token with SHA-256 Master Key"
  persistence: "data/videos.json & data/projects.json (JSON-backed REST Data Store)"

components:
  admin_portal:
    activation_triggers:
      - "Hotkey: Ctrl + Shift + A"
      - "Direct Route: /admin or /gallery?mode=admin"
      - "Console Directive: window.__emranAdminOpen()"
    security_gate:
      - "Master Passcode validation against process.env.ADMIN_MASTER_KEY"
      - "HTTP-only cookie or secure Bearer Token (Expires in 24h)"
      - "Rate limiting on failed attempts (Max 5 attempts / 15 mins)"
    capabilities:
      - "Ingest Facebook Reel (9:16 vertical player embed)"
      - "Ingest YouTube Video (16:9 widescreen player or 9:16 Shorts)"
      - "Ingest LinkedIn Post/Insight (embedded iframe)"
      - "Delete / Retire obsolete media items with confirmation"
      - "Reorder / Feature priority spotlight items"

  project_showcase:
    public_projects:
      - "Live metadata synced from GitHub API: Imran7541 (stars, forks, languages)"
    private_enterprise_projects:
      - "Curated Case Study Cards (e.g. Autonomous AI Multi-Agent Engine, Fintech Gateway)"
      - "Badges: 'Enterprise Private Repository' · 'Client Confidential'"
      - "Interactive Preview: Tech Architecture, Live Demo Link, Key Deliverables"
```

---

## 3. Gherkin BDD Scenarios

```gherkin
Feature: Stealth Admin Management & Secure Video Ingestion

  Scenario: Ordinary Visitor Browsing Gallery
    Given an unauthenticated visitor visits "/gallery"
    Then the "+ Add Video to Gallery" button is NOT rendered in the DOM
    And no "+ Add Reel" or "+ Add Post" action buttons are visible
    And no delete buttons appear on any video cards
    And the page displays an executive, cinematic media vault

  Scenario: Admin Access via Hotkey
    Given Emran is on any portfolio page
    When Emran presses "Ctrl + Shift + A"
    Then a glassmorphic "Executive Admin Passcode" modal appears
    When Emran enters the correct Master Passcode
    Then an authenticated session token is stored
    And the Executive Media Management Suite opens
    And Emran can ingest Facebook, YouTube, or LinkedIn videos with instant persistence

  Scenario: Private GitHub Projects Presentation
    Given a visitor browses the "#works" project section on the homepage
    Then open-source repositories display live GitHub stars and links
    And private client projects display curated architecture overviews, live demo links, and "Enterprise NDA" badges
    And no broken 404 links occur when clicking private project cards

  Scenario: Coolify Live Container Verification
    Given the Coolify container "3lolil9okyxy5wz6ophjozt1" is running on port 5225:8088
    When an HTTP request is made to "/api/health"
    Then the response status is 200 with "status: healthy"
    And all REST APIs (/api/videos, /api/projects, /api/admin/verify) respond with sub-50ms latency
```

---

## 4. Implementation Steps & Milestones

1. **Phase 1: Admin Gate Engine (`server.js` & `middleware/auth.js`)**:
   - Implement `POST /api/admin/auth` verifying passcode against `.env` `ADMIN_MASTER_KEY`.
   - Protect `POST /api/videos` and `DELETE /api/videos/:id` requiring Bearer token.
2. **Phase 2: UI Sanitization & Stealth Modal (`gallery.html`)**:
   - Remove public "+ Add Video" and "+ Add Reel" buttons from default view.
   - Implement `Ctrl + Shift + A` listener and `/admin` trigger.
   - Render clean, high-density Admin Management Drawer when authenticated.
3. **Phase 3: Curated Project Showcase (`index.html` & `data/projects.json`)**:
   - Enrich `data/projects.json` with both public GitHub repos and private enterprise systems.
   - Render private projects with executive badges, live demo links, and architecture highlights.
4. **Phase 4: Coolify & Worldwide Public Routing**:
   - Verify Coolify container build and Traefik router rules.
   - Configure Cloudflare Tunnel / public ingress for worldwide access without CGNAT limits.
