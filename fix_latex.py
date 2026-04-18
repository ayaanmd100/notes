import os

notes_dir = os.path.join(os.path.dirname(__file__), 'notes')

for fname in os.listdir(notes_dir):
    if not fname.endswith('.tex'):
        continue
    fpath = os.path.join(notes_dir, fname)
    with open(fpath, 'rb') as f:
        data = f.read()

    # Fix byte-level corruption from sed:
    # 1. Backslash + CR(0x0D) + ightarrow -> \rightarrow
    data = data.replace(b'\x5c\x0dightarrow', b'\x5crightarrow')
    # 2. Backslash + TAB(0x09) + ext{ -> \text{
    data = data.replace(b'\x5c\x09ext\x7b', b'\x5ctext\x7b')
    # 3. Standalone TAB + ext{ (no preceding backslash) -> \text{
    #    This handles cases where sed emitted TAB+ext{ without the backslash
    data = data.replace(b'\x09ext\x7b', b'\x5ctext\x7b')

    text = data.decode('utf-8', errors='replace')

    # Fix unsupported commands
    text = text.replace(r'\checkmark', r'\text{ok}')
    text = text.replace(r'\cdots', r'\cdot\cdot\cdot')
    text = text.replace(r'\bmod', r'\text{ mod }')
    text = text.replace(r'\ldots', r'\cdot\cdot\cdot')

    with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)

print("Done.")
