import heapq
from collections import defaultdict
from itertools import product

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def get_maze(filename: str) -> tuple[list[list[str]], tuple[int, int], tuple[int, int]]:
    start_pos = None
    end_pos = None

    with open(filename, "r") as file:
        maze = []
        for row_index, line in enumerate(file):
            row = list(line.strip())
            if "S" in row:
                start_pos = (row_index, row.index("S"))
            if "E" in row:
                end_pos = (row_index, row.index("E"))
            maze.append(row)

    if start_pos is None or end_pos is None:
        raise ValueError("The maze must contain both 'S' (start) and 'E' (end) points.")

    return maze, start_pos, end_pos


def dijkstra(maze, start) -> dict[tuple[int, int], int]:
    rows = len(maze)
    cols = len(maze[0])
    cost = {start: 0}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        _, current = heapq.heappop(pq)

        neighbours = []
        i, j = current
        for Δi, Δj in DIRECTIONS:
            if (
                0 <= i + Δi < rows
                and 0 <= j + Δj < cols
                and maze[i + Δi][j + Δj] != "#"
            ):
                neighbours.append((i + Δi, j + Δj))
        for neighbour in neighbours:
            if neighbour not in cost or cost[neighbour] > cost[current] + 1:
                cost[neighbour] = cost[current] + 1
                heapq.heappush(pq, (cost[neighbour], neighbour))
    return cost


def compute_cheats(
    maze: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
    max_cheat_length: int,
) -> dict[int, int]:
    """
    Compute the cheats for the maze where 's' and 't' are searched within a
    limited range defined by max_cheat_length.

    :param maze: The maze as a 2D grid.
    :param start: The starting position.
    :param end: The ending position.
    :param max_cheat_length: The maximum distance to consider for cheats.
    :return: A dictionary where keys are time savings, and values are counts.
    """
    cost = dijkstra(maze, start)
    picoseconds = cost[end]
    back = dijkstra(maze, end)
    rows, cols = len(maze), len(maze[0])
    saved = defaultdict(int)

    for i, j in product(range(1, rows - 1), range(1, cols - 1)):
        if maze[i][j] == "#":
            continue
        # Restrict 's' and 't' to a local window around (i, j)
        min_s, max_s = max(1, i - max_cheat_length), min(rows - 1, i + max_cheat_length)
        min_t, max_t = max(1, j - max_cheat_length), min(cols - 1, j + max_cheat_length)

        for s, t in product(range(min_s, max_s + 1), range(min_t, max_t + 1)):
            if maze[s][t] == "#":
                continue
            dist = abs(s - i) + abs(t - j)
            if dist <= max_cheat_length:
                n = cost[(i, j)] + back[(s, t)] + dist
                if n < picoseconds - 99:
                    saved[picoseconds - n] += 1

    return saved


def process_part1(filename: str) -> None:
    maze, start, end = get_maze(filename)
    saved = compute_cheats(maze, start, end, 2)
    print("Collisions disabled for 2 picoseconds max")
    for key, value in sorted(saved.items()):
        print(f"There are {value} cheats that save {key} pico")
    total = sum(value for _, value in saved.items())
    print(f"There are {total} cheats that save at least 100 pico")


def process_part2(filename: str) -> None:
    maze, start, end = get_maze(filename)
    saved = compute_cheats(maze, start, end, 20)
    print("Collisions disabled for 20 picoseconds max")
    for key, value in sorted(saved.items()):
        print(f"There are {value} cheats that save {key} pico")
    total = sum(value for _, value in saved.items())
    print(f"There are {total} cheats that save at least 100 pico")


if __name__ == "__main__":
    process_part1("input.txt")  # 1422
    process_part2("input.txt")  # 1009299
