import copy
import heapq

DIRECTIONS = {(0, 1), (1, 0), (0, -1), (-1, 0)}


def print_maze(maze: list[list[str]], visited: set[tuple[int, int]]) -> None:
    m = copy.deepcopy(maze)
    for i, j in visited:
        m[i][j] = "O"
    print("\n".join("".join(row) for row in m))


def create_maze(filename: str, memory_size: int, number_of_bytes) -> list[list[str]]:
    with open(filename) as file:
        blocks = [line.strip().split(",") for line in file]
    maze = [["."] * memory_size for _ in range(memory_size)]
    for n in range(number_of_bytes):
        j, i = blocks[n]
        maze[int(i)][int(j)] = "#"
    return maze


def solve_maze(maze: list[list[str]], memory_size: int) -> int:
    start = (0, 0)
    i_goal, j_goal = memory_size - 1, memory_size - 1
    goal = (i_goal, j_goal)

    def h(i: int, j: int) -> int:
        return (i_goal - i) + (j_goal - j)

    cost = {start: 0}
    visited = {start}
    pq = []
    heapq.heappush(pq, (h(*start), start))

    while pq:
        _, current = heapq.heappop(pq)
        visited.add(current)

        if current == goal:
            return cost[goal]

        i, j = current
        neighbours = []
        for Δi, Δj in DIRECTIONS:
            if (
                0 <= i + Δi < memory_size
                and 0 <= j + Δj < memory_size
                and maze[i + Δi][j + Δj] != "#"
            ):
                neighbours.append((i + Δi, j + Δj))
        for neighbour in neighbours:
            if neighbour not in cost or cost[neighbour] > cost[current] + 1:
                cost[neighbour] = cost[current] + 1
                heapq.heappush(pq, (cost[neighbour] + h(*neighbour), neighbour))
    return 0


def process_part1(filename: str, memory_size: int, number_of_bytes: int) -> None:
    maze = create_maze(filename, memory_size, number_of_bytes)
    steps = solve_maze(maze, memory_size)
    print(f"The minimum number of steps is {steps}")
    return


def process_part2(filename: str, memory_size: int, number_of_bytes: int) -> None:
    with open(filename, "r") as file:
        total_number_of_bytes = sum(1 for _ in file)
    right = total_number_of_bytes - number_of_bytes
    left = 1
    while left != right:
        mid = (left + right) // 2
        maze = create_maze(filename, memory_size, number_of_bytes + mid)
        if solve_maze(maze, memory_size) == 0:
            right = mid
        else:
            left = mid + 1
    with open(filename) as file:
        blocks = [line.strip().split(",") for line in file]
    print(
        "The block that cuts the escape is:",
        ",".join(blocks[number_of_bytes + left - 1]),
    )


if __name__ == "__main__":
    process_part1("input.txt", 71, 1024)
    process_part2("input.txt", 71, 1024)
