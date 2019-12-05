from aoc.day5 import part1, part2


def test_part1():
    assert part1.solution(part1.parse_input('3,0,4,0,99'), [1]) == '1'


def test_part2():
    assert part2.solution(part2.parse_input('3,9,8,9,10,9,4,9,99,-1,8 '), [8]) == '1'
    assert part2.solution(part2.parse_input('3,9,8,9,10,9,4,9,99,-1,8 '), [9]) == '0'
    assert part2.solution(part2.parse_input('3,9,7,9,10,9,4,9,99,-1,8'), [7]) == '1'
    assert part2.solution(part2.parse_input('3,9,7,9,10,9,4,9,99,-1,8'), [8]) == '0'
    assert part2.solution(part2.parse_input('3,3,1108,-1,8,3,4,3,99'), [8]) == '1'
    assert part2.solution(part2.parse_input('3,3,1108,-1,8,3,4,3,99'), [7]) == '0'
    assert part2.solution(part2.parse_input('3,3,1107,-1,8,3,4,3,99'), [7]) == '1'
    assert part2.solution(part2.parse_input('3,3,1107,-1,8,3,4,3,99'), [8]) == '0'

    assert part2.solution(part2.parse_input('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'), [0]) == '0'
    assert part2.solution(part2.parse_input('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'), [1]) == '1'


    ti1 = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
    assert part2.solution(part2.parse_input(ti1), [7]) == '999'
    assert part2.solution(part2.parse_input(ti1), [8]) == '1000'
    assert part2.solution(part2.parse_input(ti1), [9]) == '1001'
