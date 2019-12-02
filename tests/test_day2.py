from aoc.day2 import part1, part2


def test_part1():
    assert part1.solution([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert part1.solution([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert part1.solution([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5 ,99, 9801]
    assert part1.solution([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


