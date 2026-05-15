import re

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Google Fonts Link
old_font = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>'
new_font = '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Hanken+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>'
content = content.replace(old_font, new_font)

# 2. Update :root variables
root_pattern = r':root\s*\{[^}]+\}'
new_root = """:root {
    /* New Theme Scheme */
    --primary:     #0094FF;
    --secondary:   #050C33;
    --tertiary:    #E47100;
    --neutral:     #73777F;

    --navy:        var(--secondary);
    --navy-mid:    #081244; 
    --blue:        var(--primary);
    --blue-light:  #33A9FF;
    --cyan:        var(--primary);
    --cyan-soft:   #4DB4FF;
    --sky:         #E5F5FB;
    --sky-deep:    #D0EAF7;
    --white:       #FFFFFF;
    --gray-100:    #F5F6F8;
    --gray-200:    #E9EBEF;
    --gray-300:    #CBD5E0;
    --gray-500:    var(--neutral);
    --gray-700:    #4A5568;
    --text-dark:   var(--secondary);
    --text-body:   var(--neutral);
    --radius:      12px;
    --radius-sm:   8px;
    --shadow:      0 4px 24px rgba(5,12,51,.08);
    --shadow-md:   0 8px 40px rgba(5,12,51,.13);
    --transition:  .3s ease;
  }"""
content = re.sub(root_pattern, new_root, content, count=1)

# 3. Update body font to DM Sans
content = content.replace("font-family: 'Poppins', sans-serif;", "font-family: 'DM Sans', sans-serif;")

# 4. Add font classes for headlines and labels
match = re.search(r'body\s*\{[^}]+\}', content)
if match:
    typography_styles = """
  h1, h2, h3, h4, h5, h6, .section-title, .pm-title, .impact-title, .recognition-title, .cta-headline, .outcomes-title, .btn-primary, .btn-ghost {
    font-family: 'Plus Jakarta Sans', sans-serif;
  }
  
  .tag, .pm-eyebrow, .outcomes-eyebrow, .impact-eyebrow, .recognition-eyebrow, .integrations-eyebrow, .fm-badge, .pm-slider-label, .marquee-label, .h-stat-label, .metric-label {
    font-family: 'Hanken Grotesk', sans-serif;
  }
"""
    content = content[:match.end()] + typography_styles + content[match.end():]

# 5. Protect Hero Section
hero_fixes = """
  /* Protect Hero Section */
  #hero, #hero *, .hero-h1, .hero-sub, .hero-eyebrow, .hero-stats * {
    font-family: 'Poppins', sans-serif !important;
  }
  #hero .hero-eyebrow {
    color: #5BC4DE !important;
  }
  #hero .hero-h1 span {
    background: linear-gradient(135deg, #27AECE 0%, #2E87CC 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
  }
  #hero .btn-primary {
    background: #27AECE !important;
  }
  #hero .btn-primary:hover {
    background: #2E87CC !important;
    box-shadow: 0 8px 24px rgba(39,174,206,.35) !important;
  }
"""
hero_comment_idx = content.find('/* ── HERO ──────────────────────────────────────── */')
if hero_comment_idx != -1:
    content = content[:hero_comment_idx] + hero_fixes + content[hero_comment_idx:]

# 6. Apply tertiary accent to .tag
tag_old = """  .tag {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: var(--cyan);
    background: rgba(39,174,206,.1);
    border: 1px solid rgba(39,174,206,.25);"""
tag_new = """  .tag {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: var(--tertiary);
    background: rgba(228, 113, 0, 0.1);
    border: 1px solid rgba(228, 113, 0, 0.25);"""
content = content.replace(tag_old, tag_new)

# 7. Apply tertiary to pm-eyebrow and primary to pm elements
content = content.replace("color: #2DD4BF;", "color: var(--primary);")
content = content.replace("color: var(--primary);\n    font-weight: 700;\n    margin-bottom: 16px;\n    display: inline-block;\n  } /* pm-eyebrow */", "color: var(--tertiary);\n    font-weight: 700;\n    margin-bottom: 16px;\n    display: inline-block;\n  }")
# Better to use regex for pm-eyebrow specifically
content = re.sub(r'(\.pm-eyebrow\s*\{[^}]*color:\s*)var\(--primary\);', r'\1var(--tertiary);', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Theme applied successfully.")
