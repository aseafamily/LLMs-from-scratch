from pathlib import Path

file_path = Path("the-verdict.txt")
with file_path.open("r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of characters:", len(raw_text))
print(raw_text[:99])
