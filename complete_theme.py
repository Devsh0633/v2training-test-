import re

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace hardcoded RGBAs outside #hero
# We split by the Hero comment blocks to protect it.
parts = re.split(r'(/\* ── HERO .*?/\* ── OUTCOMES )', content, flags=re.DOTALL)

for i in range(len(parts)):
    # Even indices are outside the captured #hero block
    if i % 2 == 0:
        # Replace Cyan RGB (39,174,206) with New Primary Blue (0,148,255)
        parts[i] = parts[i].replace('39,174,206', '0,148,255')
        # Replace Navy RGB (14,31,69) with New Secondary Navy (5,12,51)
        parts[i] = parts[i].replace('14,31,69', '5,12,51')

content = ''.join(parts)

# 2. Update check-icon to use Tertiary Orange (#E47100)
# background: rgba(0,148,255,.15); was updated in step 1 from (39,174,206)
content = content.replace('background: rgba(0,148,255,.15);\n    color: var(--cyan);', 
                          'background: rgba(228, 113, 0, 0.15);\n    color: var(--tertiary);')

# 3. Apply Typography to Nav
content = content.replace(".nav-links a {", ".nav-links a {\n    font-family: 'Plus Jakarta Sans', sans-serif;")
content = content.replace(".nav-cta {", ".nav-cta {\n    font-family: 'Plus Jakarta Sans', sans-serif;")

# 4. Refine Section Titles and Stats
# The marquee and other small labels should use Hanken Grotesk
content = content.replace(".marquee-item {", ".marquee-item {\n    font-family: 'DM Sans', sans-serif;")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final theme refinements complete.")
