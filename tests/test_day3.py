from aoc.day3 import part1, part2


def test_part1():
    t1i = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    t2i = """
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
    assert part1.solution(*part1.parse_input(t1i)) == 159
    assert part1.solution(*part1.parse_input(t2i)) == 135


def test_part2():
    t1i = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    t2i = """
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
    assert part2.solution(*part2.parse_input(t1i)) == 610
    assert part2.solution(*part2.parse_input(t2i)) == 410

