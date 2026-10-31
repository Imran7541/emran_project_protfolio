# Specification: Add New Facebook Reels (Context Engineering & Production Debugging)

```yaml
feature_id: "010-add-facebook-reels"
feature_name: "Add New Facebook Reels to Gallery Motion Track"
status: "completed"
owner: "Emran Hosen"
last_updated: "2026-10-31"
tech_stack:
  framework: "HTML5 / Tailwind CSS / Vanilla JS / Node.js"
  target_file: "gallery.html"
  new_videos:
    episode_05:
      reel_id: "1789443445598568"
      share_url: "https://www.facebook.com/share/v/1Guapgh1PZ/"
      embed_url: "https://www.facebook.com/plugins/video.php?height=600&href=https%3A%2F%2Fwww.facebook.com%2Freel%2F1789443445598568%2F&show_text=false&width=340&t=0"
      title_bn: "বড় প্রম্পট নয়, প্রয়োজন সঠিক Context: AI-কে দিয়ে Production-Ready কাজ"
      title_en: "AI Prompting Trap: Context vs Large Prompts"
      category: "Context Engineering"
      thumbnail: "assets/thumbnails/ep05_context_engineering.jpg"
      badge: "EPISODE 05"
    episode_06:
      reel_id: "1437967031757450"
      share_url: "https://www.facebook.com/share/v/1CSQNPuiKu/"
      embed_url: "https://www.facebook.com/plugins/video.php?height=600&href=https%3A%2F%2Fwww.facebook.com%2Freel%2F1437967031757450%2F&show_text=false&width=340&t=0"
      title_bn: "Build Successful তবুও Production Fail! AI Agent দিয়ে Root Cause Analysis"
      title_en: "Root Cause Analysis & Forensic Debugging with AI Agents"
      category: "Forensic Debugging"
      thumbnail: "assets/thumbnails/ep06_production_debugging.jpg"
      badge: "EPISODE 06"
```

---

## 1. User Intent & Requirements
The user requested adding two Facebook video links to the gallery:
1. `https://www.facebook.com/share/v/1Guapgh1PZ/`
2. `https://www.facebook.com/share/v/1CSQNPuiKu/`

Both links correspond to authentic Facebook Reels created by Emran Hosen discussing advanced AI workflows:
- Reel 1 (`1789443445598568`): Context Engineering over huge prompts to achieve production-ready AI outputs.
- Reel 2 (`1437967031757450`): Forensic debugging with AI Agents when builds succeed but production fails.

---

## 2. Behavioral Specifications (Gherkin BDD)

### Scenario 1: Video Card Renders Authentic Links & Modal Player
```gherkin
Given a visitor navigates to "gallery.html"
When the visitor reaches the Facebook Reels track (Serial 1)
Then Episode 05 card must show the title "বড় প্রম্পট নয়, প্রয়োজন সঠিক Context"
And Episode 06 card must show the title "Build Successful তবুও Production Fail!"
And clicking either card must open the full-screen video modal playing the exact Facebook Reel
And clicking "Watch Reel" or popout must link directly to the authentic Facebook share URL
```

### Scenario 2: Infinite Looping & Duplicate Set Integrity
```gherkin
Given the continuous motion track is translating at 45s linear
When Set A completes its cycle and transitions into Set B
Then Set B must contain identical Episode 05 and Episode 06 cards with matching thumbnails and click handlers
And there must be no visual popping, hitching, or mismatched card order
```

---

## 3. Tasks Breakdown (`speckit-tasks`)

### Phase 1: Asset Preparation & Thumbnail Crafting
- [x] T001 Resolve open graph metadata and reel IDs for both share links
- [x] T002 Generate high-octane 1000x1000 branded thumbnails matching the visual language of Ep 01–04
- [x] T003 Verify static serving of `assets/thumbnails/ep05_context_engineering.jpg` and `assets/thumbnails/ep06_production_debugging.jpg`

### Phase 2: Card Implementation in `gallery.html`
- [x] T004 Update Episode 05 in Set A with real title, description, category, and modal trigger
- [x] T005 Update Episode 06 in Set A with real title, description, category, and modal trigger
- [x] T006 Update Episode 05 and Episode 06 in Set B (Duplicated set) for seamless infinite motion
- [x] T007 Update any external link targets and onclick attributes to pass correct embed URL and share URL

### Phase 3: Verification & Visual Proof
- [x] T008 Verify with headless Chrome CDP that clicking Episode 05 and 06 opens the modal with the proper embed URL
- [x] T009 Capture live screenshot of the updated Facebook Reels carousel showing both new episodes
- [x] T010 Update `notes/PROJECT_STATE.md` and `notes/AGENT_HANDOVER.md`
