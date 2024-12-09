from itertools import product
from collections import defaultdict
from math import gcd


def get_antinodes(
    rows: int, cols: int, antenna1: tuple[int, int], antenna2: tuple[int, int]
):
    v_x = antenna2[0] - antenna1[0]
    v_y = antenna2[1] - antenna1[1]
    antinodes = set()
    if v_x % 3 == 0 and v_y % 3 == 0:
        antinodes.add((antenna1[0] + v_x / 3, antenna1[1] + v_y / 3))
        antinodes.add((antenna1[0] + 2 * v_x / 3, antenna1[1] + 2 * v_y / 3))
    if 0 <= antenna1[0] - v_x < rows and 0 <= antenna1[1] - v_y < cols:
        antinodes.add((antenna1[0] - v_x, antenna1[1] - v_y))
    if 0 <= antenna2[0] + v_x < rows and 0 <= antenna2[1] + v_y < cols:
        antinodes.add((antenna2[0] + v_x, antenna2[1] + v_y))

    return antinodes


def get_all_antinodes(
    rows: int, cols: int, antenna1: tuple[int, int], antenna2: tuple[int, int]
):
    v_x = antenna2[0] - antenna1[0]
    v_y = antenna2[1] - antenna1[1]
    p = gcd(v_x, v_y)
    antinodes = set()
    max_iter = abs(int(min(rows * p / v_x, cols * p / v_y))) + 1
    for n in range(0, max_iter):
        step_x = int(n * v_x / p)
        step_y = int(n * v_y / p)
        if 0 <= antenna1[0] - step_x < rows and 0 <= antenna1[1] - step_y < cols:
            antinodes.add((antenna1[0] - step_x, antenna1[1] - step_y))
        if 0 <= antenna1[0] + step_x < rows and 0 <= antenna1[1] + step_y < cols:
            antinodes.add((antenna1[0] + step_x, antenna1[1] + step_y))

    return antinodes


def get_antennas(lines: list[str]) -> dict[list[tuple[int, int]]]:
    antennas = defaultdict(list)
    rows = len(lines)
    cols = len(lines[0])
    for i, j in product(range(rows), range(cols)):
        if lines[i][j] != ".":
            antennas[lines[i][j]].append((i, j))
    return antennas


def process_part1(lines):
    antennas = get_antennas(lines)
    antinodes = set()
    rows = len(lines)
    cols = len(lines[0])
    for key in antennas:
        l = antennas[key]
        n = len(l)
        for i in range(n):
            for j in range(i + 1, n):
                antinodes |= get_antinodes(rows, cols, l[i], l[j])
    return len(antinodes)


def process_part2(lines):
    antennas = get_antennas(lines)
    antinodes = set()
    rows = len(lines)
    cols = len(lines[0])
    for key in antennas:
        l = antennas[key]
        n = len(l)
        for i in range(n):
            for j in range(i + 1, n):
                antinodes |= get_all_antinodes(rows, cols, l[i], l[j])
    return len(antinodes)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [line.strip() for line in file]
    result1 = process_part1(lines)
    print(f"Number of distinct antinode locations: {result1}")
    result2 = process_part2(lines)
    print(f"New number of distinct antinode locations: {result2}")
