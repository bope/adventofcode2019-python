from typing import Set, List, Tuple
import enum
from dataclasses import dataclass, astuple


@dataclass
class Vec:
    x: int
    y: int

    def __add__(self, other: 'Vec'):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec'):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, n: int):
        return Vec(self.x * n, self.y * n)

    def __hash__(self):
        return hash(astuple(self))

    def distance(self):
        return abs(self.x) + abs(self.y)


class Direction(enum.Enum):
    U = Vec(0, 1)
    D = Vec(0, -1)
    L = Vec(-1, 0)
    R = Vec(1, 0)


def path_to_map(path: List[Tuple[Direction, int]], start: Vec) -> Set[Vec]:
    pos = start
    wmap = set()
    for dir, steps in path:
        for _ in range(steps):
            pos += dir.value
            wmap.add(pos)
    return wmap


def solution(wire1: List[Tuple[Direction, int]], wire2: List[Tuple[Direction, int]]):
    start = Vec(0, 0)
    w1 = path_to_map(wire1, start)
    w2 = path_to_map(wire2, start)

    cross = w1 & w2

    return min([(start - c).distance() for c in cross])


def parse_path(input: str) -> List[Tuple[Direction, int]]:
    ret = []
    for p in input.split(','):
        d, s = p[0], p[1:]
        ret.append((Direction[d], int(s)))
    return ret


def parse_input(input: str) -> Tuple[List[Tuple[Direction, int]], List[Tuple[Direction, int]]]:
    w1, w2 = input.strip().split('\n')
    return parse_path(w1), parse_path(w2)


def main():
    with open('inputs/day3.txt') as fd:
        res = solution(*parse_input(fd.read()))
        print(res)
