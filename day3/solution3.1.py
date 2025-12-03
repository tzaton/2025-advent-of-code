from pathlib import Path

total = 0

for bank in Path(__file__).parent.joinpath(("input.txt")).read_text().strip().splitlines():
    max_first = max(list(bank[:-1]))
    max_first_position = bank.index(max_first)
    max_second = max(list(bank[max_first_position + 1 :]))

    bank_max = 10 * int(max_first) + int(max_second)

    print(f"Bank: {bank}, Bank max: {bank_max}")
    total += int(bank_max)


print(f"Total sum: {total}")
