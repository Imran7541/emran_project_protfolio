# Spec 021: Real Contact Channels, Discord Direct Hub & OpenGraph SEO Integration

## 1. Executive Summary & Problem Formulation
- **Context**: 
  - The portfolio previously contained placeholder numbers (`+880 1900-000000`) for WhatsApp and lacked a direct community Discord link.
  - Social media share links (OpenGraph / Twitter Cards) and browser tab identity (`favicon.svg`) were missing, resulting in blank social cards and a generic browser globe icon.
- **Objectives**:
  1. **Real Communication Infrastructure**:
     - Connect verified WhatsApp: `+880 1706-754148` (`https://wa.me/8801706754148`).
     - Connect verified Discord Community Hub: `https://discord.gg/VxDzexfEN`.
     - Standardize primary client email: `imrandt2001@gmail.com`.
  2. **Brand Visual Identity & Favicon**:
     - Author crisp SVG favicon (`favicon.svg`) featuring Emran's signature obsidian dark badge, coral gradient ring (`#FF715B`), and bold typography monogram "EH".
  3. **Social Share Previews (OpenGraph & Twitter Card SEO)**:
     - Implement standard OpenGraph tags (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`) across `index.html`, `gallery.html`, and `contact.html`.
     - Set canonical URLs pointing to production `https://emran-portfolio.pages.dev`.
  4. **Knowledge Matrix Synchronicity**:
     - Update `data/ai-knowledge.json` and `js/ai-widget.js` so "Emran AI" accurately provides Emran's verified WhatsApp, Discord server, and email when asked.

---

## 2. Verified Data Matrix

| Attribute | Verified Value | Target Placement |
| :--- | :--- | :--- |
| **WhatsApp Number** | `+880 1706-754148` | `contact.html`, Footers (`index.html`, `gallery.html`, `contact.html`) |
| **WhatsApp Direct URL** | `https://wa.me/8801706754148` | Direct WhatsApp Buttons & Action Links |
| **Discord Server** | `https://discord.gg/VxDzexfEN` | Direct Channel Card in `contact.html`, Social ecosystem footers |
| **Primary Email** | `imrandt2001@gmail.com` | Primary Email Card, Form mailto links, Footers |
| **Production Domain** | `https://emran-portfolio.pages.dev` | Canonical `<link>`, OpenGraph `og:url`, Twitter Card |
| **Share Card Preview** | `https://emran-portfolio.pages.dev/emran_suit.jpg` | OpenGraph `og:image`, Twitter `twitter:image` |
| **Favicon Path** | `favicon.svg` | `<link rel="icon" type="image/svg+xml" href="favicon.svg">` |

---

## 3. Behavioral Scenarios (Gherkin BDD)

```gherkin
Feature: Real Contact Channels & OpenGraph Social Sharing

  Scenario: Visitor clicks WhatsApp Business button
    Given a visitor lands on "contact.html" or scrolls to footer
    When the visitor clicks "Start WhatsApp Chat"
    Then the link must target "https://wa.me/8801706754148"
    And open WhatsApp directly with Emran's real phone number

  Scenario: Visitor accesses Discord Community
    Given a visitor inspects the Direct Channels on "contact.html"
    When the visitor clicks "Join Discord Server"
    Then the browser must navigate to "https://discord.gg/VxDzexfEN" in a new tab

  Scenario: URL shared on Discord, Facebook, or LinkedIn
    Given a recruiter shares "https://emran-portfolio.pages.dev" in a chat or post
    When the social crawler scrapes the metadata
    Then it must extract the title "Emran Hosen — Senior Full-Stack AI Engineer & Autonomous Agent Architect"
    And render the executive portrait image "emran_suit.jpg" as a large summary preview card
```
