# CSS Class Reference — Where to Plug In Your Team's Designs

This guide maps every visual element in the Library visualization to the exact CSS class or variable that controls it. When your team delivers a design asset or style decision, this tells you exactly where to make the change in the code.

---

## Quick Start: The Fastest Changes

These are the highest-impact edits, all in one place at the top of the `<style>` block:

```css
:root {
    --shelf-white: #e8e2d8;      /* Shelf end-cap color */
    --shelf-side: #d4cec4;       /* Shelf end-cap gradient bottom */
    --shelf-edge: #c4beb4;       /* Shelf 3D depth sides */
    --label-bg: #f0ece4;         /* Genre label background */
    --floor-color: #c8c0b4;      /* Aisle floor */
    --ceiling-color: #f0ece6;    /* Aisle ceiling */
    --wall-bg: #f5f1eb;          /* Aisle walls / page background */
    --text-dark: #2c2824;        /* Primary text (light views) */
    --text-mid: #6b6560;         /* Secondary text */
    --accent: #b0753a;           /* Hover color on shelves */
    --wood-dark: #3E2723;        /* Bookshelf dark wood */
    --wood-mid: #5D4037;         /* Bookshelf mid wood */
    --wood-highlight: #8D6E63;   /* Bookshelf front lip */
    --text-light: #f5e6d3;       /* Primary text (dark views) */
    --text-dim-light: #a89279;   /* Secondary text (dark views) */
    --accent-gold: #d4a858;      /* Gold accent (genre labels, links) */
}
```

Changing these variables updates the colors across the entire site instantly. No need to hunt through individual classes.

---

## View 1 — The Library Aisle

### A1. Aisle Background

The aisle background is currently a CSS gradient. To replace it with your team's image:

**Class:** `.aisle-view`

```css
/* CURRENT */
.aisle-view {
    background: linear-gradient(180deg,
        var(--ceiling-color) 0%,
        var(--wall-bg) 12%,
        var(--wall-bg) 88%,
        var(--floor-color) 100%);
}

/* REPLACE WITH YOUR IMAGE */
.aisle-view {
    background: url('your-library-scene.png') center center / cover no-repeat;
}
```

**Related elements to consider removing if using a full background image:**

| Element | Class | What It Does |
|---------|-------|-------------|
| Ceiling lights | `.ceiling-lights`, `.ceiling-light` | Three white glow bars at top |
| Floor | `.floor` | Gradient bar at bottom |
| Vanishing glow | `.vanishing-glow` | Soft white glow in center |

To remove any of these, add `display: none;` to their CSS class or delete their HTML elements.

---

### A2. Shelf End-Cap

**Class:** `.shelf-endcap`

```css
/* CURRENT — CSS gradient */
.shelf-endcap {
    background: linear-gradient(180deg, var(--shelf-white) 0%, var(--shelf-side) 100%);
    border: 1px solid rgba(0,0,0,0.07);
    border-radius: 3px;
    width: 150px;
    height: 180px;
}

/* REPLACE WITH YOUR IMAGE */
.shelf-endcap {
    background: url('shelf-endcap.png') center center / cover no-repeat;
    border: none;  /* remove if your image has its own edge */
}
```

**Shelf divider lines** (the horizontal lines across the end-cap face):

| Line | Selector | Position |
|------|----------|----------|
| Line 1 | `.shelf-endcap::before` | 25% from top |
| Line 2 | `.shelf-endcap::after` | 55% from top |
| Line 3 | `.shelf-endcap .shelf-line-3` | 80% from top |

Remove these by setting `display: none;` or `background: transparent;` on each selector if your image already includes shelf lines.

**3D depth sides** (the angled panels on left and right):

| Side | Class |
|------|-------|
| Left depth | `.shelf-depth.left-depth` |
| Right depth | `.shelf-depth.right-depth` |

Remove or restyle these if your end-cap design doesn't need a 3D effect.

---

### A3. Genre Label

**Class:** `.endcap-label`

```css
.endcap-label {
    font-family: 'DM Sans', sans-serif;    /* ← Change font */
    font-weight: 600;                       /* ← Change weight */
    font-size: 0.72rem;                     /* ← Change size */
    text-transform: uppercase;              /* ← Remove if not wanted */
    letter-spacing: 0.1em;
    color: var(--text-dark);                /* ← Label text color */
    background: var(--label-bg);            /* ← Label background */
    padding: 8px 14px;
    border-radius: 3px;
    border: 1px solid rgba(0,0,0,0.08);    /* ← Label border */
}
```

