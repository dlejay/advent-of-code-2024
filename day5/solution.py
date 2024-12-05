def check_update(rules: dict[int, set[int]], update: list[int]) -> bool:
    if len(update) < 2:
        return True
    first = update[0]
    tail = update[1:]
    for i in tail:
        if first in rules.get(i, {}):
            return False
    return check_update(rules, tail)


def prepare_data(input_string: str) -> (dict[int, set[int]], list[list[int]]):
    first_part, second_part = input_string.split("\n\n")
    rules = {}
    for pair in first_part.split():
        a, b = pair.split("|")
        if int(a) not in rules:
            rules[int(a)] = {int(b)}
        else:
            rules[int(a)].add(int(b))
    updates = []
    for tup in second_part.split():
        updates.append(list(map(int, tup.split(","))))
    return rules, updates


def process_part1(input_string: str) -> int:
    rules, updates = prepare_data(input_string)
    return sum(
        update[len(update) // 2] if check_update(rules, update) else 0
        for update in updates
    )


def middle_after_sort(rules: dict[int, set[int]], update: list[int]) -> int:
    return sorted(
        [(len(rules[n] & set(update)), n) if n in rules else (0, n) for n in update]
    )[len(update) // 2][1]


def process_part2(input_string: str) -> int:
    rules, updates = prepare_data(input_string)
    return sum(
        middle_after_sort(rules, update) if not check_update(rules, update) else 0
        for update in updates
    )


if __name__ == "__main__":
    with open("input.txt") as file:
        input_string = file.read()

    result1 = process_part1(input_string)
    print(f"Result for Part 1: {result1}")

    result2 = process_part2(input_string)
    print(f"Result for Part 2: {result2}")
