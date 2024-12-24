from collections import defaultdict
from pprint import pprint


def execute(operation: tuple[int], register: dict[str, int]) -> None:
    op = operation[1]
    left = operation[0]
    right = operation[2]
    target = operation[4]
    if left not in register:
        print(f"{left} not yet known")
    if right not in register:
        print(f"{right} not yet known")
    if op == "XOR":
        register[target] = register[left] ^ register[right]
    if op == "OR":
        register[target] = register[left] or register[right]
    if op == "AND":
        register[target] = register[left] and register[right]


def process_part1(filename: str) -> None:
    # Initialisation
    register = {}
    operations = []
    with open(filename) as file:
        for line in file:
            if ":" in line:
                left, right = line.strip().split(": ")
                print(left, right)
                register[left] = int(right)
            elif "->" in line:
                operations.append(line.strip().split())
    print(register)
    print(operations)

    while operations:
        waiting = []
        for op in operations:
            left, right = op[0], op[2]
            if left in register and right in register:
                execute(op, register)
            else:
                waiting.append(op)
        operations = waiting
    pprint(register)

    result = sum(register.get(f"z{n:02}", 0) * 2**n for n in range(100))
    print("Result:", result)


def process_part2(filename: str) -> None:
    # Initialisation
    register = {}
    operations = []
    with open(filename) as file:
        for line in file:
            if ":" in line:
                left, right = line.strip().split(": ")
                print(left, right)
                register[left] = int(right)
            elif "->" in line:
                operations.append(line.strip().split())
    print(register)
    print(operations)
    print("AND", sum(1 for op in operations if op[1] == "AND"))
    print("XOR", sum(1 for op in operations if op[1] == "XOR"))
    print("OR", sum(1 for op in operations if op[1] == "OR"))
    pprint(sorted(operations, key=lambda op: op[1]))

    and_results = {
        entry[4] for entry in operations if (entry[1] == "AND" and entry[0] != "x00")
    }
    or_arguments = {entry[0] for entry in operations if entry[1] == "OR"} | {
        entry[2] for entry in operations if entry[1] == "OR"
    }
    suspicious = and_results - or_arguments
    non_xor_z_entries = {
        entry[4]
        for entry in operations
        if entry[4].startswith("z") and entry[1] != "XOR" and entry[4] != "z45"
    }
    suspicious |= non_xor_z_entries

    print(suspicious)


if __name__ == "__main__":
    process_part1("input.txt")
    process_part2("input.txt")
