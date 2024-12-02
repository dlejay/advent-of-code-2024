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


def is_fixable(report: List[int], index, monotony) -> int:
    """
    Expects report[index] to be an error.
    Will check for report[index+1] and edge cases.
    If a fix is possible by removing a level,
    the function returns the shift to the cursor that
    can be applied.
    A value of 0 means that it is not possible to fix
    """
    # If we are just before the last level of the report, it's
    # always fixable
    if index == len(report) - 2:
        return 1
    # Here we check for a second consecutive error
    # In which case the only possible fix is to remove index + 1
    if not check(report[index + 1], report[index + 2], monotony):
        if check(report[index], report[index + 2], monotony):
            return 2
        return 0

    # Now the last case is when the error is not followed by
    # a second error.
    # If the error is on the very first level, it's always fixable
    if index == 0:
        return 1
    # If there is a single error, in the interior of the report,
    # then we need to check if it's fixable at index or at index + 1
    if check(report[index - 1], report[index + 1], monotony) or check(
        report[index], report[index + 2], monotony
    ):
        return 2
    # If nothing worked
    return 0


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

    error_already_found = False
    k = 0
    while k < n - 1:
        if not check(report[k], report[k + 1], monotony):
            if error_already_found:
                return False
            error_already_found = True
            k += is_fixable(report, k, monotony)
        else:
            k += 1

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
