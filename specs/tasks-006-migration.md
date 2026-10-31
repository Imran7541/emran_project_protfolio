# Tasks: Migrate Portfolio to Documents/emran_project_protfolio

**Feature**: `006-migrate-portfolio-to-documents`
**Target Path**: `/home/emran/Documents/emran_project_protfolio`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Target environment initialization and verification

- [ ] T001 Verify source directory files in `/home/emran/Downloads/emran_cinematic_portfolio`
- [ ] T002 [P] Verify destination directory exists at `/home/emran/Documents/emran_project_protfolio`
- [ ] T003 [P] Kill any stale processes bound to port 5225

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Prerequisites before migration execution

- [ ] T004 Check disk space and permissions on `/home/emran/Documents/emran_project_protfolio`
- [ ] T005 [P] Create subdirectories in `/home/emran/Documents/emran_project_protfolio`: `data`, `specs`, `docs`, `notes`, `config`

---

## Phase 3: User Story 1 - Full Data & Asset Migration (Priority: P1) 🎯 MVP

**Goal**: Transfer 100% of the portfolio codebase, assets, and data files into `/home/emran/Documents/emran_project_protfolio`.

**Independent Test**: Verify file listings and sha256 checksums match between source and destination.

### Implementation for User Story 1
- [ ] T006 [P] [US1] Copy core HTML pages `index.html` and `gallery.html` to `/home/emran/Documents/emran_project_protfolio/`
- [ ] T007 [P] [US1] Copy media assets `emran_cutout.png`, `emran_portrait.jpg`, `emran_suit.jpg`, `emran_suit_cutout.png` to `/home/emran/Documents/emran_project_protfolio/`
- [ ] T008 [P] [US1] Copy backend files `server.js` and `package.json` to `/home/emran/Documents/emran_project_protfolio/`
- [ ] T009 [P] [US1] Copy database directory `data/` (`projects.json` and `inquiries.jsonl`) to `/home/emran/Documents/emran_project_protfolio/data/`
- [ ] T010 [US1] Verify checksums and file counts between source and destination

**Checkpoint**: At this point, all data is safely and completely mirrored in `Documents/emran_project_protfolio`.

---

## Phase 4: User Story 2 - Standard Antigravity Architecture & Zero-Trust Scaffold (Priority: P1)

**Goal**: Establish standard project structure, `.env.example`, `.gitignore`, `docs/ARCHITECTURE.md`, `specs/`, `notes/`, and `README.md`.

**Independent Test**: Directory matches mandatory Antigravity Architecture standard.

### Implementation for User Story 2
- [ ] T011 [P] [US2] Create `.gitignore` and `.env.example` in `/home/emran/Documents/emran_project_protfolio/`
- [ ] T012 [P] [US2] Create system architecture blueprint in `/home/emran/Documents/emran_project_protfolio/docs/ARCHITECTURE.md`
- [ ] T013 [P] [US2] Create live tracking in `/home/emran/Documents/emran_project_protfolio/notes/PROJECT_STATE.md`
- [ ] T014 [P] [US2] Create session directive in `/home/emran/Documents/emran_project_protfolio/notes/AGENT_HANDOVER.md`
- [ ] T015 [P] [US2] Copy all feature specifications into `/home/emran/Documents/emran_project_protfolio/specs/`
- [ ] T016 [P] [US2] Create comprehensive documentation in `/home/emran/Documents/emran_project_protfolio/README.md`

**Checkpoint**: The repository is fully structured, documented, and reproducible.

---

## Phase 5: User Story 3 - Server Execution & REST API Verification (Priority: P1)

**Goal**: Run the Node.js application server from the new Documents directory and verify all endpoints.

**Independent Test**: Curl requests to all endpoints return HTTP 200 OK.

### Implementation for User Story 3
- [ ] T017 [US3] Launch Node.js server via daemon process from `/home/emran/Documents/emran_project_protfolio/server.js` on port 5225
- [ ] T018 [P] [US3] Verify `GET /index.html` and `GET /gallery.html` return HTTP 200
- [ ] T019 [P] [US3] Verify `GET /api/health` returns HTTP 200 with system metrics
- [ ] T020 [P] [US3] Verify `GET /api/projects` returns HTTP 200 with 4 flagship projects
- [ ] T021 [P] [US3] Verify `GET /api/agent/status` returns HTTP 200 with active skills telemetry
- [ ] T022 [US3] Verify `POST /api/contact` logs successfully to `/home/emran/Documents/emran_project_protfolio/data/inquiries.jsonl`

**Checkpoint**: Full-stack application runs completely from the new Documents location.

---

## Phase 6: User Story 4 - Visual Headless CDP Verification (Priority: P2)

**Goal**: Verify visual rendering and asset resolution using headless Chrome.

**Independent Test**: Screenshots show 100% loaded images, styling, and WebGL canvas.

### Implementation for User Story 4
- [ ] T023 [US4] Execute headless Chrome screenshot test for `http://localhost:5225/index.html`
- [ ] T024 [US4] Execute headless Chrome screenshot test for `http://localhost:5225/gallery.html`
- [ ] T025 [US4] Confirm zero console errors or broken media paths

---

## Final Phase: Polish & Cross-Cutting Concerns

- [ ] T026 Update `notes/PROJECT_STATE.md` and `notes/AGENT_HANDOVER.md` in both workspaces
- [ ] T027 Generate completion report for user in clear Bengali
