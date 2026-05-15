import sys

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Identify features block
feat_start = content.find('<!-- ── FEATURES')
if feat_start == -1:
    print("Could not find FEATURES block start")
    sys.exit(1)

outcomes_start = content.find('<!-- ── CUSTOMER OUTCOMES')
if outcomes_start == -1:
    print("Could not find CUSTOMER OUTCOMES block start")
    sys.exit(1)

comp_start = content.find('<!-- ── COMPARISON')
if comp_start == -1:
    print("Could not find COMPARISON block start")
    sys.exit(1)

# Ensure the order is as expected: features -> outcomes -> comparison
if not (feat_start < outcomes_start < comp_start):
    print("Unexpected order of sections")
    sys.exit(1)

features_block = content[feat_start:outcomes_start]
outcomes_block = content[outcomes_start:comp_start]

# Swap them
new_content = content[:feat_start] + outcomes_block + features_block + content[comp_start:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully interchanged features and outcomes sections.")
