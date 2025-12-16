import os
import json
import re

SRC_DIR = "./data/json"

pattern = re.compile(r"^c_(.+)\.json$")

for fname in os.listdir(SRC_DIR):
    match = pattern.match(fname)
    if not match:
        continue

    row_id = match.group(1)
    src_path = os.path.join(SRC_DIR, fname)

    out_dir = os.path.join(SRC_DIR, row_id, "c-shows")
    os.makedirs(out_dir, exist_ok=True)

    with open(src_path, "r", encoding="utf-8") as f:
        c_list = json.load(f)

    if not isinstance(c_list, list):
        continue  # safety check

    for i, c in enumerate(c_list, start=1):
        c_id = c.get("id", f"{row_id}_{i}")
        filename = f'c-{c_id.split("/")[-1]}.json'

        with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
            json.dump(c, f, ensure_ascii=False, indent=2)
