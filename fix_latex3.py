import os

notes_dir = os.path.join(os.path.dirname(__file__), 'notes')

for fname in os.listdir(notes_dir):
    if not fname.endswith('.tex'):
        continue
    fpath = os.path.join(notes_dir, fname)
    with open(fpath, 'rb') as f:
        data = f.read()

    if b'\x04' not in data:
        continue

    # \cdot\cdot\cdot was corrupted by sed: \cd -> \x04, producing \x5c\x04ot\x04ot\x04ot
    # Fix: restore to \cdot\cdot\cdot
    data = data.replace(b'\x5c\x04ot\x04ot\x04ot', b'\\cdot\\cdot\\cdot')

    # Any remaining lone \x04ot patterns (shouldn't happen after above, but just in case)
    data = data.replace(b'\x04ot', b'cdot')

    with open(fpath, 'wb') as f:
        f.write(data)
    print(f"Fixed: {fname}")

print("Done.")
