# Specification: GitHub Pages Live Deployment (`emran_project_protfolio`)

```yaml
feature_id: "012-github-pages-live-deployment"
feature_name: "GitHub Pages Live Deployment and Hosting"
status: "completed"
owner: "Emran Hosen"
last_updated: "2026-10-31"
repository: "Imran7541/emran_project_protfolio"
live_urls:
  home: "https://imran7541.github.io/emran_project_protfolio/"
  gallery: "https://imran7541.github.io/emran_project_protfolio/gallery.html"
tech_stack:
  hosting: "GitHub Pages"
  source: "branch: main, path: /"
  enforce_https: true
```

---

## 1. User Intent & Problem Definition
The user requested:
*"vai ekhon amer ei site take github a live dekhano jai seta kivabe ami janina tmi github live kore dekho"*
(Translation: "Brother, now how can my site be shown live on GitHub? I don't know how to do that, you make it live on GitHub and show me.")

The user wants the portfolio and video gallery accessible live to the public on the web via GitHub's free hosting feature (GitHub Pages), without having to run a local server.

---

## 2. Technical Architecture & Constraints
1. **GitHub Pages Configuration**:
   - Repository: `Imran7541/emran_project_protfolio`
   - Source branch: `main`
   - Directory: `/` (repository root)
   - Domain: `https://imran7541.github.io/emran_project_protfolio/`
2. **Path Verification**:
   - All internal links in `index.html` and `gallery.html` must remain relative (`gallery.html`, `index.html`, `assets/thumbnails/...`) to function properly under the `/emran_project_protfolio/` sub-path.
3. **Graceful API Fallbacks**:
   - Backend APIs (`/api/health`, `/api/agent/status`) in `index.html` already include graceful `.catch(() => null)` fallbacks and default values (`PORT 5225 ONLINE`, `248 Skills Active`) so static GitHub Pages hosts seamlessly.

---

## 3. Tasks Breakdown (`speckit-tasks`)

### Phase 1: Pre-Deployment Path & Asset Audit
- [x] T001 Verify no absolute leading slash paths exist in `index.html` or `gallery.html`
- [x] T002 Verify graceful fallbacks for backend API calls when statically hosted

### Phase 2: GitHub Pages Activation
- [x] T003 Enable GitHub Pages on repository via GitHub API (`POST /repos/Imran7541/emran_project_protfolio/pages`)
- [x] T004 Monitor GitHub Pages build pipeline until status transitions to `built`

### Phase 3: Live Verification & Proof
- [x] T005 Test live HTTP response on `https://imran7541.github.io/emran_project_protfolio/` (HTTP 200)
- [x] T006 Test live HTTP response on `https://imran7541.github.io/emran_project_protfolio/gallery.html` (HTTP 200)
- [x] T007 Configure GitHub repository Homepage URL in About section
- [x] T008 Update `notes/PROJECT_STATE.md` and `notes/AGENT_HANDOVER.md`
