# DRI Library Bookshelf — Visual Editing Guide

This is a single self-contained HTML file (`bookshelf-final.html`) that renders a virtual library bookshelf from a CSV data file. This guide is written for people who want to change how the site **looks** without accidentally breaking how it **works**.

---

## How the Page Works (Plain English)

When the page loads it fetches a CSV file, parses it, and builds three views on top of each other:

1. **Loading Screen** — shown while data is being fetched
2. **Aisle View** — a library aisle showing one card ("endcap") per genre
3. **Shelf Detail View** — shown after clicking a genre; displays individual book spines on a wooden shelf
4. **Book Modal** — a popup that appears when you click any book spine

Only one view is visible at a time. The JavaScript swaps between them by adding/removing a `hidden` CSS class.

---

## Where to Find Things in the File

The file has three clearly separated sections you can navigate by searching:

| Search for this | What you'll find |
|---|---|
| `<style>` | Start of all CSS (line ~8) |
| `⚙️ CONFIGURATION` | The only JS block editors should ever touch |
| `PALETTES` | The book spine color arrays |
| `/* ═══ LOADING` | CSS for the loading screen |
| `/* ═══ AISLE VIEW` | CSS for the aisle/genre cards |
| `/* ═══ SHELF DETAIL` | CSS for the bookshelf page |
| `/* ═══ MODAL` | CSS for the book detail popup |
| `/* ═══ RESPONSIVE` | Mobile overrides (bottom of the `<style>` block) |

---

## The Color System — Your Primary Tool

Almost every color on the site is defined in one place: the `:root` block near the top of the `<style>` section (around line 11). Changing a value here updates it everywhere on the page.

```css
:root {
  /* ── Aisle View (light room) ── */
  --wall-bg: #f5f1eb;        /* main page background (warm off-white) */
  --ceiling-color: #f0ece6;  /* top gradient of the aisle room */
  --floor-color: #c8c0b4;    /* floor strip at the bottom */

  /* ── Shelf Endcap Cards ── */
  --shelf-white: #e8e2d8;    /* face of the endcap */
  --shelf-side: #d4cec4;     /* side panels of the endcap */
  --shelf-edge: #c4beb4;     /* border/shadow color */
  --label-bg: #f0ece4;       /* background of the genre label badge */

  /* ── Text on Light Backgrounds ── */
  --text-dark: #2c2824;      /* headings, body text */
  --text-mid: #6b6560;       /* subtitles, placeholders */

  /* ── Accent Colors (Light Mode) ── */
  --accent: #b0753a;         /* search bar focus ring, endcap hover */

  /* ── Bookshelf Wood (Dark Mode shelf page) ── */
  --wood-dark: #3E2723;      /* darkest wood tone */
  --wood-mid: #5D4037;       /* main shelf surface */
  --wood-highlight: #8D6E63; /* shelf lip highlight */

  /* ── Text on Dark Backgrounds ── */
  --text-light: #f5e6d3;     /* primary text on dark shelf */
  --text-dim-light: #a89279; /* secondary/muted text on dark shelf */

  /* ── Accent Colors (Dark Mode shelf page) ── */
  --accent-gold: #d4a858;    /* alphabetical section labels, links */
}
```

### Quick color recipes

| I want to change… | Edit this variable |
|---|---|
| Page background | `--wall-bg` |
| The genre card color | `--shelf-white` and `--shelf-side` |
| The genre label badge | `--label-bg` |
| The wooden shelf | `--wood-mid` (main surface) and `--wood-dark` (shadow) |
| Gold headings on shelf page | `--accent-gold` |
| Orange hover/focus highlights | `--accent` |

---

## Fonts

Three Google Fonts are loaded at the very top of the file (line 7):

| Font | Where it's used |
|---|---|
| **Playfair Display** | Page title ("The Library"), genre heading, alphabetical section letters |
| **Source Serif 4** | Book spine author names, search result titles |
| **DM Sans** | Everything else — body text, buttons, labels, inputs |

To swap a font, change the `family=` values in the `<link>` tag and update the matching `font-family:` declarations in the CSS. All three fonts are declared via `font-family: 'Playfair Display', serif` — search for the font name to find every usage.

---

## Book Spine Colors

Book spines are colored automatically using 8 preset palettes. Each genre is assigned one palette (always the same one for a given genre name), and each book within gets one color from that palette.

The palettes live in the JS at the line `const PALETTES = [` (around line 1181):

```js
const PALETTES = [
  ["#2c5f7c","#8b3a3a","#3b6b4f", ...],  // Palette 0 — muted blues/reds/greens
  ["#8b6914","#5c3d2e","#2e5047", ...],  // Palette 1 — earthy browns/teals
  ["#1e1e2e","#3a1a1a","#2a2a3a", ...],  // Palette 2 — very dark/gothic
  // ... 5 more
];
```

**Safe to change:** the hex color values inside each array. Keep the same number of colors per palette (8) and the same number of palettes (8) — changing those counts won't break anything functionally but will shift which colors are assigned to which genres and books.

**Do not change:** the `hashStr()`, `getBookColor()`, or `getBookHeight()` functions below the palettes — these are the logic that picks which color from which palette.

---

## Book Heights

