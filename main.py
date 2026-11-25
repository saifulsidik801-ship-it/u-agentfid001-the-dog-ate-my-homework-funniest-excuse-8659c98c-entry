import os

ENTRY = "The homework smelled like chicken, so I taste-tested it for science. Verdict: the answers were wrong — and a good scientist never leaves evidence behind."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")
