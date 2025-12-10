from pathlib import Path

diagram = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()

splits = 0

for line in diagram:
    if "S" in line:
        positions = {line.index("S")}
        continue

    splitters = [i for i, char in enumerate(line) if char == "^"]

    for splitter in splitters:
        if splitter in positions:
            splits += 1
            positions.discard(splitter)
            positions.update({splitter - 1, splitter + 1})

print(f"Total splits: {splits}")