**Hover state** (when mouse is over the shelf):

```css
.shelf-endcap:hover .endcap-label {
    background: var(--accent);   /* ← Hover background color */
    color: #fff;                 /* ← Hover text color */
    border-color: var(--accent); /* ← Hover border color */
}
```

---

### A4. Page Title

**Title:** `.aisle-header h1`
**Subtitle:** `.aisle-header .subtitle`

```css
.aisle-header h1 {
    font-family: 'Playfair Display', serif;  /* ← Change display font */
    font-size: clamp(1.8rem, 4vw, 2.8rem);  /* ← Responsive size */
    font-weight: 700;
    color: var(--text-dark);                 /* ← Title color */
    letter-spacing: 0.05em;
}

.aisle-header .subtitle {
    font-family: 'Source Serif 4', serif;    /* ← Change body font */
    font-size: 0.95rem;
    color: var(--text-mid);                  /* ← Subtitle color */
    font-style: italic;                      /* ← Remove if not wanted */
}
```

---

### Global Search Bar

**Class:** `.aisle-search-bar input`

```css
.aisle-search-bar input {
    border: 1px solid var(--shelf-edge);     /* ← Border color */
    border-radius: 6px;                      /* ← Corner rounding */
    background: rgba(255,255,255,0.7);       /* ← Background */
    color: var(--text-dark);                 /* ← Text color */
}

/* Focus state (when clicked into) */
.aisle-search-bar input:focus {
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(176,117,58,0.12);  /* ← Focus glow */
}
```

---

## View 2 — Shelf Detail

### B1. Page Background

**Class:** `.shelf-view`

```css
/* CURRENT */
.shelf-view {
    background: #1a1410;
}

/* REPLACE WITH TEXTURE */
.shelf-view {
    background: url('dark-texture.png') center center / cover;
}
```

---

### B2. Bookshelf Surface

**Class:** `.bookshelf-container`

```css
/* CURRENT — CSS gradient */
.bookshelf-container {
    background: linear-gradient(180deg, var(--wood-mid) 0%, var(--wood-dark) 100%);
    border-radius: 6px;
    padding: 24px 24px 12px;
}

/* REPLACE WITH WOOD TEXTURE */
.bookshelf-container {
    background: url('wood-shelf.png') center bottom / cover no-repeat;
}
```

**Shelf front lip:**

```css
.bookshelf-container::before {
    /* The visible front edge of the shelf */
    background: linear-gradient(180deg, var(--wood-highlight), var(--wood-dark));
    height: 10px;
}
```

**Top highlight:**

```css
.bookshelf-container::after {
    /* Subtle light reflection on top edge */
    background: linear-gradient(180deg, rgba(255,255,255,0.08), transparent);
    height: 5px;
}
```

---

### B3. Book Spine Colors

**Location:** `PALETTES` array in the `<script>` section (not CSS)

```javascript
const PALETTES = [
    ["#2c5f7c", "#8b3a3a", "#3b6b4f", ...],  // Palette 0
    ["#8b6914", "#5c3d2e", "#2e5047", ...],  // Palette 1
    // ... more palettes
];
```

Each genre is automatically assigned a palette based on its name. To control which genre gets which palette, you'd need to modify the `getBookColor()` function.

**Book dimensions:**

| Property | Class | Current Value |
|----------|-------|---------------|
| Spine width | `.book` | `clamp(34px, 4.5vw, 48px)` |
| Spine border radius | `.book` | `2px 4px 4px 2px` |
| Spine shadow | `.book` | `2px 0 6px rgba(0,0,0,0.3)` |
| Spine text font | `.book-spine-text` | `Source Serif 4, 0.5rem` |
| Spine text color | `.book-spine-text` | `rgba(255,255,255,0.85)` |
| Hover lift distance | `.book:hover` | `translateY(-14px)` |

**Book height** is controlled by JavaScript in the `getBookHeight()` function. Currently varies from 120–180px based on title length.

---

### B4. Controls (Back Button, Search, Filter)

**Back button:** `.back-btn`

```css
.back-btn {
    color: var(--text-dim-light);         /* ← Text color */
    border: 1px solid rgba(255,255,255,0.08);  /* ← Border */
    border-radius: 6px;
    padding: 8px 20px;
}
```

**Search input:** `.shelf-controls input`
**State dropdown:** `.shelf-controls select`

Both use the same base styling:

