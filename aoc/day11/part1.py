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


def solution(program: List[int]) -> int:
    pos = Vec(0, 0)
    robdir = 0
    white = set()
    painted = set()
    e = Emulator(program)
    while not e.stopped:
        e.input.append(int(pos in white))
        e.run()
        color = e.output.popleft()
        if color:
            white.add(pos)
        else:
            white.remove(pos)
        painted.add(pos)

        turn = e.output.popleft()
        if turn:
            robdir -= 1
        else:
            robdir += 1

        pos += dirs[robdir % len(dirs)]

    return len(painted)


def parse_input(input: str) -> List[int]:
    return map(int, input.strip().split(','))


def main():
    with open('inputs/day11.txt') as fd:
        print(solution(parse_input(fd.read())))
