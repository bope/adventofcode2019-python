from aoc.day6 import part1, part2


def test_part1():
    t1i = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
    assert part1.solution(part1.parse_input(t1i)) == 42


def test_part2():
    t1i = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

    assert part2.solution(part2.parse_input(t1i)) == 4
