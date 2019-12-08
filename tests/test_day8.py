from aoc.day8 import part2


def test_part2():
    input = list(map(int, '0222112222120000'))
    assert part2.solution(input, (2, 2)) == '01\n10'
