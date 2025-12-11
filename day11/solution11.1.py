from pathlib import Path

data = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
data = {line.split(":")[0]: line.split(":")[1].split() for line in data}


def count_paths(graph, start: str, end: str) -> int:
    if start == end:
        return 1

    total = 0

    for neighbor in graph[start]:
        total += count_paths(graph, neighbor, end)

    return total


result = count_paths(data, "you", "out")
print(f"Number of different paths: {result}")
