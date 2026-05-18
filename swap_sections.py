import sys
import os

file_path = 'stl.html'
if not os.path.exists(file_path):
    print(f"Error: {file_path} not found")
    sys.exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Identify blocks
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

# Check the order of sections. We want to swap them regardless of which one is first.
if outcomes_start < feat_start < comp_start:
    # Current order is Outcomes -> Features -> Comparison
    print("Found order: CUSTOMER OUTCOMES -> FEATURES -> COMPARISON. Swapping them...")
    outcomes_block = content[outcomes_start:feat_start]
    features_block = content[feat_start:comp_start]
    new_content = content[:outcomes_start] + features_block + outcomes_block + content[comp_start:]
elif feat_start < outcomes_start < comp_start:
    # Order is Features -> Outcomes -> Comparison
    print("Found order: FEATURES -> CUSTOMER OUTCOMES -> COMPARISON. Swapping them...")
    features_block = content[feat_start:outcomes_start]
    outcomes_block = content[outcomes_start:comp_start]
    new_content = content[:feat_start] + outcomes_block + features_block + content[comp_start:]
else:
    print("Unexpected order of sections")
    sys.exit(1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully interchanged features and outcomes sections in stl.html.")
