DIRECTIONAL_KEYPAD = {
    "A": {"<": "^", "v": ">"},
    "<": {">": "v"},
    ">": {"^": "A", "<": "v"},
    "^": {">": "A", "v": "v"},
    "v": {"^": "^", "<": "<", ">": ">"},
}

NUMPAD_AUTOMATON = {
    "A": {"<": "0", "^": "3"},
    "0": {">": "A", "^": "2"},
    "1": {"^": "4", ">": "2"},
    "2": {">": "3", "v": "0", "^": "5", "<": "1"},
    "3": {"^": "6", "<": "2", "v": "A"},
    "4": {"^": "7", "v": "1", ">": "5"},
    "5": {"^": "8", "<": "4", ">": "6", "v": "2"},
    "6": {"^": "9", "<": "5", "v": "3"},
    "7": {"v": "4", ">": "8"},
    "8": {"v": "5", "<": "7", ">": "9"},
    "9": {"v": "6", "<": "8"},
}

KEYPAD_MOVES = {
    ("A", "^"): ["<"],
    ("A", ">"): ["v"],
    ("A", "<"): ["<v<", "v<<"],
    ("A", "v"): ["v<", "<v"],
    ("^", "A"): [">"],
    ("^", "v"): ["v"],
    ("^", ">"): ["v>", ">v"],
    ("^", "<"): ["<v"],
    ("<", "A"): [">>^", ">^>"],
    ("<", "^"): [">^"],
    ("<", "v"): [">"],
    ("<", ">"): [">>"],
    ("v", "A"): ["^>", ">^"],
    ("v", "^"): ["^"],
    ("v", "<"): ["<"],
    ("v", ">"): [">"],
    (">", "A"): ["^"],
    (">", "^"): ["^<", "<^"],
    (">", "<"): ["<<"],
    (">", "v"): ["<"],
}

# List by hand only the ones I will need
NUMPAD_MOVES = {
    ("A", "0"): ["<"],
    ("A", "1"): ["^<<"],
    ("A", "2"): ["^<", "<^"],
    ("A", "3"): ["^"],
    ("A", "4"): ["^^<<"],
    ("A", "6"): ["^^"],
    ("A", "8"): ["<^^^", "^^^<"],
    ("A", "9"): ["^^^"],
    ("0", "A"): [">"],
    ("0", "2"): ["^"],
    ("0", "8"): ["^^^"],
    ("1", "A"): [">>v"],
    ("1", "7"): ["^^"],
    ("2", "8"): ["^^"],
    ("2", "9"): [">^^", "^^>"],
    ("3", "A"): ["v"],
    ("3", "7"): ["^^<<", "<<^^"],
    ("4", "5"): [">"],
    ("4", "6"): [">>"],
    ("5", "A"): [">vv", "vv>"],
    ("5", "6"): [">"],
    ("5", "9"): [">^", "^>"],
    ("6", "A"): ["vv"],
    ("6", "7"): ["<<^", "^<<"],
    ("7", "1"): ["vv"],
    ("7", "9"): [">>"],
    ("8", "0"): ["vvv"],
    ("8", "3"): ["vv>", ">vv"],
    ("8", "4"): ["v<", "<v"],
    ("8", "5"): ["v"],
    ("9", "A"): ["vvv"],
    ("9", "8"): ["<"],
}


def list_keypad_moves(target: str) -> list[str]:
    state = "A"
    output = [""]
    for l in target:
        output = [x + more + "A" for x in output for more in NUMPAD_MOVES[(state, l)]]
        state = l
    return output


def list_programs(target: str) -> list[str]:
    state = "A"
    output = [""]
    for l in target:
        if l == state:
            output = [x + "A" for x in output]
        else:
            output = [
                x + more + "A" for x in output for more in KEYPAD_MOVES[(state, l)]
            ]
            state = l
    return output


def type_on_directional_keypad(instructions: str, repeat: int) -> str:
    output = ""
    state = "A"
    print(instructions)
    for l in instructions:
        if l == "A":
            output += state
        else:
            try:
                state = DIRECTIONAL_KEYPAD[state][l]
            except KeyError:
                print(f"Error with state = {state} and l = {l}")
    if repeat == 0:
        return output
    else:
        return type_on_directional_keypad(output, repeat - 1)


def press_on_numpad(instructions: str) -> str:
    output = ""
    state = "A"
    print(instructions)
    for l in instructions:
        if l == "A":
            output += state
        else:
            try:
                state = NUMPAD_AUTOMATON[state][l]
            except KeyError:
                print(f"Error with state = {state} and l = {l}")
    return output


USELESS_MOVES = {
    "<v<",
    "v<v",
    "^<^",
    "<^<",
    "v>v",
    ">v>",
    "^>^",
    ">^>",
    "A>vA",
    "Av<A",
    "A^<A",
    "A^>A",
    "v<A",
}


def extract_minimal_moves(moves: list[str]) -> list[str]:
    all_moves = [move for m in moves for move in list_programs(m)]

    useful_moves = [
        move for move in all_moves if not any(bad in move for bad in USELESS_MOVES)
    ]

    min_length = min(len(move) for move in useful_moves) if useful_moves else 0

    minimal_moves = [move for move in useful_moves if len(move) == min_length]
    return minimal_moves


def process_part1(codes: list[str]) -> None:
    total = 0
    for code in codes:
        print("For code:", code)
        moves = list_keypad_moves(code)
        moves = extract_minimal_moves(moves)
        moves = extract_minimal_moves(moves)
        print(f"There are {len(moves)} minimal moves")
        for move in moves[:10]:
            print((len(move), move))
        total += int(code[:3]) * min(len(w) for w in moves)
    print(f"The total is: {total}")
    return


def process_part2(codes: list[str]) -> None:
    total = 0
    for code in codes:
        print("For code:", code)
        moves = list_keypad_moves(code)
        for _ in range(25):
            moves = extract_minimal_moves(moves)
        print(f"There are {len(moves)} minimal moves")
        total += int(code[:3]) * min(len(w) for w in moves)
    print(f"The total is: {total}")
    return


if __name__ == "__main__":
    test = ["029A", "980A", "179A", "456A", "379A"]
    my_input = ["459A", "671A", "846A", "285A", "083A"]
    process_part1(my_input)
