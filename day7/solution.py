from math import pow


def possible(result: int, l: list[int]) -> bool:
    if len(l) == 1:
        return l[0] == result
    last = l[-1]
    remaining = l[:-1]
    mult = result % last == 0 and possible(result / last, remaining)
    add = result >= last and possible(result - last, remaining)
    return mult or add


def concat_int(x: int, y: int) -> int:
    return int(str(x) + str(y))


def deconcat_int(x: int, y: int) -> int:
    return int(str(x).rstrip(str(y)))


def possible2(result: int, l: list[int]) -> bool:
    if len(l) == 1:
        return l[0] == result
    last = l[-1]
    remaining = l[:-1]
    mult = result % last == 0 and possible2(result / last, remaining)
    add = result >= last and possible2(result - last, remaining)
    num_of_digits = pow(10, len(str(last)))
    concat = (
        result >= last
        and (result - last) % num_of_digits == 0
        and possible2((result - last) / num_of_digits, remaining)
    )
    return mult or add or concat


def process_part1(lines) -> int:
    count = 0
    for line in lines:
        result, numbers = line.split(":")
        l = list(map(int, numbers.split()))
        result = int(result)
        count += possible(result, l) * result
    return count


def process_part2(file) -> int:
    count = 0
    for line in lines:
        result, numbers = line.split(":")
        l = list(map(int, numbers.split()))
        result = int(result)
        count += possible2(result, l) * result
    return count


if __name__ == "__main__":
    with open("test.txt") as file:
        lines = file.readlines()
    result1 = process_part1(lines)
    result2 = process_part2(lines)
    print(f"Total calibration: {result1}")
    print(f"New total calibration: {result2}")
