import os, re

notes_dir = os.path.join(os.path.dirname(__file__), 'notes')

for fname in os.listdir(notes_dir):
    if not fname.endswith('.tex'):
        continue
    fpath = os.path.join(notes_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Fix bare ightarrow (not preceded by 'r', i.e. not already part of \rightarrow)
    # This catches ightarrow that lost its leading \r due to sed corruption
    text = re.sub(r'(?<![rR])ightarrow', r'\\rightarrow', text)

    # Fix \mid (not supported) -> | for divisibility notation
    text = text.replace(r'\mid', '|')

    # Also catch any \to that's unsupported - actually \to IS supported, leave it

    with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)

print("Done.")
