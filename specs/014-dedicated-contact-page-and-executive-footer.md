# Spec 014: Dedicated Contact Page and Executive Footer Redesign

## 1. Overview
Resolve user feedback regarding visual balance and clutter:
1. Move the project inquiry form off the homepage (`index.html`) to its dedicated, full-featured **`contact.html`** page.
2. Replace the primitive 1-line footer with a rich, multi-column **Executive Footer** featuring brand identity, status badge, structured navigation, technical domains, direct contact details, authentic SVG social icons, and smooth back-to-top navigation.

---

## 2. Architectural Design & Components

### 2.1 Dedicated `contact.html` Page
- **URL**: `/contact` and `/contact.html` (Local port 5225, Coolify port 8088/sslip.io, and GitHub Pages).
- **Aesthetic**: Unified Three.js WebGL Abyss background with ambient drifting particles and film grain overlay.
- **Left Column**: Direct Communication Channels (Primary Email with 1-click copy toast, WhatsApp Business direct chat, Telegram message link, and live Dhaka GMT+6 clock).
- **Right Column**: Interactive Project Inquiry Form connected to Node.js backend REST API `POST /api/contact`, with real-time field validation, encrypted transmission badge, and status acknowledgment.

### 2.2 Cleaned-up Homepage (`index.html`)
- Removed the bulky input form box from the homepage.
- Replaced with a sleek, balanced Call-to-Action banner ("Have a vision or project? Let's build it together.") linking directly to `contact.html` and providing quick direct email/WhatsApp/Telegram buttons.
- Updated desktop navigation and mobile drawer: `Contact` points to `contact.html`.

### 2.3 World-Class Executive Footer (Omnipresent across `index.html`, `gallery.html`, and `contact.html`)
- **Header Row**: Prominent "Emran Hosen." brand logo, professional positioning bio, live pulsing green availability pill ("Available for Global Contracts & Roles"), and "Get In Touch" button.
- **4-Column Grid**:
  - *Col 1 (Navigation)*: Home Overview, About & Bio, Flagship Projects, Media Gallery, Contact & Inquiries.
  - *Col 2 (Core Expertise)*: Autonomous AI Agents, Full-Stack SaaS (Next/Node), WebGL & Three.js 3D Web, Cross-Platform Mobile (Flutter), Cloud & Docker.
  - *Col 3 (Direct Contact)*: `imrandt2001@gmail.com`, WhatsApp, Telegram, Location (Dhaka, Bangladesh · GMT+6).
  - *Col 4 (Social Ecosystem)*: Authentic vector SVG icons for GitHub, LinkedIn, Facebook, and Email.
- **Bottom Sub-Footer**: Copyright statement, Zero-Trust Precision standard watermark, tech stack badge, and smooth "Back to Top" button.

---

## 3. BDD Scenarios

### Scenario: Dedicated Contact Navigation
- **Given** a user is on any page (`index.html`, `gallery.html`, or `contact.html`)
- **When** the user clicks the "Contact" link in the navbar
- **Then** the browser navigates to `contact.html` with the inquiry portal active

### Scenario: Clean Homepage Experience
- **Given** a visitor navigates down the homepage (`index.html`)
- **When** the visitor scrolls past the technology stack marquee
- **Then** no bulky form input fields or textareas are rendered on the homepage; instead, a refined CTA banner and executive footer are displayed

### Scenario: Inquiry Transmission
- **Given** a client is on `contact.html`
- **When** valid contact details and project scope are submitted
- **Then** the payload is posted to `/api/contact`, appended to `data/inquiries.jsonl`, and an inquiry reference ID is displayed
