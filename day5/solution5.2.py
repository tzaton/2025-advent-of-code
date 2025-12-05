from pathlib import Path

data = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
id_ranges = [tuple(map(int, line.split("-"))) for line in data if "-" in line]

id_ranges.sort()

non_overlapping = []

for i, id_range in enumerate(id_ranges):
    if not non_overlapping:
        non_overlapping.append(id_range)
        continue

    last_start, last_end = non_overlapping[-1]
    current_start, current_end = id_range

    if current_start >= last_start and current_end <= last_end:
        continue  # Fully contained -> skip
    elif current_start > last_end + 1:
        non_overlapping.append(id_range)  # No overlap -> add new range
    elif current_start == last_end + 1:
        non_overlapping[-1] = (last_start, current_end)  # Adjacent -> merge
    else:
        non_overlapping[-1] = (last_start, max(last_end, current_end))  # Partial overlap -> merge

fresh = sum(end - start + 1 for start, end in non_overlapping)
print(f"Total fresh IDs: {fresh}")
