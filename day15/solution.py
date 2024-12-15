from itertools import product

MOVES = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}


def GPS_sum(state: list[list[str]]) -> int:
    return sum(
        100 * i + j if state[i][j] == "O" else 0
        for i, j in product(range(len(state)), range(len(state[0])))
    )


def find_robot(state: list[list[str]]) -> tuple[int, int]:
    for i, j in product(range(len(state)), range(len(state[0]))):
        if state[i][j] == "@":
            return (i, j)


def move(
    state: list[list[str]], position: tuple[int, int], instruction: str
) -> tuple[int, int]:
    i, j = position
    Δi, Δj = MOVES[instruction]
    if state[i + Δi][j + Δj] == "#":
        return (i, j)
    if state[i + Δi][j + Δj] == ".":
        return (i + Δi, j + Δj)
    steps = 1
    while state[i + steps * Δi][j + steps * Δj] == "O":
        steps += 1
    if state[i + steps * Δi][j + steps * Δj] == "#":
        return (i, j)
    else:
        state[i + steps * Δi][j + steps * Δj] = "O"
        state[i + Δi][j + Δj] = "."
        return (i + Δi, j + Δj)


def process_part1(content: str) -> int:
    state, moves = content.split("\n\n")
    state = list(map(list, state.strip().split()))
    moves = "".join(moves.split())
    position = find_robot(state)
    # Clean up map
    state[position[0]][position[1]] = "."
    for i in range(len(moves)):
        position = move(state, position, moves[i])
    return GPS_sum(state)


def widen(state: list[list[str]]) -> list[list[str]]:
    widen = []
    for line in state:
        widened_line = []
        for char in line:
            if char == "O":
                widened_line.append("[")
                widened_line.append("]")
            else:
                widened_line.append(char)
                widened_line.append(char)
        widen.append(widened_line)
    return widen


def second_GPS_sum(state: list[list[str]]) -> int:
    return sum(
        100 * i + j if state[i][j] == "[" else 0
        for i, j in product(range(len(state)), range(len(state[0])))
    )


def can_move_block(
    state: list[list[str]], position: tuple[int, int], direction: tuple[int, int]
) -> bool:
    i, j = position
    Δi, Δj = direction
    if state[i][j] == ".":
        return True
    if state[i][j] == "#":
        return False
    if state[i][j] == "[":
        j_left = j
        j_right = j + 1
    else:
        j_left = j - 1
        j_right = j
    if Δj == 1:
        return can_move_block(state, (i, j_right + 1), direction)
    if Δj == -1:
        return can_move_block(state, (i, j_left - 1), direction)
    return can_move_block(state, (i + Δi, j_left), direction) and can_move_block(
        state, (i + Δi, j_right), direction
    )


def move_block(
    state: list[list[str]], position: tuple[int, int], direction: tuple[int, int]
) -> None:
    i, j = position
    Δi, Δj = direction
    if state[i][j] == ".":
        return
    if state[i][j] == "[":
        j_left = j
        j_right = j + 1
    else:
        j_left = j - 1
        j_right = j
    if Δj == 1:
        move_block(state, (i, j_right + 1), direction)
        state[i][j_right + 1] = "]"
        state[i][j_right] = "["
        state[i][j_right - 1] = "."
    if Δj == -1:
        move_block(state, (i, j_left - 1), direction)
        state[i][j_left - 1] = "["
        state[i][j_left] = "]"
        state[i][j_left + 1] = "."
    if Δj == 0:
        if state[i + Δi][j_left] == "[" and state[i + Δi][j_right] == "]":
            move_block(state, (i + Δi, j_left), direction)
        else:
            move_block(state, (i + Δi, j_left), direction)
            move_block(state, (i + Δi, j_right), direction)
        state[i + Δi][j_left] = "["
        state[i + Δi][j_right] = "]"
        state[i][j_left] = "."
        state[i][j_right] = "."


def move_robot(
    state: list[list[str]], position: tuple[int, int], instruction: str
) -> tuple[int, int]:
    i, j = position
    Δi, Δj = MOVES[instruction]
    direction = (Δi, Δj)
    if state[i + Δi][j + Δj] == "#":
        return (i, j)
    if state[i + Δi][j + Δj] == ".":
        return (i + Δi, j + Δj)
    if can_move_block(state, (i + Δi, j + Δj), direction):
        print("I can move that block!")
        move_block(state, (i + Δi, j + Δj), direction)
        return (i + Δi, j + Δj)
    return (i, j)


def print_robot(state: list[list[str]], position: tuple[int, int]) -> None:
    i, j = position
    state[i][j] = "@"
    print("\n".join(map("".join, state)))
    state[i][j] = "."


def process_part2(content: str) -> int:
    state, moves = content.split("\n\n")
    state = list(map(list, state.strip().split()))
    moves = "".join(moves.split())
    position = find_robot(state)

    # Clean up map
    state[position[0]][position[1]] = "."

    # Double in width
    position = (position[0], 2 * position[1])
    widened = widen(state)
    print_robot(widened, position)

    for i in range(len(moves)):
        print("Move", moves[i])
        position = move_robot(widened, position, moves[i])
        print_robot(widened, position)
    return second_GPS_sum(widened)


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()
    result1 = process_part1(content)
    print(f"{result1}")
    result2 = process_part2(content)
    print(f"{result2}")
