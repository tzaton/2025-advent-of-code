from pathlib import Path

invalid = []

for num_range in Path(__file__).parent.joinpath("input.txt").read_text().split(","):
    start, end = num_range.split("-")

    for num in range(int(start), int(end) + 1):
        print(num)

        num_len = len(str(num))

        for i in range(1, int(num_len / 2) + 1):
            if num_len % i != 0:
                continue

            if str(num)[:i] * (num_len // i) == str(num):
                print(f"{num} is invalid")
                invalid.append(num)
                break

print(f"Adding up all the invalid IDs in this example produces: {sum(invalid)}")