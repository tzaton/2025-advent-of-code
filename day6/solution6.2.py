import operator
from functools import reduce
from pathlib import Path

worksheet = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
operators = worksheet[-1].split()
values = ["".join(x).strip() for x in zip(*worksheet[:-1])]

problems = []

for i, val in enumerate(values):
    if i == 0:
        problems.append([val])
        continue

    if val:
        problems[-1].append(val)
    else:
        problems.append([])

result = 0

for problem, op in zip(problems, operators):
    if op == "*":
        solution = reduce(operator.mul, map(int, problem), 1)
    else:
        solution = reduce(operator.add, map(int, problem), 0)
    result += solution

print(f"Sum of all problem results: {result}")
