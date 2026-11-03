# Tasks: Multi-Device Responsive System

## Phase 1: Setup & Diagnostics
- [x] T001 Audit responsive breakpoints, fixed pixel containers, and horizontal scroll leakage across index.html, gallery.html, and contact.html
- [x] T002 Create automated multi-viewport verification script in tests/verify_responsive.py using headless Chrome

## Phase 2: Foundational Responsive Framework
- [x] T003 Enforce global CSS viewport safeguards (touch-action, -webkit-text-size-adjust, overflow-x-hidden, fluid font clamping) in index.html, gallery.html, contact.html

## Phase 3: User Story 1 (US1) - Mobile Optimization (< 640px)
- [x] T004 [US1] Refactor Hero section in index.html with flexible halo dimensions (w-[280px] to sm:w-[420px]), clamped typography, and stacked CTA buttons
- [x] T005 [US1] Enhance mobile navigation drawer in index.html, gallery.html, and contact.html with smooth animated transitions, 48px tap targets, and auto-close on selection
- [x] T006 [US1] Optimize technical stack marquee on index.html with overflow-x-hidden constraints and mobile padding to guarantee 0px horizontal spill
- [x] T007 [US1] Refactor video player modal in gallery.html with max-h-[90vh], responsive iframe height, and touch-optimized close buttons
- [x] T008 [US1] Restructure contact form and direct channels in contact.html for mobile single-column flow with 16px font inputs to eliminate iOS zoom

## Phase 4: User Story 2 (US2) - Tablet & Foldable Optimization (640px - 1023px)
- [x] T009 [P] [US2] Adjust tablet navbar padding and font size in index.html, gallery.html, contact.html to prevent logo-menu collision on 768px-850px screens
- [x] T010 [P] [US2] Balance 2-column project cards and direct channel cards grid in index.html and contact.html for tablet viewports

## Phase 5: User Story 3 (US3) - Laptop & Large Desktop (> 1024px)
- [x] T011 [P] [US3] Enforce max-w-7xl content constraints, full 4-column footer alignment, and smooth marquee looping across wide screens in index.html, gallery.html, contact.html

## Phase 6: Polish & Verification
- [x] T012 Run tests/verify_responsive.py across 360x640, 390x844, 768x1024, 1280x800, and 1920x1080 viewports and generate visual screenshot artifacts
- [x] T013 Commit and push responsive updates to origin main on GitHub
- [x] T014 Verify live deployments on GitHub Pages and Coolify

## Phase 7: Interactive Video Management Portal (Spec 015)
- [x] T015 [US4] Create initial video dataset `data/videos.json` seeding all 6 Facebook Reels, 4 LinkedIn Insights, and template schema
- [x] T016 [US4] Add REST API endpoints `GET /api/videos`, `POST /api/videos`, and `DELETE /api/videos/:id` with input validation in `server.js`
- [x] T017 [US4] Add "+ Add Video" action button to gallery header filter bar and individual section headers in `gallery.html`
- [x] T018 [US4] Build executive glassmorphic modal `#add-video-modal` with platform selection (Facebook, YouTube, LinkedIn), smart URL auto-detection, live preview, and form fields in `gallery.html`
- [x] T019 [US4] Implement hybrid client-side persistence and dynamic rendering engine (supports both Node.js backend and GitHub Pages `localStorage`) with real-time DOM card injection in `gallery.html`
- [x] T020 [US4] Implement dynamic YouTube video showcase grid in `#serial-youtube` and dynamic filter tab counters in `gallery.html`
- [x] T021 [US4] Create automated test suite in `tests/test_video_management.py` to verify API persistence, URL parsing, and modal UI
- [x] T022 [US4] Commit, push to `origin main`, sync Coolify container, and verify live on GitHub Pages

## Phase 8: Stealth Admin Portal & Curated Project Showcase (Spec 016)
- [x] T023 [US5] Implement secure Admin Auth API (`POST /api/admin/login`, `GET /api/admin/verify`, `POST /api/admin/logout`) in `server.js`, configure `ADMIN_MASTER_KEY` in `.env.example` and `.env`
- [x] T024 [US5] Sanitize public UI in `gallery.html`: Remove all public "+ Add Video to Gallery", "+ Add Reel", and public delete buttons so visitors see a clean, read-only executive media vault
- [x] T025 [US5] Implement stealth admin trigger in `gallery.html`: Add `Ctrl + Shift + A` keyboard shortcut, `/gallery?admin=1` route, and glassmorphic Master Passcode Modal
- [x] T026 [US5] Integrate protected Executive Media Management Portal in `gallery.html` that unlocks only after successful passcode verification to ingest Facebook Reels, YouTube videos, and LinkedIn insights
- [x] T027 [US6] Curate public & private enterprise projects in `data/projects.json` with "Enterprise Private Project • Client Confidential (NDA)" badges, live demo links, and tech architecture summaries
- [x] T028 [US6] Update `#works` flagship project section in `index.html` to dynamically render public and private enterprise showcase cards with executive styling
- [x] T029 [US5] Write automated test suite in `tests/test_stealth_admin.py` verifying stealth protection, authentication gates, and DOM sanitization
- [x] T030 Polish, commit to `origin main`, sync with Coolify container, and verify live status

