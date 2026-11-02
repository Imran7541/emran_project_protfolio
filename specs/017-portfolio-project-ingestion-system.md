# Spec 017: Portfolio Project Ingestion & Showcase System

## 1. Context & Objectives
- **User Requirement**: The user wants to showcase public GitHub projects (specifically `Next_Label_protfolio` and future repositories) on their portfolio (`index.html`), and wants to know the best architectural workflow to add and manage projects effortlessly.
- **Current State**:
  - `data/projects.json` contains 6 curated projects (3 OSS, 3 Private).
  - `Next_Label_protfolio` is already listed as Project 2 with repository link `https://github.com/Imran7541/Next_Label_protfolio`, but its live deployment (`https://next-label-portfolio.vercel.app`) is not yet linked.
  - Another active public project `digitools-projects` (`https://symphonious-crisp-3617dc.netlify.app`) exists on GitHub.
  - The project cards in `index.html` are statically rendered HTML, requiring manual HTML edits for future additions.

---

## 2. Best Architectural Approaches (Comparison Matrix)

| Strategy | Effort to Add | Scalability | Offline / Static Support | User Experience |
| :--- | :--- | :--- | :--- | :--- |
| **A. Static HTML Hardcoding** | High (Write 40+ lines of HTML per project) | Poor (Risk of breaking layout / unclosed tags) | High | Static only |
| **B. JSON-Driven Dynamic Hydration** *(Recommended Baseline)* | Very Low (Add 1 JSON object to `data/projects.json`) | Excellent (Clean separation of data & UI) | High (Supports local JSON bundle + `/api/projects`) | Consistent card design & auto-filtering |
| **C. Stealth Admin Project Ingestion** | Zero Coding (Fill web form in `Ctrl+Shift+A` modal) | High (Integrated with `server.js` REST API) | High (Dual backend + localStorage fallback) | Executive dashboard experience |
| **D. GitHub Auto-Sync CLI Tool** | Instant (1 command: `node scripts/add_repo.js <repo>`) | High (Auto-extracts GitHub metadata & tags) | High | Developer-friendly automation |

---

## 3. Implementation Plan (Phased Roadmap)

### Phase 1: Elevate `Next_Label_protfolio` with Live Demo
- Update `data/projects.json` and `index.html` for Project 2:
  - Add `liveDemoUrl: "https://next-label-portfolio.vercel.app"`
  - Add secondary CTA button: **"Live 3D Experience ↗"** alongside **"GitHub Repository"**
  - Highlight WebGL GPGPU shader particles and live 60 FPS performance.

### Phase 2: Ingest Additional Flagship Works (e.g. `digitools-projects`)
- Showcase `digitools-projects`:
  - Category: Modern React SaaS & Digital Tools
  - Tags: `React 19`, `Vite`, `Tailwind CSS`, `DaisyUI`
  - GitHub: `https://github.com/Imran7541/digitools-projects`
  - Live Demo: `https://symphonious-crisp-3617dc.netlify.app`
  - Badge: `Public Open Source`

### Phase 3: Transition `index.html` to Dynamic Project Hydration
- Make `projects-grid` auto-render from `data/projects.json` (with graceful fallback to inline initial data for zero-flicker SEO/static speed).
- When a new project is added to `data/projects.json`, the cards and filter counters update automatically.

### Phase 4: Stealth Admin Project Form (`Ctrl + Shift + A`)
- Extend the existing stealth admin drawer with a "+ Add Project" tab.
- Admin inputs Title, GitHub URL, Live Demo URL, Category, Tags, and selects Public vs. Private.
- Persists to `data/projects.json` and syncs dynamically.
