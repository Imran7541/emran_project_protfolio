---
feature_id: "005-portfolio-backend-and-works"
title: "Full-Stack Node.js Application Server, Live Works Telemetry & Hash Loading Fix for Emran Hosen Portfolio"
status: "completed"
created_at: "2026-10-31"
priority: "P1"
author: "Antigravity Engineering"
---

# Feature Specification: Portfolio Backend & #works Live Telemetry

## 1. Overview & Objective
Replace the primitive, single-threaded Python static server (`python3 -m http.server 5225`) with a production-grade Node.js Express application server serving the portfolio at `http://localhost:5225`. Implement high-performance REST API endpoints (`/api/health`, `/api/projects`, `/api/agent/status`, `/api/contact`), dynamic telemetry integration in the `#works` flagship projects section, and an interactive contact inquiry form in `#contact`. Additionally, resolve URL hash jumping behavior on `#works` so the site always starts and reloads smoothly from the top Hero section, and prevent navbar clipping on in-page navigation via `scroll-mt-24`.

---

## 2. Gherkin Scenarios & Acceptance Criteria

### Scenario 1: Express Application Server Replaces Python on Port 5225
- **Given** Python `http.server` is currently bound to port 5225
- **When** the Python process is terminated and the Node.js Express server is started on port 5225
- **Then** `curl --noproxy '*' -I http://localhost:5225/index.html` and `gallery.html` must return `HTTP/1.1 200 OK` with proper MIME types.

### Scenario 2: Dynamic Project Feed API (`/api/projects`)
- **Given** the 4 flagship projects (AI-Agents-Hub, Next Label 3D, Autonomous Video Producer, Enterprise Student Platform)
- **When** a client requests `GET /api/projects`
- **Then** the server must return HTTP 200 with JSON array containing `id`, `slug`, `title`, `category`, `tags`, `repoUrl`, `status`, and `highlights`.

### Scenario 3: Real-Time Agent Telemetry API (`/api/agent/status`)
- **Given** the local AI-Agents-Hub at `/home/emran/Documents/AI-Agents-Hub` with 248 loaded skills
- **When** a client requests `GET /api/agent/status`
- **Then** the server returns HTTP 200 with `{ status: "online", skills_loaded: 248, model: "nvidia/nemotron-3.5-super-vl-120b-a12b", gateway: "Render/Railway" }`.

### Scenario 4: Validated Contact Form Submission (`/api/contact`)
- **Given** valid JSON payload `{ name: "John Doe", email: "john@example.com", service: "AI Automation", message: "Inquiring about multi-agent systems." }`
- **When** submitted via `POST /api/contact`
- **Then** the server validates the input, safely appends it to `data/inquiries.jsonl`, and returns `HTTP 200` with `{ ok: true, message: "..." }`.

### Scenario 5: Frontend Dynamic Integration in `#works` & `#contact`
- **Given** the user navigates to `http://localhost:5225/index.html`
- **When** the page loads
- **Then** the live telemetry bar displays real-time agent/server health, and `#contact` features a functional inquiry form submitting to `/api/contact`.

### Scenario 6: Smooth Top Load & Section Scroll-Margin Spacing
- **Given** a visitor navigates directly to `http://localhost:5225/index.html#works` or reloads the browser
- **When** the page renders
- **Then** `history.scrollRestoration` is manual, `window.scrollY` initializes strictly at 0 (Hero view "Hello. Im Emran"), the URL hash is cleaned via `history.replaceState`, and clicking navbar anchor links smoothly glides to target sections (`#works`, `#about`, `#stack`, `#contact`) with `scroll-mt-24` clearance under the fixed 80px navbar without clipping.
