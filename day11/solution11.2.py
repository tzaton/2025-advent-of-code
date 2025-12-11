from functools import cache
from pathlib import Path

data = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
data = {line.split(":")[0]: line.split(":")[1].split() for line in data}


@cache
def count_paths(start: str, end: str, go_through: frozenset[str]) -> int:
    if start == end:
        return int(go_through.issubset({start}))

    total = 0

    for neighbor in data[start]:
        total += count_paths(neighbor, end, frozenset(go_through - {neighbor}))

    return total


result = count_paths("svr", "out", frozenset({"dac", "fft"}))
print(f"Number of different paths: {result}")
