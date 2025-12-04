from copy import deepcopy
from pathlib import Path

diagram = Path(__file__).parent.joinpath(("input.txt")).read_text().replace(".", "0").replace("@", "1").splitlines()
diagram = [[int(cell) for cell in row] for row in diagram]

total = 0
marked_to_remove = deepcopy(diagram)

for i, row in enumerate(diagram):
    for j, cell in enumerate(row):
        sum_adjacent = 0

        if cell == 0:
            continue

        for index in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            if i + index[0] < 0 or j + index[1] < 0 or i + index[0] >= len(diagram) or j + index[1] >= len(row):
                continue
            neighbor_value = diagram[i + index[0]][j + index[1]]
            sum_adjacent += neighbor_value

        if sum_adjacent < 4:
            total += 1
            marked_to_remove[i][j] = "x"

output = "\n".join(["".join(str(cell) for cell in row) for row in marked_to_remove]).replace("0", ".").replace("1", "@")
print(output)

print(f"Total rolls removed: {total}")
Path(__file__).parent.joinpath("output4.1.txt").write_text(output)
