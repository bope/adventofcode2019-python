from aoc.day1 import part1, part2


def test_part1():
    assert part1.solution([12]) == 2
    assert part1.solution([14]) == 2
    assert part1.solution([1969]) == 654
    assert part1.solution([100756]) == 33583


def test_part2():
    assert part2.solution([14]) == 2
    assert part2.solution([1969]) == 966
    assert part2.solution([100756]) == 50346
