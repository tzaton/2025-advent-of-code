from pathlib import Path

position = 50
at_zero = 0

for move in Path(__file__).parent.joinpath(("input.txt")).read_text().strip().splitlines():
    direction = move[0]
    amount = int(move[1:]) % 100

    print(f"Current position: {position}, Move: {move}")

    if direction == "L":
        position -= amount
        if position < 0:
            position = 100 + position
    elif direction == "R":
        position += amount
        if position > 99:
            position = position - 100

    print(f"New position: {position}")
    if position == 0:
        at_zero += 1

print(f"Reached position 0 {at_zero} times")
