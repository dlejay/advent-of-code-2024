from functools import cache


@cache
def number_of_children(stone: str, blinks: int) -> int:
    n = len(stone)
    if blinks == 0:
        return 1
    result = 0
    if stone == "0":
        return number_of_children("1", blinks - 1)
    elif len(stone) % 2 == 0:
        return number_of_children(stone[: n // 2], blinks - 1) + number_of_children(
            str(int(stone[n // 2 :])), blinks - 1
        )
    else:
        return number_of_children(str(2024 * int(stone)), blinks - 1)


def process_part1(stones: str) -> int:
    return sum(number_of_children(stone, 25) for stone in stones.split())


def process_part2(stones: str) -> int:
    return sum(number_of_children(stone, 75) for stone in stones.split())


if __name__ == "__main__":
    with open("input.txt") as file:
        stones = file.read().strip()
    result1 = process_part1(stones)
    print(f"There are {result1} stones")
    result2 = process_part2(stones)
    print(f"There are {result2} stones")
