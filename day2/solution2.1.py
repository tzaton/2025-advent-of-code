from pathlib import Path

invalid = []

for num_range in Path(__file__).parent.joinpath("input.txt").read_text().split(","):
    start, end = num_range.split("-")

    for num in range(int(start), int(end) + 1):
        print(num)

        num_len = len(str(num))
        if str(num)[: int(num_len / 2)] == str(num)[int(num_len / 2) :]:
            print(f"{num} is invalid")
            invalid.append(num)

print(f"Adding up all the invalid IDs in this example produces: {sum(invalid)}")
