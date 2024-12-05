from solution import process_part1, process_part2


def test_official():
    with open("test.txt") as file:
        input_string = file.read()

    assert process_part1(input_string) == 143
    assert process_part2(input_string) == 123
