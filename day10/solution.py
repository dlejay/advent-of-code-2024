from itertools import product


def find_trailheads(topographic_map: list[list[int]]) -> set[tuple[int, int]]:
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    return {
        (i, j)
        for i, j in product(range(rows), range(cols))
        if topographic_map[i][j] == 0
    }


def get_submits(
    topographic_map: list[list[int]], trailhead: tuple[int, int]
) -> set[tuple[int, int]]:
    i = trailhead[0]
    j = trailhead[1]
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    submits = set()
    if topographic_map[i][j] == 9:
        submits.add((i, j))
    for v_i, v_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (
            0 <= i + v_i < rows
            and 0 <= j + v_j < cols
            and topographic_map[i][j] + 1 == topographic_map[i + v_i][j + v_j]
        ):
            submits |= get_submits(topographic_map, (i + v_i, j + v_j))
    return submits


def get_rating(topographic_map: list[list[int]], trailhead: tuple[int, int]) -> int:
    i = trailhead[0]
    j = trailhead[1]
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    rating = 0
    if topographic_map[i][j] == 9:
        return 1
    for v_i, v_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (
            0 <= i + v_i < rows
            and 0 <= j + v_j < cols
            and topographic_map[i][j] + 1 == topographic_map[i + v_i][j + v_j]
        ):
            rating += get_rating(topographic_map, (i + v_i, j + v_j))
    return rating


def process_part1(topographic_map: list[list[int]]) -> int:
    trailheads = find_trailheads(topographic_map)
    return sum(len(get_submits(topographic_map, trailhead)) for trailhead in trailheads)


def process_part2(topographic_map: list[list[int]]) -> int:
    trailheads = find_trailheads(topographic_map)
    return sum(get_rating(topographic_map, trailhead) for trailhead in trailheads)


if __name__ == "__main__":
    with open("input.txt") as file:
        topographic_map = []
        for line in file:
            topographic_map.append([*map(int, list(line.strip()))])
    result1 = process_part1(topographic_map)
    print(f"{result1}")
    result2 = process_part2(topographic_map)
    print(f"{result2}")
