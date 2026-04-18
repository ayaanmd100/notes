import os, re

notes_dir = os.path.join(os.path.dirname(__file__), 'notes')

for fname in sorted(os.listdir(notes_dir)):
    if not fname.endswith('.tex'):
        continue
    fpath = os.path.join(notes_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    original = text

    # --- Fix 1: corrupted words containing "iff" ---
    # sed replaced \iff with \text{ iff } globally, even inside words
    text = text.replace(r'd\text{ iff }erence', 'difference')
    text = text.replace(r'D\text{ iff }erence', 'Difference')
    text = text.replace(r'd\text{ iff }erences', 'differences')
    text = text.replace(r'd\text{ iff }erent', 'different')
    text = text.replace(r'D\text{ iff }erent', 'Different')

    # --- Fix 2: standalone \text{ iff } (where \iff was) -> \rightarrow ---
    # In math context between expressions, use \rightarrow as substitute
    text = text.replace(r'\text{ iff }', r'\rightarrow ')

    # --- Fix 3: nested \text{ mod } inside \text{...} ---
    # e.g. \text{ (\text{ mod } } -> \text{(mod }
    text = text.replace(r'\text{ (\text{ mod } }', r'\text{(mod }')

    # --- Fix 4: remove \text{ok} (was \checkmark replacement) ---
    text = text.replace(r'\text{ok}', '')

    # --- Fix 5: standalone \bmod that became \text{ mod } ---
    # In expressions like "n \text{ mod } 4", use \% or just leave
    # Actually the real issue was \bmod inside \text{} creating nesting.
    # Standalone \text{ mod } between math is fine per supported list.
    # Leave those as-is.

    if text != original:
        with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f"Fixed: {fname}")

print("Done.")
