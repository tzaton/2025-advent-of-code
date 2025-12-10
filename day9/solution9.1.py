from itertools import combinations
from pathlib import Path

data = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
data = [list(map(int, x.split(","))) for x in data]

max_area = 0

for comb in combinations(data, 2):
    point_a, point_b = comb

    area = (abs(point_a[0] - point_b[0]) + 1) * (abs(point_a[1] - point_b[1]) + 1)

    if area > max_area:
        max_area = area

    print(f"Points: {comb}, area: {area}")

print(f"Max area: {max_area}")
