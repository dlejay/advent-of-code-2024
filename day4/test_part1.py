from solution import process_part1


def test_line():
    puzzle = ["XMAS"]
    assert process_part1(puzzle) == 1

    puzzle = ["SAMX"]
    assert process_part1(puzzle) == 1

    puzzle = ["SAMXS"]
    assert process_part1(puzzle) == 1


def test_diag():
    puzzle = [
        "oXoooo",
        "ooMooo",
        "oooAoo",
        "ooooSo",
        "oooooo",
    ]
    assert process_part1(puzzle) == 1

    puzzle = [
        "Xooooo",
        "oMoooo",
        "ooAooo",
        "oooSoo",
        "oooooo",
    ]
    assert process_part1(puzzle) == 1

    puzzle = [
        "oooooo",
        "Xooooo",
        "oMoooo",
        "ooAooo",
        "oooSoo",
    ]
    assert process_part1(puzzle) == 1

    puzzle = [
        "Xooooo",
        "XMoooo",
        "oMAooo",
        "ooASoo",
        "oooSoo",
    ]
    assert process_part1(puzzle) == 2


def test_official():
    puzzle = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    assert process_part1(puzzle) == 18