```css
.shelf-controls input,
.shelf-controls select {
    border: 1px solid rgba(255,255,255,0.1);  /* ← Border */
    background: rgba(255,255,255,0.06);        /* ← Background */
    color: var(--text-light);                  /* ← Text color */
    border-radius: 6px;
}
```

---

### Alphabetical Section Labels

**Class:** `.alpha-label`

```css
.alpha-label {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    color: var(--accent-gold);                          /* ← Letter color */
    border-bottom: 1px solid rgba(212,168,88,0.15);     /* ← Divider line */
}
```

---

## View 3 — Book Detail Modal

### C1. Modal Card

**Class:** `.modal-card`

```css
.modal-card {
    background: linear-gradient(135deg, #2c2218 0%, #1e1812 100%);  /* ← Card background */
    border: 1px solid rgba(255,255,255,0.08);                       /* ← Card border */
    border-radius: 12px;                                            /* ← Corner rounding */
    padding: 40px;
    max-width: 520px;
    box-shadow: 0 24px 80px rgba(0,0,0,0.6);                       /* ← Drop shadow */
}
```

**Modal text elements:**

| Element | Class | Key Properties |
|---------|-------|---------------|
| Genre tag | `.modal-genre` | `color: var(--accent-gold)`, `font-size: 0.7rem`, uppercase |
| Book title | `.modal-title` | `font-family: Playfair Display`, `color: var(--text-light)`, `1.5rem` |
| Author name | `.modal-author` | `font-family: Source Serif 4`, `color: var(--text-dim-light)`, italic |
| Detail label | `.modal-detail-row .label` | `color: var(--text-dim-light)` |
| Detail value | `.modal-detail-row .value` | `color: var(--text-light)` |
| Link color | `.modal-detail-row .value a` | `color: var(--accent-gold)` |

---

### C2. Modal Backdrop

**Class:** `.modal-overlay`

```css
.modal-overlay {
    background: rgba(10,8,6,0.85);    /* ← Color and opacity */
    backdrop-filter: blur(8px);        /* ← Blur amount (0 = no blur) */
}
```

---

## Fonts — How to Swap Them

Fonts are loaded via Google Fonts in the `<link>` tag at the top of the HTML:

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Source+Serif+4:opsz,wght@8..60,300;8..60,400;8..60,600&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
```

To change fonts:
1. Go to fonts.google.com
2. Select your new fonts
3. Copy the new `<link>` tag
4. Replace the existing one
5. Update every `font-family` reference in the CSS (search for the old font name)

The three font roles are:
- **Display:** Used in `.aisle-header h1`, `.shelf-detail-header h2`, `.modal-title`, `.alpha-label`
- **Body:** Used in `.aisle-header .subtitle`, `.modal-author`, `.book-spine-text`
- **UI:** Used in `body`, `.endcap-label`, `.back-btn`, `.shelf-controls`, `.modal-genre`, `.stats-bar`

---

## Adding Background Images — Step by Step

1. Place your image file in the same folder as the HTML (or in a subfolder like `images/`)
2. Find the CSS class for the element (use this guide)
3. Replace the `background` property:

```css
/* From this: */
background: linear-gradient(180deg, #5D4037, #3E2723);

/* To this: */
background: url('images/your-file.png') center center / cover no-repeat;
```

The `center center` controls position, `/cover` makes it fill the area, and `no-repeat` prevents tiling. For textures that should tile, use `repeat` instead of `no-repeat` and remove `/cover`.

---

## Quick Lookup Table

| I want to change… | Edit this class / variable |
|---|---|
| Overall page color (light) | `--wall-bg` |
| Overall page color (dark) | `.shelf-view { background }` |
| Shelf end-cap appearance | `.shelf-endcap` |
| Genre label look | `.endcap-label` |
| Genre label hover | `.shelf-endcap:hover .endcap-label` |
| Main title font/color | `.aisle-header h1` |
| Wooden shelf look | `.bookshelf-container` |
| Book spine width | `.book { width }` |
| Book spine colors | `PALETTES` array in JavaScript |
| Book hover behavior | `.book:hover` |
| Spine text font/size | `.book-spine-text` |
| Popup card background | `.modal-card` |
| Popup text colors | `.modal-title`, `.modal-author`, etc. |
| Link color in popup | `.modal-detail-row .value a` |
| Search box styling | `.aisle-search-bar input` |
| Filter dropdown styling | `.shelf-controls select` |
| Alphabet section headers | `.alpha-label` |
| Background blur on popup | `.modal-overlay { backdrop-filter }` |
| Accent/hover color globally | `--accent` |
| Gold highlight color globally | `--accent-gold` |
