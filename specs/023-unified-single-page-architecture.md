# Spec 023: Unified Single-Page Architecture & Gallery Consolidation

## 1. Feature Overview & Rationale
This specification details the architectural transition of the **Emran Hosen Portfolio** from a multi-page setup with a separate external `gallery` page into a cohesive, high-conversion **Unified Single-Page Portfolio Experience**.

### 1.1 Developer & UX Rationale
1. **Recruiter & Client Attention Span (Under 60s)**:
   Visitors and prospective clients evaluate software developer portfolios in 30 to 60 seconds. A single continuous storytelling scroll (`Hero` -> `Live Metrics Strip` -> `Selected Flagship Projects` -> `Technology Stack Marquee` -> `Core Services` -> `Verified Direct Contact Channels`) maximizes engagement and significantly lowers bounce rates compared to forcing navigation across disparate pages.
2. **Elimination of Content Redundancy**:
   Direct links to Emran's verified channels (Facebook, LinkedIn, GitHub, Discord Community) are already prominently embedded in the header, footer, contact section, and AI chatbot. Visitors wanting to watch reels or read technical articles can directly visit Emran's actual social profiles, where they can organically engage, comment, and follow.
3. **Streamlined Navigation**:
   Removing `Gallery` removes cognitive friction from the primary navigation bar. The main navigation becomes crisp and focused: `Home`, `About`, `Project`, and `Contact`.
4. **Non-Destructive Preservation**:
   The physical file `gallery.html` and its media data `data/videos.json` remain preserved in the codebase as an archive. Any direct inbound links or bookmarks to `/gallery` will cleanly route to the home page or remain functional without broken links.

```yaml
feature_metadata:
  spec_id: "023"
  title: "Unified Single-Page Architecture & Gallery Consolidation"
  author: "Emran Hosen"
  status: "Draft"
  architecture_pattern: "Single-Page Continuous Narrative (SPA/Scroll-Linked)"
  target_ui_surfaces:
    - "index.html (Desktop Nav, Mobile Drawer, Footer)"
    - "contact.html (Desktop Nav, Mobile Drawer, Footer)"
  target_routing_surfaces:
    - "server.js"
    - "_routes.json"
    - "functions/"
  test_suites:
    - "tests/test_single_page_navigation.py"
    - "tests/test_channels_and_seo.py"
```

---

## 2. Gherkin BDD Scenarios

```gherkin
Feature: Unified Single-Page Portfolio Navigation
  As a recruiter, enterprise client, or site visitor
  I want a streamlined single-page navigation without an unnecessary separate gallery link
  So that I can explore Emran's complete background, metrics, projects, and contact info in one continuous flow

  Scenario: Visitor explores desktop navigation on homepage
    Given the visitor opens "https://emrandev.pages.dev/"
    When the visitor examines the top fixed navigation bar
    Then the navigation links MUST include "Home", "About", "Project", and "Contact"
    And the "Gallery" navigation link MUST NOT be present in the main menu
    And clicking "Home", "About", or "Project" smoothly scrolls to the corresponding in-page section

  Scenario: Mobile visitor opens drawer menu
    Given the visitor opens the portfolio on a mobile device (viewport width <= 768px)
    When the visitor taps the hamburger toggle button
    Then the mobile drawer displays "Home", "About", "Project", and "Contact"
    And the "Gallery" item MUST NOT appear in the drawer menu

  Scenario: Visitor examines the executive footer
    Given the visitor scrolls to the footer of "index.html"
    When the visitor reviews the "Quick Links" column
    Then the links MUST navigate to in-page anchors ("#hero", "#about", "#works", "contact")
    And direct social channels (Facebook, LinkedIn, GitHub, Discord) are prominently displayed for external content consumption

  Scenario: Direct URL access to legacy /gallery route
    Given a visitor enters "https://emrandev.pages.dev/gallery" directly from an old link or bookmark
    When the request is processed by the edge router
    Then the server handles the request gracefully without HTTP 404 or Fastly CDN rate limits
```

---

## 3. Implementation Plan & Execution Tasks

### Task 1: Navigation Bar Harmonization (`index.html`)
- Remove `<a href="gallery"...>Gallery</a>` from desktop navbar (`nav .hidden.md:flex`).
- Remove `<a href="gallery"...>Gallery</a>` from mobile drawer (`#mobile-drawer`).
- Standardize active links to:
  - `Home` (`#`)
  - `About` (`#about`)
  - `Project` (`#works`)
  - `Contact` (`contact` or `#contact`)

### Task 2: Executive Footer Harmonization (`index.html` & `contact.html`)
- In `index.html` and `contact.html` footer "Navigation / Quick Links" column:
  - Replace the separate "Media Gallery" link with "Direct Inquiries" or "Selected Works".
  - Ensure social channels (Facebook, LinkedIn, GitHub, Discord) remain clear and prominent.

### Task 3: Edge Routing & Backward Compatibility
- In `server.js` and Cloudflare Pages:
  - Ensure `/gallery` continues to resolve without 404s (serving archive or smoothly redirecting to `/`).

### Task 4: Automated Testing & Verification
- Create automated test `tests/test_single_page_navigation.py` to assert that:
  - `Gallery` is strictly absent from the main desktop and mobile navigation on `index.html`.
  - In-page anchors (`#`, `#about`, `#works`) exist and resolve properly.
  - All existing SEO and channels tests pass 100%.

### Task 5: Live Production Deployment & Sync
- Push to GitHub `origin main`.
- Deploy to Cloudflare Pages (`emrandev` and `emran-portfolio`).
- Sync to Coolify Docker container (port 8088).
