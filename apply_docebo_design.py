import sys
import re

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS Replacements
css_outcome_card_old = """  .outcome-card {
    flex: 0 0 340px;
    border-radius: 20px;
    padding: 32px 28px 24px 28px;
    border: 1px solid rgba(255, 255, 255, 0.07);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }"""
css_outcome_card_new = """  .outcome-card {
    flex: 0 0 340px;
    border-radius: 20px;
    padding: 36px 32px 32px 32px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    background-size: cover;
    background-position: center;
    background-blend-mode: overlay;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
  }
  .outcome-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.3) 100%);
    pointer-events: none;
    z-index: 0;
  }
  .outcome-card > * {
    z-index: 1;
  }
  .read-story-link {
    margin-top: 24px;
    font-size: 11px;
    font-weight: 800;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    display: inline-block;
    text-decoration: none;
    transition: opacity 0.2s ease;
  }
  .read-story-link:hover { opacity: 0.8; }
"""

css_card_quote_old = """  .card-quote {
    font-size: 13.5px;
    line-height: 1.72;
    color: rgba(255,255,255,0.65);
    font-style: italic;
    margin-bottom: 24px;
    position: relative;
    z-index: 1;
  }"""
css_card_quote_new = """  .card-quote {
    font-size: 18px;
    line-height: 1.6;
    color: #fff;
    font-style: normal;
    font-weight: 500;
    margin-bottom: 32px;
    margin-top: 10px;
    position: relative;
    z-index: 1;
  }"""

css_id_name_old = """  .id-name {
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 2px;
  }"""
css_id_name_new = """  .id-name {
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 2px;
    color: #fff !important;
  }"""

css_id_desc_old = """  .id-desc {
    font-size: 11px;
    color: rgba(255,255,255,0.45);
    line-height: 1.5;
  }"""
css_id_desc_new = """  .id-desc {
    font-size: 12px;
    color: rgba(255,255,255,0.85);
    line-height: 1.4;
  }"""

css_outcome_number_old = """  .outcome-number {
    font-size: 40px;
    font-weight: 700;
    line-height: 1;
    letter-spacing: -0.02em;
    margin-bottom: 5px;
    position: relative;
    z-index: 1;
  }"""
css_outcome_number_new = """  .outcome-number {
    font-size: 48px;
    font-weight: 800;
    line-height: 1;
    letter-spacing: -0.02em;
    margin-bottom: 8px;
    position: relative;
    z-index: 1;
    color: #fff !important;
    margin-top: auto;
  }"""

css_outcome_label_old = """  .outcome-label {
    font-size: 12px;
    font-weight: 500;
    color: rgba(255,255,255,0.5);
    line-height: 1.4;
    position: relative;
    z-index: 1;
  }"""
css_outcome_label_new = """  .outcome-label {
    font-size: 15px;
    font-weight: 600;
    color: rgba(255,255,255,0.95);
    line-height: 1.4;
    position: relative;
    z-index: 1;
  }"""

content = content.replace(css_outcome_card_old, css_outcome_card_new)
content = content.replace(css_card_quote_old, css_card_quote_new)
content = content.replace(css_id_name_old, css_id_name_new)
content = content.replace(css_id_desc_old, css_id_desc_new)
content = content.replace(css_outcome_number_old, css_outcome_number_new)
content = content.replace(css_outcome_label_old, css_outcome_label_new)

# 2. HTML cleanup
content = re.sub(r'<div class="card-accent-line"[^>]*></div>', '', content)
content = re.sub(r'<div class="card-glow"[^>]*></div>', '', content)
content = content.replace('<div class="card-divider"></div>', '')

# Remove inline colors on names and numbers
content = re.sub(r'<div class="id-name" style="color: #[A-Fa-f0-9]+;">', '<div class="id-name">', content)
content = re.sub(r'<div class="outcome-number" style="color: #[A-Fa-f0-9]+;">', '<div class="outcome-number">', content)

# 3. HTML Card Replacements
colors = ['#8b5cf6', '#3b82f6', '#d946ef', '#10b981', '#f43f5e', '#f59e0b', '#6366f1']
bgs = [1, 2, 3, 4, 5, 1, 2]

cards_pattern = re.compile(r'<div class="outcome-card" style="background: radial-gradient[^>]*>.*?<div class="outcome-label">.*?</div>', re.DOTALL)

def replace_card(match):
    global card_idx
    if 'card_idx' not in globals():
        globals()['card_idx'] = 0
    
    color = colors[card_idx % 7]
    bg_num = bgs[card_idx % 7]
    card_idx += 1
    
    text = match.group(0)
    text = re.sub(r'style="background: radial-gradient[^"]*"', f'style="background-color: {color}; background-image: url(\\\'https://www.docebo.com/content/themes/phoenix/patterns/assets/testimonial-bg-0{bg_num}.webp\\\');"', text)
    
    # Append read story
    text += '\n            <a href="#" class="read-story-link">READ STORY &rarr;</a>'
    return text

content = cards_pattern.sub(replace_card, content)

# Fix backslashes in background-image url from the regex replacement
content = content.replace("\\'", "'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Applied Docebo design to testimonials successfully")
