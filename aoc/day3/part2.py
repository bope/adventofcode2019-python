from typing import Set, List, Tuple, Optional, Dict
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


def path_to_map(path: List[Tuple[Direction, int]], start: Vec) -> Dict[Vec, int]:
    pos = start
    wmap = {}
    tot = 0
    for dir, steps in path:
        for _ in range(steps):
            tot += 1
            pos += dir.value
            if pos in wmap:
                continue
            wmap[pos] = tot
    return wmap


def solution(wire1: List[Tuple[Direction, int]], wire2: List[Tuple[Direction, int]]):
    start = Vec(0, 0)
    w1 = path_to_map(wire1, start)
    w2 = path_to_map(wire2, start)
    cross = w1.keys() & w2.keys()
    return min([w1[c] + w2[c] for c in cross])
    

def parse_path(input: str) -> List[Tuple[Direction, int]]:
    ret = []
    for p in input.split(','):
        d, s = p[0], p[1:]
        ret.append((Direction[d], int(s)))
    return ret


def parse_input(input: str) -> Tuple[List[Tuple[Direction, int]], List[Tuple[Direction, int]]]:
    w1, w2 = input.strip().split('\n')
    return parse_path(w1), parse_path(w2)

if __name__ == '__main__':
    with open('inputs/day3.txt') as fd:
        res = solution(*parse_input(fd.read()))
        print(res)

