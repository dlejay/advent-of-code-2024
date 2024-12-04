from typing import List
from itertools import product


def check_line(puzzle: List[str], i: int, j: int) -> bool:
    if j + 3 >= len(puzzle[0]):
        return False
    return all(puzzle[i][j + k] == "XMAS"[k] for k in range(4)) or all(
        puzzle[i][j + k] == "SAMX"[k] for k in range(4)
    )


def check_col(puzzle: List[str], i: int, j: int) -> bool:
    if i + 3 >= len(puzzle):
        return False
    return all(puzzle[i + k][j] == "XMAS"[k] for k in range(4)) or all(
        puzzle[i + k][j] == "SAMX"[k] for k in range(4)
    )


def check_diag(puzzle: List[str], i: int, j: int) -> bool:
    if i + 3 >= len(puzzle) or j + 3 >= len(puzzle[0]):
        return False
    return all(puzzle[i + k][j + k] == "XMAS"[k] for k in range(4)) or all(
        puzzle[i + k][j + k] == "SAMX"[k] for k in range(4)
    )


def check_anti_diag(puzzle: List[str], i: int, j: int) -> bool:
    if i - 3 < 0 or j + 3 >= len(puzzle[0]):
        return False
    return all(puzzle[i - k][j + k] == "XMAS"[k] for k in range(4)) or all(
        puzzle[i - k][j + k] == "SAMX"[k] for k in range(4)
    )


def process_part1(puzzle: List[str]) -> int:
    rows = len(puzzle)
    cols = len(puzzle[0])
    count_l = 0
    count_c = 0
    count_d = 0
    count_ad = 0
    for i, j in product(range(rows), range(cols)):
        if puzzle[i][j] not in {"X", "S"}:
            continue
        count_l += check_line(puzzle, i, j)
        count_c += check_col(puzzle, i, j)
        count_d += check_diag(puzzle, i, j)
        count_ad += check_anti_diag(puzzle, i, j)
    return count_l + count_c + count_d + count_ad


def x_mas(puzzle: List[str], i: int, j: int) -> bool:
    """
    (i,j) assumed to be in the interior of the puzzle
    """
    if puzzle[i][j] != "A":
        return False
    if {puzzle[i - 1][j - 1], puzzle[i + 1][j + 1]} == {"M", "S"} and {
        puzzle[i - 1][j + 1],
        puzzle[i + 1][j - 1],
    } == {"M", "S"}:
        return True
    return False


def process_part2(puzzle: List[str]) -> int:
    return sum(
        x_mas(puzzle, i, j)
        for i, j in product(range(1, len(puzzle) - 1), range(1, len(puzzle[0]) - 1))
    )


if __name__ == "__main__":
    with open("input.txt") as file:
        puzzle = file.readlines()
    result_1 = process_part1(puzzle)
    print(f"Total Part 1: {result_1}")
    # 2496

    result_2 = process_part2(puzzle)
    print(f"Total Part 2: {result_2}")
    # 1967
