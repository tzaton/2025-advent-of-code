from pathlib import Path

position = 50
at_zero = 0

for move in Path(__file__).parent.joinpath(("input.txt")).read_text().strip().splitlines():
    direction = move[0]
    amount_total = int(move[1:])
    amount = int(move[1:]) % 100

    print(f"Current position: {position}, Move: {move}")
    old_position = position

    if direction == "L":
        position -= amount
        if position < 0:
            position = 100 + position

        if position > old_position and old_position != 0 and position != 0:
            at_zero += 1

    elif direction == "R":
        position += amount
        if position > 99:
            position = position - 100

        if position < old_position and old_position != 0 and position != 0:
            at_zero += 1

    print(f"New position: {position}")

    at_zero += amount_total // 100

    if (position == 0) and (amount_total % 100 != 0):
        at_zero += 1

print(f"Reached position 0 {at_zero} times")
