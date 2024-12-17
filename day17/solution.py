class Computer:
    def __init__(self, a: int, b: int, c: int):
        self._Register_A = a
        self._Register_B = b
        self._Register_C = c
        self._instruction_pointer: int = 0
        self._stdout = ""

        self.OPCODE = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }

    def __repr__(self) -> str:
        return (
            "\n"
            f"Computer\n"
            f"Register A: {self._Register_A}\n"
            f"Register B: {self._Register_B}\n"
            f"Register C: {self._Register_C}\n"
            f"Instruction Pointer: {self._instruction_pointer}"
        )

    def _combo(self, operand: int) -> int:
        if 0 <= operand < 4:
            return operand
        elif operand == 4:
            return self._Register_A
        elif operand == 5:
            return self._Register_B
        elif operand == 6:
            return self._Register_C

    def _adv(self, operand: int) -> None:
        self._instruction_pointer += 2
        self._Register_A //= 2 ** self._combo(operand)

    def _bxl(self, operand: int) -> None:
        self._instruction_pointer += 2
        self._Register_B ^= operand

    def _bst(self, operand: int) -> None:
        self._instruction_pointer += 2
        self._Register_B = self._combo(operand) % 8

    def _jnz(self, operand: int) -> None:
        if self._Register_A:
            self._instruction_pointer = operand
        else:
            self._instruction_pointer += 2

    def _bxc(self, operand: int) -> None:
        self._instruction_pointer += 2
        self._Register_B ^= self._Register_C

    def _out(self, operand: int) -> None:
        self._instruction_pointer += 2
        if self._stdout:
            self._stdout += ","
        self._stdout += str(self._combo(operand) % 8)

    def _bdv(self, operand: int) -> None:
        self._instruction_pointer += 2
        self._Register_B = self._Register_A // 2 ** self._combo(operand)

    def _cdv(self, operand: int) -> None:
        self._instruction_pointer += 2
        self._Register_C = self._Register_A // 2 ** self._combo(operand)

    def run(self, program: str) -> None:
        self._instruction_pointer = 0
        program = [int(s) for s in program.split(",")]
        n = len(program)
        while True:
            if self._instruction_pointer >= n:
                return self._stdout
            opcode = program[self._instruction_pointer]
            operand = program[self._instruction_pointer + 1]
            self.OPCODE[opcode](operand)


def process_part1(filename: str) -> None:
    c = Computer(22817223, 0, 0)
    program = "2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0"
    print("Output:", c.run(program))


def process_part2(filename: str) -> None:
    program = "2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0"
    print("Program:", program)
    N = len(program) // 2
    A = 0
    for i in range(N + 1):
        for r in range(8):
            test = A + r * 8 ** (N - i)
            c = Computer(test, 0, 0)
            result = c.run(program)
            if program[-2 * i - 1] == result[-2 * i - 1]:
                A = test
                break
    c = Computer(A, 0, 0)
    print("A:", A)
    print("Output:", c.run(program))


if __name__ == "__main__":
    process_part1("input.txt")
    process_part2("input.txt")
