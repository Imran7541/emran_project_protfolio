# Emran Hosen — Cinematic Portfolio & Autonomous AI Hub

> Official portfolio of **Emran Hosen** — Software Developer & Autonomous AI Systems Engineer.

---

## 🌟 Highlights & Features
- **Cinematic Visuals**: Dark deep-sea abyss theme (`#121E27` background, Coral `#FF715B` accents) with procedural Three.js caustics shaders, drifting bubbles, and ambient dust particles.
- **Dedicated Media Gallery (`gallery.html`)**:
  - **Serial 1 (Facebook Reels)**: 2x2 luxury horizontal cards with 9:16 vertical Reel embeds, episode badges, and hashtag pills.
  - **Serial 2 (LinkedIn Case Studies)**: 3-column responsive grid with interactive LinkedIn posts and tags.
  - **Serial 3 (YouTube Masterclasses)**: Upcoming long-form video courses and architectural deep dives.
  - **Filter Tabs**: Instant category switching (All, Facebook, LinkedIn, YouTube).
- **Modern Technical Stack**: 14 authentic brand vector SVG badges with hover glow effects.
- **Full-Stack Node.js Application Server**:
  - `GET /api/health` -> System health and uptime metrics.
  - `GET /api/projects` -> Dynamic JSON feed of 4 flagship projects.
  - `GET /api/agent/status` -> Live telemetry scanning AI-Agents-Hub (248 skills active).
  - `POST /api/contact` -> Input validation and append-only inquiry logging in `data/inquiries.jsonl`.
- **Rock-Solid Scroll Architecture**:
  - `history.scrollRestoration = 'manual'` prevents awkward browser jumps to URL hashes on load or refresh.
  - In-page navigation with `scroll-mt-24` ensures 16px clearance beneath the 80px fixed glass navbar.

---

## 🚀 Quick Start

### 1. Run the Application Server
```bash
node server.js
```
The server will start on port `5225` (configurable via `PORT` environment variable).

### 2. Access in Browser
- **Home Portfolio**: [http://localhost:5225/index.html](http://localhost:5225/index.html)
- **Video & Media Gallery**: [http://localhost:5225/gallery.html](http://localhost:5225/gallery.html)
- **System Health API**: [http://localhost:5225/api/health](http://localhost:5225/api/health)
- **Flagship Projects API**: [http://localhost:5225/api/projects](http://localhost:5225/api/projects)
- **Autonomous Agent Telemetry**: [http://localhost:5225/api/agent/status](http://localhost:5225/api/agent/status)

---

## 📁 Directory Structure
```text
emran_project_protfolio/
├── .env.example              # Environment variables template
├── .env                      # Real environment configuration
├── .gitignore                # Git ignore rules
├── index.html                # Main cinematic portfolio
├── gallery.html              # Dedicated media gallery
├── server.js                 # Zero-dependency Node.js HTTP server & REST API
├── package.json              # Node.js project definition
├── tasks.md                  # SDD Task checklist
├── README.md                 # Project documentation
│
├── data/                     # Persistent application data
│   ├── projects.json         # Flagship projects metadata
│   └── inquiries.jsonl       # Append-only contact inquiry log
│
├── docs/                     # Architectural documentation
│   └── ARCHITECTURE.md       # System design & Mermaid diagrams
│
├── notes/                    # Live state tracking & agent handover
│   ├── PROJECT_STATE.md      # Completed & pending task registry
│   └── AGENT_HANDOVER.md     # 1-paragraph session resume directive
│
├── config/                   # Policies & security guardrails
│   └── policies.yaml         # Structural & rate-limiting policies
│
└── specs/                    # Feature specifications (SDD)
    ├── 003-cinematic-gallery-page.md
    ├── 004-tech-stack-redesign.md
    ├── 005-portfolio-backend-and-works.md
    └── 006-migrate-portfolio-to-documents.md
```

---

## 👤 Developer
**Emran Hosen**
- **GitHub**: [github.com/Imran7541](https://github.com/Imran7541)
- **LinkedIn**: [linkedin.com/in/imran-fullstack/](https://www.linkedin.com/in/imran-fullstack/)
- **Email**: `imrandt2001@gmail.com`
