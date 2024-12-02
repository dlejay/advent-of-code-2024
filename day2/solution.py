from typing import List


def is_safe(report: List[int]) -> bool:
    n = len(report)

    if n < 2:
        return True

    diff_0 = report[1] - report[0]

    for k in range(n - 1):
        diff_k = report[k + 1] - report[k]
        if abs(diff_k) > 3:
            return False
        if abs(diff_k) < 1 or diff_k * diff_0 < 0:
            return False
    return True


def is_safe_with_dampener(report: List[int]) -> bool:
    return any(is_safe(report[:k] + report[k + 1 :]) for k in range(len(report)))


def check(current: int, after: int, monotony: int) -> bool:
    return monotony * (after - current) > 0 and abs(after - current) < 4


def sign(x: int) -> int:
    return (x > 0) - (x < 0)


def is_safe_with_dampener_optimised(report: List[int]) -> bool:
    n = len(report)

    # When n > 3, we can determine the monotony of the sequence
    # And from the given data, n is always greater than 3
    monotony = (
        sign(report[1] - report[0])
        + sign(report[2] - report[1])
        + sign(report[3] - report[2])
    )

    # if the monotony is 0, it means that we face something akin to [2, 1, 1, 5],
    # which cannot be fixed with one removal
    if monotony == 0:
        return False

    # Create a list of error pairs of points
    # Each int k will represent the pair (k, k+1)
    errors = []
    for k in range(n - 1):
        if not check(report[k], report[k + 1], monotony):
            errors.append(k)
    number_of_errors = len(errors)
    if number_of_errors > 2:
        # If there are more than two errors, it cannot be fixed by only one removal
        return False
    if number_of_errors == 2:
        k = errors[0]
        # If the two errors are not next to each other, it cannot work
        if k + 1 != errors[1]:
            return False
        # If the two errors are next to each other, the only possible fix is to remove k+1
        if not check(report[k], report[k + 2], monotony):
            return False
    if number_of_errors == 1:
        k = errors[0]
        # If the error happens at the start or at the end of the list, it's always fixable
        if k == n - 2 or k == 0:
            return True
        # If there is a single error, in the interior of the list, then we need to check if it's fixable  at k or at k+1
        if not check(report[k - 1], report[k + 1], monotony) and not check(
            report[k], report[k + 2], monotony
        ):
            return False

    return True


if __name__ == "__main__":
    reports = []

    with open("input.txt") as file:
        for line in file:
            report = list(map(int, line.split()))
            reports.append(report)

    safe = 0
    safe_with_dampener = 0

    for report in reports:
        safe += is_safe(report)
        safe_with_dampener += is_safe_with_dampener_optimised(report)
    print(f"It appears that {safe} reports are safe.")
    print(f"With the Problem Dampener, {safe_with_dampener} are safe.")

# Number of safe reports: 369
# Number of safe reports with the Problem Dampener: 428
