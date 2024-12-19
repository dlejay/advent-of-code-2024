from functools import cache


@cache
def is_possible(design: str, towels: tuple[str]) -> bool:
    if design == "":
        return True
    for towel in towels:
        if design.endswith(towel):
            prefix = design[: -len(towel)]
            if is_possible(prefix, towels):
                return True
    return False


@cache
def total_possibilities(design: str, towels: tuple[str]) -> int:
    if design == "":
        return 1
    possibilities = 0
    for towel in towels:
        if design.endswith(towel):
            prefix = design[: -len(towel)]
            possibilities += total_possibilities(prefix, towels)
    return possibilities


def process_part1(filename: str) -> None:
    with open(filename) as file:
        first, second = file.read().strip().split("\n\n")
        towels = tuple(first.split(", "))
        designs = second.split()
    print(towels)
    print(designs)
    possible = 0
    for design in designs:
        possible += is_possible(design, towels)
    possible
    print(f"There are {possible} designs possible.")


def process_part2(filename: str) -> None:
    with open(filename) as file:
        first, second = file.read().strip().split("\n\n")
        towels = tuple(first.split(", "))
        designs = second.split()
    possible = 0
    for design in designs:
        possible += total_possibilities(design, towels)
    possible
    print(f"There are {possible} possibilities in total.")


if __name__ == "__main__":
    process_part1("input.txt")
    process_part2("input.txt")