## Phase 9: Cloudflare Pages Edge, "Emran AI" Ambassador & Telegram Notification Core (Spec 018)
- [x] T031 [US7] Configure native Cloudflare Pages edge architecture: create `_headers` (caching, security, CORS, CSP) and `_routes.json` in project root
- [x] T032 [US8] Update `.env.example` with `GEMINI_API_KEY`, `TELEGRAM_BOT_TOKEN`, and `TELEGRAM_CHAT_ID` placeholders
- [x] T033 [US8] Implement instant Telegram push notification dispatch in `server.js` (`POST /api/contact`) with async non-blocking webhook and persistent ledger logging (`data/inquiries.jsonl`)
- [x] T034 [P] [US8] Create Cloudflare Pages Function `functions/api/contact.js` mirroring the Telegram contact dispatch for serverless edge execution
- [x] T035 [US9] Author "Emran AI" Knowledge Base & System Prompt Matrix in `data/ai-knowledge.json` detailing Emran's verified bio, WebGL/AI Agent projects, skill stack, and contact channels
- [x] T036 [US9] Implement secure `POST /api/chat` endpoint in `server.js` with sliding-window rate limit (10 req/min/IP), input sanitization, Google Gemini 2.5 Flash API integration, and local semantic fallback matcher
- [x] T037 [P] [US9] Create Cloudflare Pages Function `functions/api/chat.js` for edge AI streaming and execution on Cloudflare Pages
- [x] T038 [US9] Build modern glassmorphic "Emran AI" floating assistant widget (`#emran-ai-widget`) across `index.html`, `gallery.html`, and `contact.html` with toggle trigger, message bubble history, typing indicators, quick prompt chips, and responsive drawer on mobile
- [x] T039 [US9] Write comprehensive automated test suite `tests/test_ai_and_telegram.py` verifying `/api/chat` rate-limiting, response formatting, prompt safety, and `/api/contact` Telegram dispatch
- [x] T040 Polish, verify locally on port 5225, sync to Coolify container (port 8088), commit to Git, and push to GitHub `main` for instant Cloudflare Pages edge deployment

## Phase 10: Discord Real-Time Webhook Alert Core & Zero-Breakage Assurance (Spec 020)
- [x] T041 [US10] Update `.env.example` with `DISCORD_WEBHOOK_URL` placeholder and documentation
- [x] T042 [US10] Implement `dispatchDiscordNotification(inquiry)` in `server.js` with non-blocking async execution, rich `#FF715B` embed card, and error isolation
- [x] T043 [US10] Update Cloudflare Pages Function `functions/api/contact.js` to support `context.env.DISCORD_WEBHOOK_URL` via `context.waitUntil()`
- [x] T044 [US10] Enhance automated test suite `tests/test_ai_and_telegram.py` to verify Discord payload generation, non-blocking resilience, and error suppression
- [x] T045 Polish, run test suite (100% pass), sync to Coolify container (port 8088), restart Node daemon (port 5225), and push to GitHub `main`

## Phase 11: Real Contact Channels, Discord Direct Hub & OpenGraph SEO Integration (Spec 021)
- [x] T046 [US11] Design and author crisp SVG favicon `favicon.svg` with monogram "EH" and coral gradient ring
- [x] T047 [US11] Inject OpenGraph, Twitter Cards, canonical links, and `favicon.svg` into `<head>` of `index.html`, `gallery.html`, `contact.html`, and `404.html`
- [x] T048 [US11] Update `contact.html` Direct Channels: replace placeholder WhatsApp with `+880 1706-754148` (`https://wa.me/8801706754148`), add Discord Server card (`https://discord.gg/VxDzexfEN`), and standardize email to `imrandt2001@gmail.com`
- [x] T049 [US11] Update footers across `index.html`, `gallery.html`, and `contact.html` with real WhatsApp `+880 1706-754148`, email `imrandt2001@gmail.com`, and Discord ecosystem link
- [x] T050 [US11] Synchronize `data/ai-knowledge.json` and `js/ai-widget.js` knowledge matrices with verified WhatsApp, Discord, and email details
- [x] T051 [US11] Update static mirror entrypoints (`gallery/index.html` and `contact/index.html`)
- [x] T052 [US11] Write automated test verifications in `tests/test_channels_and_seo.py`, run all test suites (100% pass), deploy to Cloudflare Pages (`emran-portfolio.pages.dev`), sync to Coolify container (port 8088), and push to GitHub `main`

## Phase 12: Stealth Admin Client Inquiry Inbox & Management Portal (Spec 022)
- [x] T053 [US12] Draft and finalize feature architecture in `specs/022-stealth-admin-inquiry-inbox.md`
- [x] T054 [US12] Implement `GET /api/admin/inquiries` and `DELETE /api/admin/inquiries/:id` in `server.js` with Bearer auth verification and atomic file updates
- [x] T055 [P] [US12] Create Cloudflare Pages serverless edge function `functions/api/admin/inquiries.js` for edge parity
- [x] T056 [US12] Build `#admin-inbox-modal` and "📬 Client Inquiries (N)" trigger in `#admin-control-bar` in `gallery.html` with real-time keyword search, mailto quick action, and delete confirmation
- [x] T057 [US12] Synchronize static mirrors (`gallery/index.html`) with inbox components
- [x] T058 [US12] Write automated test suite `tests/test_admin_inbox.py` verifying 401 unauthenticated rejection, 200 authenticated listing, inquiry deletion, and DOM sanitization
- [x] T059 [US12] Polish, run all 45+ automated test checks (100% pass), deploy to Cloudflare Pages (`emran-portfolio.pages.dev`), sync to Coolify container (port 8088), and push to GitHub `main`




