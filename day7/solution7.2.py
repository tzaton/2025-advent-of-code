from collections import Counter
from pathlib import Path

lines = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()

active: Counter[int] = Counter()

for line in lines:
    if "S" in line:
        active = Counter({line.index("S"): 1})
        continue

    splitters = [i for i, ch in enumerate(line) if ch == "^"]

    next_active: Counter[int] = Counter()

    for pos, cnt in active.items():
        if pos in splitters:
            next_active[pos - 1] += cnt
            next_active[pos + 1] += cnt
        else:
            next_active[pos] += cnt

    active = next_active

print(f"Active timelines: {sum(active.values())}")
