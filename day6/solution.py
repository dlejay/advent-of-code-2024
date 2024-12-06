from itertools import product


def print_data(data: list[list[str]]):
    print("\n".join("".join(list) for list in data))


def find_guard(data: list[list[str]]) -> tuple[int, int]:
    for i, j in product(range(len(data)), range(len(data[0]))):
        if data[i][j] == "^":
            return (i, j)


def walk(data: list[list[str]]) -> set:

    # initialise
    i, j = find_guard(data)
    visited = {(i, j)}

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    vector = directions[direction_index % 4]
    v_x = vector[0]
    v_y = vector[1]

    while 0 <= i < len(data) and 0 <= j < len(data[0]):
        visited.add((i, j))
        if not (0 <= i + v_x < len(data) and 0 <= j + v_y < len(data[0])):
            break
        if data[i + v_x][j + v_y] == "#":
            direction_index += 1
            vector = directions[direction_index % 4]
            v_x = vector[0]
            v_y = vector[1]
        else:
            i += v_x
            j += v_y
    return visited


def will_loop(data: list[list[str]], obstacle: tuple[int, int]) -> bool:
    i, j = find_guard(data)
    x, y = obstacle

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    vector = directions[direction_index % 4]
    v_x = vector[0]
    v_y = vector[1]
    visited = {(i, j, v_x, v_y)}
    while True:
        if not (0 <= i + v_x < len(data) and 0 <= j + v_y < len(data[0])):
            return False
        if data[i + v_x][j + v_y] == "#" or (x == i + v_x and y == j + v_y):
            direction_index += 1
            vector = directions[direction_index % 4]
            v_x = vector[0]
            v_y = vector[1]
        else:
            i += v_x
            j += v_y
        if (i, j, v_x, v_y) in visited:
            return True
        visited.add((i, j, v_x, v_y))


def process_part1(data: list[list[str]]) -> int:
    visited = walk(data)
    return len(visited)


def process_part2(data: list[list[str]]) -> int:
    x, y = find_guard(data)
    count = 0
    for i, j in product(range(len(data)), range(len(data[0]))):
        if not (i == x and y == j):
            count += will_loop(data, (i, j))
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        data = [list(line.strip()) for line in file]
    result1 = process_part1(data)
    print(f"The guard has taken {result1} distinct positions")
    # 5162
    result2 = process_part2(data)
    print(f"We can choose {result2} positions for the obstruction")
    # 1909
