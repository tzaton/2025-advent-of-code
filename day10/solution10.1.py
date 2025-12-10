import re
from pathlib import Path

data = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


total_steps = 0

for line in data:
    diagram = list(re.match(r"\[(.*)\]", line).group(1).replace(".", "0").replace("#", "1"))
    diagram = tuple(int(x) for x in diagram)

    buttons = re.search(r"\((.*)\)", line).group(0).strip().replace("(", "").replace(")", "").split()
    buttons = [tuple(int(y) for y in x.split(",")) for x in buttons]

    start = tuple([0] * len(diagram))

    print(f"Diagram: {diagram}")
    print(f"Buttons: {buttons}")

    # BFS
    queue = [(start, 0)]
    visited = {start}
    found = False

    while queue and not found:
        state, steps = queue.pop(0)

        for button in buttons:
            new_state = list(state)
            for i in button:
                new_state[i] = 1 - new_state[i]
            new_state = tuple(new_state)

            if new_state == diagram:
                steps += 1
                found = True
                break

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))

    print(f"Steps required: {steps}")
    total_steps += steps
    print()

print(f"Total steps: {total_steps}")
