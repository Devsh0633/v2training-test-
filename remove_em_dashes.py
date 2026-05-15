import re

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_em_dashes(text):
    parts = re.split(r'(<h[1-6][^>]*>.*?</h[1-6]>)', text, flags=re.DOTALL)
    for i in range(len(parts)):
        # If it's not a heading (even indices)
        if not re.match(r'<h[1-6]', parts[i]):
            # First replace spaced em dash with comma and space
            parts[i] = parts[i].replace(' — ', ', ')
            # Then replace any remaining unspaced em dashes with just a comma and space
            parts[i] = parts[i].replace('—', ', ')
    return ''.join(parts)

new_content = replace_em_dashes(content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Em dashes replaced with commas outside of headings.")