Books vary in height to look realistic. The height is derived from the title length using the formula:

```
height = 120 + ((title.length × 7) % 60)
```

This means books are always between **120px and 179px** tall. To make all books taller or shorter, change the base value `120`. To increase the range of variation, change the `60`.

The function is `getBookHeight` (search for it). The one line to edit is:

```js
return 120 + ((title.length * 7) % 60);
//     ^^^                          ^^
//     min height (px)              variation range (px)
```

---

## Component-by-Component Style Guide

### Loading Screen

CSS class: `.loading-view`

The loading screen is a full-page centered layout. Key sub-elements:

- `.loading-spinner` — the spinning circle; its color is `border-top-color: var(--accent)`
- `.upload-zone` — the drag-and-drop file upload box (shown when no server CSV is found)
- `.upload-zone:hover` — hover/drag-over highlight state

### Aisle View (Genre Cards)

The aisle is a horizontally scrolling row of "endcap" cards, one per genre.

- `.aisle-view` — outer container; has the room background gradient and floor/ceiling
- `.ceiling-lights` / `.ceiling-light` — decorative white bars at the very top; remove or edit their `box-shadow` to change the glow effect
- `.floor` — the floor strip; color comes from `--floor-color`
- `.vanishing-glow` — a subtle radial glow in the center of the aisle; lower its `opacity` or remove the element to eliminate it
- `.aisle-header h1` — "The Library" title
- `.aisle-header .subtitle` — the italic tagline below the title
- `.shelf-endcap` — each genre card; width/height set here (default 150×180px)
- `.endcap-label` — the genre name badge on each card
- `.shelf-depth.left-depth` / `.shelf-depth.right-depth` — the 3D side panels on the endcap cards; remove to make them flat

### Shelf Detail View (Bookshelf Page)

The dark-background page that shows actual book spines.

- `.shelf-view` — outer container; background is hardcoded to `#1a1410` (very dark brown). To change the page background color, edit this selector directly rather than via a variable
- `.back-btn` — the "← Back to Library" button
- `.shelf-detail-header h2` — genre title in large text
- `.bookshelf-container` — the wooden shelf bar that books sit on; `background` uses `--wood-mid` and `--wood-dark`
- `.alpha-section` — a grouping block (one per starting letter)
- `.alpha-label` — the letter heading (e.g. "A · 12 works"); color is `--accent-gold`
- `.book` — individual book spine; width uses `clamp(34px, 4.5vw, 48px)` (min 34px, max 48px)
- `.book-spine-text` — the author last name printed on the spine
- `.book:hover` — the book "pop up" animation; controlled by `transform: translateY(-14px) scale(1.04)`

### Book Detail Modal

- `.modal-overlay` — the dark blurred backdrop; `backdrop-filter: blur(8px)` creates the frosted glass effect
- `.modal-card` — the popup card itself; background is a dark brown gradient
- `.modal-title` — book title at the top of the card
- `.modal-author` — author name in italic below the title
- `.modal-detail-row .value a` — clickable "View Text ↗" link; color is `--accent-gold`

---

## Responsive / Mobile

Mobile overrides are at the very bottom of the `<style>` block under `@media (max-width: 640px)`. These adjust padding, font sizes, and book/endcap widths for small screens. If you change any sizes in the main styles, check whether the mobile overrides also need updating.

---

## What NOT to Touch

The following JavaScript areas control data and behavior. Editing them can break the site:

| Area | Why hands-off |
|---|---|
| `const CSV_URL` | Points to the data file |
| `const COLUMN_MAP` | Maps your CSV headers to internal field names |
| `parseCSV()` / `splitCSVRow()` | CSV file reading and parsing |
| `processData()` / `groupByGenre()` | Builds the in-memory data structure |
| `renderAisle()` / `renderShelfBooks()` / `renderBooksIntoShelf()` | Builds the HTML from data |
| `handleGlobalSearch()` / `applyShelfFilters()` | Search and filter logic |
| `showShelf()` / `showAisle()` / `showBookDetail()` / `closeModal()` | View navigation |
| `hashStr()` / `getBookColor()` | Color assignment logic (edit PALETTES instead) |
| `init()` / `launchWithCSV()` | Application startup |

---

## Quick Reference: Safe vs. Risky Edits

| Change | Safe? |
|---|---|
| Editing any hex value in `:root` | ✅ Safe |
| Editing hex values inside `PALETTES` | ✅ Safe |
| Changing `font-family` values in CSS | ✅ Safe |
| Changing padding, margin, border-radius in CSS | ✅ Safe |
| Changing the `background` of `.shelf-view` | ✅ Safe |
| Editing the `120` base value in `getBookHeight` | ✅ Safe (cosmetic) |
| Changing the `width`/`height` of `.shelf-endcap` | ✅ Safe |
| Removing `.ceiling-lights` or `.vanishing-glow` HTML elements | ✅ Safe |
| Editing text inside HTML that is hardcoded (e.g. "The Library" in `<h1>`) | ✅ Safe |
| Editing anything inside `<script>` tags outside `PALETTES` | ⚠️ Risky |
| Changing `id=` attributes on HTML elements | ❌ Will break the JS |
| Renaming or removing CSS classes used by JavaScript | ❌ Will break rendering |
