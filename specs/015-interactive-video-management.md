# Spec 015: Interactive Video Management Portal for Facebook, YouTube & LinkedIn

```yaml
feature: interactive_video_management
status: in_progress
version: "1.0.0"
date: "2026-11-01"
author: "Emran Hosen & Antigravity"
stack:
  backend: "Node.js HTTP Server (REST API)"
  storage: "data/videos.json + client-side localStorage fallback"
  frontend: "HTML5, Tailwind CSS, Vanilla JS, Swiper/Motion Marquee"
```

## 1. Overview & Business Rationale
The user requested an interactive, self-service video ingestion portal directly on the gallery page (`gallery.html`):
> *"amer gallery site a video add korar kono option nei ami fb ba youtube linkden er er video add krote pari jeno sei option ta nei seta add korte hobe"*
> (There is currently no option in my gallery site to add videos. I need an option so I can add Facebook, YouTube, or LinkedIn videos.)

This specification defines a high-tech, cyber-glassmorphic **"+ Add Video" modal and management engine** that allows Emran to effortlessly add new videos from Facebook Reels, YouTube videos/Shorts, and LinkedIn Insight posts with live preview, automatic thumbnail resolution, and hybrid dual-mode persistence (Node.js REST backend + GitHub Pages `localStorage` client persistence).

---

## 2. Architecture & Technical Design

### 2.1 Hybrid Persistence Strategy (Dual Engine)
1. **Node.js Production Server (`server.js`)**:
   - `GET /api/videos`: Reads `data/videos.json` and returns the unified list of all media items.
   - `POST /api/videos`: Validates input, parses URL into platform-specific embed source & thumbnail, assigns unique ID, and saves to `data/videos.json`.
   - `DELETE /api/videos/:id`: Allows deletion of custom-added items.
2. **Static GitHub Pages Engine (`localStorage`)**:
   - When hosted on GitHub Pages (`imran7541.github.io`), static hosts cannot accept `POST` requests.
   - The frontend automatically tests `fetch('/api/videos')`. If unavailable or fails, it merges the built-in seed database with `localStorage.getItem('emran_custom_videos')`.
   - Any added video is immediately saved to `localStorage` and dynamically injected into the DOM, persisting across browser sessions even without a running backend server.

### 2.2 Smart URL Parser Specification
- **YouTube URLs**:
  - Patterns: `youtube.com/watch?v=(ID)`, `youtu.be/(ID)`, `youtube.com/shorts/(ID)`, `youtube.com/embed/(ID)`
  - Output Embed: `https://www.youtube.com/embed/${ID}?autoplay=1`
  - Output Thumbnail: `https://img.youtube.com/vi/${ID}/hqdefault.jpg`
  - Aspect Ratio: `16:9` (Default) or `9:16` (if Shorts).
- **Facebook URLs**:
  - Patterns: `facebook.com/reel/(ID)`, `facebook.com/share/v/(ID)/`, `facebook.com/watch/?v=(ID)`
  - Output Embed: `https://www.facebook.com/plugins/video.php?height=600&href=${encodeURIComponent(url)}&show_text=false&width=340&t=0`
  - Aspect Ratio: `9:16` Portrait.
- **LinkedIn URLs**:
  - Patterns: `linkedin.com/posts/(ID)`, `linkedin.com/feed/update/urn:li:(ID)`
  - Output: Direct post link and embed card.

### 2.3 UI & Modal Components (`gallery.html`)
- **Action Triggers**:
  - **Global Header / Filter Bar Button**: Prominent `+ Add Video` button with coral accent glow (`#FF715B`), neon pulsing indicator, and tooltip.
  - **Section Action Micro-Buttons**: Fast "+ Add Reel" on Facebook header, "+ Add Post" on LinkedIn header, "+ Add YouTube" on YouTube header.
- **Executive Glass Modal (`#add-video-modal`)**:
  - Platform Radio Selector (Facebook Reel, YouTube, LinkedIn).
  - Smart URL Input with auto-detection (typing a YouTube or FB link auto-selects the platform and previews the thumbnail).
  - Title, Category badge, Episode/Tag, and Summary fields.
  - Interactive Live Card Preview inside modal.
  - "Publish to Gallery" and "Cancel" buttons.
- **Dynamic Ingestion & Rendering**:
  - Injects newly added card into active track/grid.
  - Updates filter counts (`All Content (N)`, `Facebook Reels (N)`, etc.).
  - Added custom cards display a discrete delete action for management.

---

## 3. Data Schema (`data/videos.json`)

```json
[
  {
    "id": "vid-fb-01",
    "platform": "facebook",
    "title": "কি ডেভেলপারদের চাকরি খাবে? (Will AI Replace Developers?)",
    "url": "https://www.facebook.com/share/v/1FxXPzNdX6/",
    "embedSrc": "https://www.facebook.com/plugins/video.php?height=600&href=https%3A%2F%2Fwww.facebook.com%2Freel%2F1689852442742183%2F&show_text=false&width=340&t=0",
    "thumbnail": "assets/thumbnails/ep01_will_ai_replace_devs.jpg",
    "category": "Career Strategy",
    "episode": "Episode 01",
    "summary": "AI যুগে সফটওয়্যার ইঞ্জিনিয়ারদের মূল শক্তি শুধু কোডিং নয়, সিস্টেম আর্কিটেকচার ও রিয়েল বিজনেস ভ্যালু ডেলিভারি।",
    "isPortrait": true,
    "isCustom": false,
    "createdAt": "2026-10-31T06:00:00Z"
  }
]
```

---

## 4. Gherkin BDD Scenarios

### Scenario: User Adds a YouTube Video via Modal
- **Given** the user is viewing `gallery.html`
- **When** the user clicks the "+ Add Video" button
- **And** selects "YouTube" and pastes a URL `https://youtu.be/dQw4w9WgXcQ`
- **And** fills in title "Autonomous Agent Orchestration with LangGraph"
- **And** clicks "Publish to Gallery"
- **Then** the YouTube thumbnail is fetched automatically
- **And** the video is stored in `data/videos.json` and `localStorage`
- **And** the new card appears in the YouTube section and total count increments by 1

### Scenario: User Adds a Facebook Reel
- **Given** the user is on the gallery page
- **When** the user adds a new Facebook Reel URL `https://www.facebook.com/share/v/1Guapgh1PZ/`
- **Then** the system converts the URL into the official Facebook video embed iframe
- **And** the reel card is injected into the infinite marquee track

### Scenario: GitHub Pages Offline / Client Fallback
- **Given** the user is on the static GitHub Pages deployment (`imran7541.github.io/emran_project_protfolio/gallery`)
- **When** the user adds a new video and the Node backend is unreachable
- **Then** the video is seamlessly persisted into `localStorage`
- **And** immediately rendered in the DOM without any network error crash

### Scenario: Custom Video Deletion
- **Given** a user has previously added a custom video
- **When** the user clicks the delete trash icon on the custom card
- **Then** the custom card is removed from both the DOM and persistent storage
