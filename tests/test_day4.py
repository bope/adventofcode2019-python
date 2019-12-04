from aoc.day4 import part1, part2


def test_part1():
    assert part1.is_valid(111111) is True
    assert part1.is_valid(223450) is False
    assert part1.is_valid(123789) is False


def test_part2():
    assert part2.is_valid(112233) is True
    assert part2.is_valid(123444) is False
    assert part2.is_valid(111122) is True
