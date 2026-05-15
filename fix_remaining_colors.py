import re

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Protect Hero - though it doesn't seem to have these specific codes, but good practice
parts = re.split(r'(/\* ── HERO .*?/\* ── OUTCOMES )', content, flags=re.DOTALL)

for i in range(len(parts)):
    if i % 2 == 0:
        parts[i] = parts[i].replace('#0B1F3A', 'var(--secondary)')
        parts[i] = parts[i].replace('#0E1F45', 'var(--secondary)')

content = ''.join(parts)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Remaining legacy color codes replaced.")
