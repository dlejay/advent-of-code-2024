import heapq

DIRECTIONS = {(0, 1), (1, 0), (0, -1), (-1, 0)}


def h(
    position: tuple[int, int], direction: tuple[int, int], goal: tuple[int, int]
) -> int:
    i, j = position
    i_goal, j_goal = goal
    Δi, Δj = direction
    if Δj == 1:
        if i == i_goal:
            return j_goal - j
        else:
            return 1000 + (j_goal - j) + (i - i_goal)
    if Δi == -1:
        if j == j_goal:
            return i - i_goal
        else:
            return 1000 + (j_goal - j) + (i - i_goal)
    # In all other cases, one needs to make two turns at least to reach exit
    return 2000 + (j_goal - j) + (i - i_goal)


def lowest_score(maze: tuple[str]) -> int:
    rows = len(maze)
    cols = len(maze[0])
    start = (rows - 2, 1)
    goal = (1, cols - 2)
    cost = {start: 0}
    direction = (0, 1)

    priority_queue = []
    heapq.heappush(priority_queue, (h(start, direction, goal), start, direction))

    while priority_queue:
        value, current, direction = heapq.heappop(priority_queue)

        if current == goal:
            return cost[current]
        i, j = current
        for Δi, Δj in DIRECTIONS:
            neighbour = (i + Δi, j + Δj)
            if maze[i + Δi][j + Δj] == "#":
                continue
            if (Δi, Δj) == direction:
                tentative_cost = cost[current] + 1
            else:
                tentative_cost = cost[current] + 1001
            if neighbour not in cost or tentative_cost < cost[neighbour]:
                cost[neighbour] = tentative_cost
                heapq.heappush(
                    priority_queue,
                    (
                        cost[neighbour] + h(neighbour, (Δi, Δj), goal),
                        neighbour,
                        (Δi, Δj),
                    ),
                )


def seats(maze: tuple[str]) -> int:
    return 0


def print_seats(maze: tuple[str], seats: set[tuple[int, int]]) -> None:
    # Convert the maze from a tuple of strings to a list of lists for mutability
    maze_list = [list(row) for row in maze]

    # Replace characters at visited coordinates with 'O'
    for i, j in seats:
        maze_list[i][j] = "O"

    # Convert the modified maze back to a string and print it
    for row in maze_list:
        print("".join(row))


def process_part1(filename: str) -> None:
    with open(filename) as file:
        maze = tuple(line.strip() for line in file.readlines())
    print(f"Lowest score: {lowest_score(maze)}")


def process_part2(filename: str) -> None:
    with open(filename) as file:
        maze = tuple(line.strip() for line in file.readlines())
    print(f"Number of seats: {seats(maze)}")


if __name__ == "__main__":
    process_part1("test.txt")
    process_part2("test.txt")
