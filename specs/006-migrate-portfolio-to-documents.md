---
feature_id: "006-migrate-portfolio-to-documents"
title: "Consolidate and Migrate Full-Stack Portfolio to Documents/emran_project_protfolio"
status: "completed"
created_at: "2026-10-31"
priority: "P1"
author: "Antigravity Engineering"
---

# Feature Specification: Portfolio Migration to Documents/emran_project_protfolio

## 1. Overview & Objective
Move and consolidate the entire cinematic portfolio codebase, media assets, full-stack Node.js server, telemetry databases, and SDD documentation from the temporary download path (`/home/emran/Downloads/emran_cinematic_portfolio`) to the permanent user workspace directory at `/home/emran/Documents/emran_project_protfolio`. Maintain 100% data integrity, apply the mandatory Antigravity project architecture, and ensure the live server runs seamlessly on port 5225 from the new location.

---

## 2. User Stories & Acceptance Criteria

### User Story 1 (P1): Full Data & Asset Migration to Documents
- **Given** all portfolio files and assets exist in `/home/emran/Downloads/emran_cinematic_portfolio/`
- **When** copied recursively to `/home/emran/Documents/emran_project_protfolio/`
- **Then** all files (`index.html`, `gallery.html`, `server.js`, `package.json`, `emran_cutout.png`, `emran_portrait.jpg`, `emran_suit.jpg`, `emran_suit_cutout.png`, and `data/` directory) exist with identical checksums and permissions.

### User Story 2 (P1): Standard Antigravity Architecture & Zero-Trust Scaffold
- **Given** the destination directory `/home/emran/Documents/emran_project_protfolio/`
- **When** initialized with the mandatory Antigravity standard
- **Then** `.env.example`, `.gitignore`, `docs/ARCHITECTURE.md`, `specs/`, `notes/PROJECT_STATE.md`, `notes/AGENT_HANDOVER.md`, `config/policies.yaml`, and `README.md` are established and populated.

### User Story 3 (P1): Server Execution & REST API Verification from Target Directory
- **Given** `/home/emran/Documents/emran_project_protfolio/server.js`
- **When** launched as a persistent service on port 5225
- **Then** all endpoints (`/index.html`, `/gallery.html`, `/api/health`, `/api/projects`, `/api/agent/status`, `/api/contact`) return HTTP 200 OK.

### User Story 4 (P2): Visual Headless CDP Verification
- **Given** the newly hosted portfolio at `http://localhost:5225`
- **When** inspected via headless Chrome CDP
- **Then** screenshots verify that high-resolution portraits, Three.js abyss canvas, and telemetry render without missing asset (404) errors.
