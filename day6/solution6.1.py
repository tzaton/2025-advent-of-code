import operator
from functools import reduce
from pathlib import Path

worksheet = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
worksheet = [[val.strip() for val in row.split()] for row in worksheet]

transposed = list(zip(*worksheet))


def solve(problem) -> int:
    if problem[-1] == "*":
        return reduce(operator.mul, map(int, problem[:-1]), 1)
    return reduce(operator.add, map(int, problem[:-1]), 0)


result = sum(solve(problem) for problem in transposed)
print(f"Sum of all problem results: {result}")
