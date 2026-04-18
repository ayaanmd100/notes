import os, re

notes_dir = os.path.join(os.path.dirname(__file__), 'notes')

# Replace \text{content} with " content " to avoid command-name collisions.
# e.g. \quad\text{or}\quad -> \quad or \quad (not \quador\quad)
pattern = re.compile(r'\\text\{([^}]*)\}')

def replacer(m):
    content = m.group(1)
    return ' ' + content + ' '

for fname in sorted(os.listdir(notes_dir)):
    if not fname.endswith('.tex'):
        continue
    fpath = os.path.join(notes_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    original = text
    text = pattern.sub(replacer, text)

    if text != original:
        with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f"Fixed: {fname}")

print("Done.")
