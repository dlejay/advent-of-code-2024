def get_fences(garden: list[str], i: int, j: int) -> int:
    region = garden[i][j]
    rows = len(garden)
    cols = len(garden[0])
    fences = 0
    for Δi, Δj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if not (
            0 <= i + Δi < rows
            and 0 <= j + Δj < cols
            and region == garden[i + Δi][j + Δj]
        ):
            fences += 1
    return fences


def visit_and_price_region(
    garden: list[str],
    i: int,
    j: int,
    visited: set[tuple[int, int]],
    frontier: list[tuple[int, int]],
    fn,
) -> int:
    rows = len(garden)
    cols = len(garden[0])
    area = 0
    fences = 0
    region_internal_frontier = [(i, j)]
    while region_internal_frontier:
        i, j = region_internal_frontier.pop()
        region = garden[i][j]
        if (i, j) in visited:
            continue
        visited.add((i, j))
        area += 1
        fences += fn(garden, i, j)
        for Δi, Δj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if (
                0 <= i + Δi < rows
                and 0 <= j + Δj < cols
                and region == garden[i + Δi][j + Δj]
            ):
                region_internal_frontier.append((i + Δi, j + Δj))
            if (
                0 <= i + Δi < rows
                and 0 <= j + Δj < cols
                and region != garden[i + Δi][j + Δj]
            ):
                frontier.append((i + Δi, j + Δj))
    return area * fences


def border_continue(garden: list[str], i: int, j: int, Δi: int, Δj: int) -> bool:
    region = garden[i][j]
    rows = len(garden)
    cols = len(garden[0])
    next_i = i + Δj
    next_j = j - Δi
    if not (0 <= next_i < rows and 0 <= next_j < cols):
        return False
    if not (0 <= next_i + Δi < rows and 0 <= next_j + Δj < cols):
        return region == garden[next_i][next_j]
    return (
        region == garden[next_i][next_j] and garden[next_i + Δi][next_j + Δj] != region
    )


def get_sides(garden: list[str], i: int, j: int) -> int:
    region = garden[i][j]
    rows = len(garden)
    cols = len(garden[0])
    sides = 0
    for Δi, Δj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if not (
            0 <= i + Δi < rows
            and 0 <= j + Δj < cols
            and region == garden[i + Δi][j + Δj]
        ):
            if not border_continue(garden, i, j, Δi, Δj):
                sides += 1
    return sides


def process_part1(garden: list[str]) -> int:
    visited = set()
    frontier = [(0, 0)]
    price = 0
    while frontier:
        i, j = frontier.pop()
        price += visit_and_price_region(garden, i, j, visited, frontier, get_fences)
    return price


def process_part2(garden: list[str]) -> int:
    visited = set()
    frontier = [(0, 0)]
    price = 0
    while frontier:
        i, j = frontier.pop()
        price += visit_and_price_region(garden, i, j, visited, frontier, get_sides)
    return price


if __name__ == "__main__":
    with open("input.txt") as file:
        garden = [line.strip() for line in file]

    result1 = process_part1(garden)
    print(f"Total price is: {result1}")
    result2 = process_part2(garden)
    print(f"Total price is: {result2}")
