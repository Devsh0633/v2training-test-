# SimpliTrain Premium Design System & Style Guide

Welcome to the **SimpliTrain Design System**. This guide provides the visual tokens, core design rules, and reusable CSS/HTML recipes established on the main landing page. Use these guidelines to maintain a seamless, high-end, and high-conversion aesthetic across all other templates and child pages.

---

## 🎨 1. Core Color Palette

The SimpliTrain color scheme relies on rich, modern deep backgrounds, clear high-contrast white text overlays, and highly saturated premium color pops for tags and callouts.

### CSS Variables
```css
:root {
  /* Brand Core */
  --primary: #050c33;     /* Deep Navy Base background */
  --secondary: #00f2fe;   /* Electric Neon Blue / Cyan */
  --tertiary: #3b82f6;    /* Premium Classic Blue */
  --purple: #8b5cf6;      /* Royal Violet Accent */
  --amber: #f59e0b;       /* Bright Amber Highlight */
  
  /* Solid Semantic Accents (High-Contrast Badges) */
  --success: #0d9488;     /* Clean Teal (used for flat-rate/success tags) */
  --danger: #dc2626;      /* High-visibility Red (used for warnings/per-learner tags) */
  
  /* Text & Overlays */
  --text-white: #ffffff;
  --text-muted: rgba(255, 255, 255, 0.7);
  --glass-border: rgba(255, 255, 255, 0.2);
}
```

---

## font-family: 'Outfit', 'Inter', sans-serif;
```

### Type Hierarchy
- **Hero Title (`H1`):** `font-size: 56px; font-weight: 800; line-height: 1.1; letter-spacing: -0.02em;`
- **Section Heading (`H2`):** `font-size: 40px; font-weight: 800; line-height: 1.2; letter-spacing: -0.01em;`
- **Card Statistics:** `font-size: 64px; font-weight: 900; line-height: 1; letter-spacing: -0.03em;`
- **Body Copy:** `font-size: 16px; font-weight: 400; line-height: 1.6; color: var(--text-muted);`
- **Labels / Badges:** `font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;`

---

## 📐 3. The Signature "Chamfered Card" Recipe (Docebo Style)

This is the exact high-fidelity card layout implemented for the testimonials section. 

> [!IMPORTANT]
> **Why the Parent Wrapper is Required:** Standard box-shadows get clipped when using `clip-path` on a card. Placing `filter: drop-shadow(...)` on a parent `.card-wrapper` successfully projects a shadow outlines the exact diagonal shape of the child card.

### HTML Structure
```html
<div class="card-wrapper">
  <div class="outcome-card" style="background-color: #8b5cf6; background-image: url('gradient-pattern.webp');">
    <!-- Card Identity -->
    <div class="card-identity">
      <div class="avatar-circle">JM</div>
      <div>
        <div class="id-name">Julian Mercer</div>
        <div class="id-desc">Founder & CEO<br>Commercial Education Provider</div>
      </div>
    </div>
    
    <!-- Testimonial / Quote -->
    <div class="card-quote">"Unified course catalog in one single point of sale."</div>
    
    <!-- Massive Impact Metric -->
    <div class="outcome-number">+180%</div>
    <div class="outcome-label">Increase in course sales revenue</div>
    
    <!-- Interactive Link -->
    <a href="#" class="read-story-link">READ STORY &rarr;</a>
  </div>
</div>
```

### CSS Recipe
```css
/* 1. Parent Wrapper (Maintains Shadow & Proportions) */
.card-wrapper {
  flex: 0 0 400px;
  height: 580px;
  padding: 10px; /* Essential to prevent shadow clipping */
  filter: drop-shadow(0 20px 25px rgba(0, 0, 0, 0.15)) 
          drop-shadow(0 10px 10px rgba(0, 0, 0, 0.1));
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.card-wrapper:hover {
  transform: translateY(-8px) scale(1.02);
}

/* 2. Capped / Chamfered Card Element */
.outcome-card {
  position: relative;
  width: 100%;
  height: 100%;
  padding: 48px 40px;
  background-size: cover;
  background-position: center;
  
  /* The Signature Chamfer (Top-Left & Bottom-Right cut, Top-Right & Bottom-Left rounded) */
  clip-path: polygon(40px 0%, 100% 0%, 100% calc(100% - 40px), calc(100% - 40px) 100%, 0% 100%, 0% 40px);
  border-radius: 0 36px 0 36px;
  
  /* Inset white border (Does not get clipped by polygon clip-path) */
  box-shadow: inset 0 0 0 1.5px rgba(255, 255, 255, 0.25);
  
  display: flex;
  flex-direction: column;
  color: var(--text-white);
}

/* 3. Deepening overlay gradient for legible text */
.outcome-card::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(5,12,51,0) 0%, rgba(5,12,51,0.4) 50%, rgba(5,12,51,0.85) 100%);
  pointer-events: none;
  z-index: 1;
}

/* 4. High-Contrast Read Story Link with Hover Slide */
.read-story-link {
  position: relative;
  z-index: 2;
  color: #ffffff !important;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 11px;
  letter-spacing: 0.05em;
  text-decoration: none;
  margin-top: auto;
  align-self: flex-start;
  transition: transform 0.3s ease;
}

.read-story-link:hover {
  transform: translateX(6px);
}
```

---

## 🏷️ 4. Premium High-Contrast UI Components

To maintain readability and premium quality, use solid backgrounds with bold white text instead of semi-transparent tints.

### Reusable Badges (e.g. Pricing / Tag lists)
```css
.pm-card-badge {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 11px;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.05em;
}

/* High-Contrast Warning / Per-Learner Badges */
.pm-card.per-learner .pm-card-badge {
  background: var(--danger); /* #dc2626 Red */
  color: #ffffff;
}

/* High-Contrast Success / Flat-Rate Badges */
.pm-card.flat-rate .pm-card-badge {
  background: var(--success); /* #0d9488 Teal */
  color: #ffffff;
}
```

### Premium Buttons
Always provide a smooth transition for both scale, opacity, and borders.
```css
.btn-primary {
  background: linear-gradient(135deg, var(--secondary) 0%, var(--tertiary) 100%);
  color: var(--primary);
  font-weight: 700;
  padding: 14px 28px;
  border-radius: 8px;
  text-decoration: none;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0, 242, 254, 0.25);
}
```

---

## 📱 5. Responsive Design Adaptation

When building grids and custom containers, always plan adjustments for smaller screens to maintain legibility.

```css
/* Tablets (Max Width: 900px) */
@media (max-width: 900px) {
  .card-wrapper {
    flex: 0 0 340px; /* Scale down card width */
    height: 540px;   /* Scale down card height */
  }
  
  .outcome-card {
    padding: 36px 30px; /* Tighter padding */
    clip-path: polygon(30px 0%, 100% 0%, 100% calc(100% - 30px), calc(100% - 30px) 100%, 0% 100%, 0% 30px);
  }
}

/* Mobile (Max Width: 600px) */
@media (max-width: 600px) {
  .card-wrapper {
    flex: 0 0 290px;
    height: 520px;
  }
  
  .outcome-card {
    padding: 28px 24px;
    clip-path: polygon(24px 0%, 100% 0%, 100% calc(100% - 24px), calc(100% - 24px) 100%, 0% 100%, 0% 24px);
  }
}
```
