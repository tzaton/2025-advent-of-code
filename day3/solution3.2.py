from pathlib import Path

total = 0
num_size = 12

for bank in Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines():
    first_position = 0
    max_numbers = []

    for i in range(num_size):
        last_position = len(bank) - num_size + i
        bank_slice = bank[first_position : last_position + 1]
        max_number = max(list(bank_slice))
        max_numbers.append(max_number)

        first_position += bank_slice.index(max_number) + 1

    bank_max = "".join(max_numbers)

    print(f"Bank: {bank}, Bank max: {bank_max}")
    total += int(bank_max)


print(f"Total sum: {total}")
