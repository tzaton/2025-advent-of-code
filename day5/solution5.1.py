from pathlib import Path

data = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
id_ranges = [line for line in data if "-" in line]
ids = [line for line in data if line.isnumeric()]

fresh = set()

for id in ids:
    for id_range in id_ranges:
        start, end = map(int, id_range.split("-"))
        if start <= int(id) <= end:
            fresh.add(id)

print(f"Total fresh IDs: {len(fresh)}")
