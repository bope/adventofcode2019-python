from aoc.day5 import part1


def test_part1():
    assert part1.solution(part1.parse_input('3,0,4,0,99'), [1]) == '1'

