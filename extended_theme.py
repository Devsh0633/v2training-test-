import re

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section Backgrounds for a "New Feel"
# Make #integrations more brand-aligned (using new blue instead of teal)
content = content.replace('background: #F2F5F9;', 'background: var(--white);')
content = content.replace('color: #0D9488;', 'color: var(--primary);')
content = content.replace('background: #0D9488;', 'background: var(--primary);')
content = content.replace('background: #0F766E;', 'background: var(--blue-light);')
content = content.replace('border-color: #0D9488;', 'border-color: var(--primary);')

# Update #recognition badges (replacing teal with orange for tertiary pop)
content = content.replace('background: #E6FBF8; color: #0D9488;', 'background: rgba(228, 113, 0, 0.1); color: var(--tertiary);')
content = content.replace('background: #0D9488;', 'background: var(--tertiary);')

# 2. Update Feature Blocks to look more premium
feature_block_old = """  .feature-block {
    flex: 0 0 calc(50% - 16px);
    display: flex;
    flex-direction: column;
    gap: 32px;
    background: var(--white);
    border: 1px solid var(--gray-200);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    margin-bottom: 0 !important;
  }"""
feature_block_new = """  .feature-block {
    flex: 0 0 calc(50% - 16px);
    display: flex;
    flex-direction: column;
    gap: 32px;
    background: var(--white);
    border: 1px solid var(--gray-200);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(5,12,51,0.05); /* Modernized shadow */
    margin-bottom: 0 !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .feature-block:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 40px rgba(5,12,51,0.08);
  }"""
content = content.replace(feature_block_old, feature_block_new)

# 3. Update comparison table to new colors
comp_table_old = """  .comp-table th:nth-child(3) {
    background: var(--navy);
    color: var(--white);"""
comp_table_new = """  .comp-table th:nth-child(3) {
    background: var(--primary);
    color: var(--white);"""
content = content.replace(comp_table_old, comp_table_new)

# 4. Update Final CTA to be more striking
content = content.replace('background: linear-gradient(155deg, var(--navy) 0%, var(--navy-mid) 60%, #1a4a7a 100%);',
                          'background: linear-gradient(155deg, var(--secondary) 0%, #0A1B3D 50%, #002D54 100%);')
content = content.replace('.cta-headline span { color: var(--cyan); }', '.cta-headline span { color: var(--primary); }')

# 5. Fix Pricing Model colors (ensuring no hardcoded old navy remains)
content = content.replace('background: #0B1F3A;', 'background: var(--secondary);')

# 6. Ensure FAQ icon uses new colors
content = content.replace('background: var(--sky);', 'background: #F1F5F9;')
content = content.replace('border: 1px solid var(--sky-deep);', 'border: 1px solid var(--gray-200);')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Extended color theme and 'feel' update applied.")
