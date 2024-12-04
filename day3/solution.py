import re
from typing import Tuple

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"(do\(\))"
dont_pattern = r"(don't\(\))"


def mult_pair(p: Tuple[str, str]) -> int:
    return int(p[0]) * int(p[1])


def process_part1(memory: str) -> int:
    """Calculate result for Part 1."""
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum(mult_pair(pair) for pair in re.findall(mul_pattern, memory))


def process_part2(memory: str) -> int:
    result = 0
    enabled = True
    pattern = mul_pattern + "|" + do_pattern + "|" + dont_pattern
    for instruction in re.findall(pattern, memory):
        if instruction[2]:  # do()
            enabled = True
            continue
        if instruction[3]:  # don't()
            enabled = False
            continue
        if enabled:
            result += mult_pair(instruction[:2])
    return result


if __name__ == "__main__":
    with open("input.txt") as file:
        memory = file.read()

    part1_result = process_part1(memory)
    print(f"The result for Part 1 is {part1_result}")
    # 170778545

    part2_result = process_part2(memory)
    print(f"The result for Part 2 is {part2_result}")
    # 82868252
