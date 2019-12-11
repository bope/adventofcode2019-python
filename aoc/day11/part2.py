from typing import List
from dataclasses import dataclass, astuple
from aoc.intcode import Emulator


@dataclass
class Vec:
    x: int
    y: int

    def __hash__(self):
        return hash(astuple(self))

    def __add__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x + other.x, self.y + other.y)


dirs = [
    Vec(0, 1),
    Vec(1, 0),
    Vec(0, -1),
    Vec(-1, 0)
]


def solution(program: List[int]) -> str:
    pos = Vec(0, 0)
    robdir = 0
    white = set([pos])
    painted = set()
    e = Emulator(program)
    while not e.stopped:
        is_white = int(pos in white)
        e.input.append(is_white)
        e.run()
        color = e.output.popleft()
        if color:
            white.add(pos)
        elif is_white:
            white.remove(pos)
        painted.add(pos)

        turn = e.output.popleft()
        if turn:
            robdir -= 1
        else:
            robdir += 1

        pos += dirs[robdir % len(dirs)]

    min_y = min(p.y for p in white)
    max_y = max(p.y for p in white)
    min_x = min(p.x for p in white)
    max_x = max(p.x for p in white)

    ret = ""
    for y in range(max_y, min_y-1, -1):
        for x in range(max_x, min_x - 1, -1):
            if Vec(x, y) in white:
                ret += '#'
            else:
                ret += '.'
        ret += '\n'

    return ret


def parse_input(input: str) -> List[int]:
    return map(int, input.strip().split(','))


def main():
    with open('inputs/day11.txt') as fd:
        print(solution(parse_input(fd.read())))
