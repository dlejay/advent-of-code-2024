from dataclasses import dataclass
import re


@dataclass
class ClawMachine:
    A: tuple[int, int]
    B: tuple[int, int]
    Prize: tuple[int, int]


def tokens(machine: ClawMachine) -> int:
    A_x = machine.A[0]
    A_y = machine.A[1]
    B_x = machine.B[0]
    B_y = machine.B[1]
    P_x = machine.Prize[0]
    P_y = machine.Prize[1]
    det = A_x * B_y - A_y * B_x
    n_A = (P_x * B_y - P_y * B_x) / det
    n_B = (-P_x * A_y + P_y * A_x) / det
    if n_A == int(n_A) and n_B == int(n_B) and n_A > -1 and n_B > -1:
        return int(3 * n_A + n_B)
    else:
        return 0


def process_part1(path: str) -> int:
    with open(path) as file:
        text_machines = file.read().split("\n\n")
    machines = []
    for text_machine in text_machines:
        digits = re.findall("\d+", text_machine)
        machines.append(
            ClawMachine(
                A=(int(digits[0]), int(digits[1])),
                B=(int(digits[2]), int(digits[3])),
                Prize=(int(digits[4]), int(digits[5])),
            )
        )
    return sum(tokens(machine) for machine in machines)


def process_part2(machines: list[ClawMachine]) -> int:
    with open(path) as file:
        text_machines = file.read().split("\n\n")
    machines = []
    for text_machine in text_machines:
        digits = re.findall("\d+", text_machine)
        machines.append(
            ClawMachine(
                A=(int(digits[0]), int(digits[1])),
                B=(int(digits[2]), int(digits[3])),
                Prize=(
                    10000000000000 + int(digits[4]),
                    10000000000000 + int(digits[5]),
                ),
            )
        )
    # for machine in machines:
    #     print(tokens(machine))
    return sum(tokens(machine) for machine in machines)


if __name__ == "__main__":
    path = "input.txt"

    result1 = process_part1(path)
    print(f"Minimum number of tokens: {result1}")

    result2 = process_part2(path)
    print(f"Minimum number of tokens: {result2}")
