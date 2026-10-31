# System Architecture: Emran Hosen Portfolio

```mermaid
flowchart TD
    Client["Client Browser\n(Desktop / Mobile)"] --> |HTTP GET /| Server["Node.js Application Server\n(Port 5225)"]
    Client --> |GET /gallery.html| Server
    Client --> |GET /api/projects| Server
    Client --> |GET /api/agent/status| Server
    Client --> |POST /api/contact| Server

    subgraph "Frontend Layer"
        WebGL["Three.js Deep-Sea Abyss Engine\n(Custom GLSL Shaders & Particles)"]
        HTMLPages["index.html & gallery.html\n(Tailwind CSS & Glassmorphism)"]
        NavControl["Scroll Restoration & Offset Controller\n(scroll-mt-24 & manual restoration)"]
    end

    subgraph "Backend API Layer (server.js)"
        Router["Zero-Dependency Native HTTP Router"]
        StaticServe["Streamlined File Server with MIME Mapping"]
        Telemetry["Agent Hub Scanner (/home/emran/Documents/AI-Agents-Hub)"]
        InquiryLogger["Append-only JSONL Logger"]
    end

    subgraph "Data Storage"
        ProjectsDB[("data/projects.json")]
        InquiriesDB[("data/inquiries.jsonl")]
    end

    Server --> StaticServe
    StaticServe --> HTMLPages
    StaticServe --> WebGL
    Server --> Router
    Router --> Telemetry
    Router --> InquiryLogger
    InquiryLogger --> InquiriesDB
    Router --> ProjectsDB
```

## Pinned Core Dependencies & Technologies
- **Runtime**: Node.js v22+
- **Styling**: Tailwind CSS CDN, Montserrat & Inter Fonts
- **3D Graphics**: Three.js r128 (Procedural caustics, floating particles, caustics waves)
- **APIs**: Native Node.js `http`, `fs`, `path`, `url` (Zero npm vulnerabilities)
- **Data Stores**: Flat JSON (`data/projects.json`) & Append-only JSONL (`data/inquiries.jsonl`)
