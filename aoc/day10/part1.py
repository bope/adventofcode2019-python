from typing import List, Tuple, Set
from dataclasses import dataclass, astuple
import math

@dataclass
class Vec:
    x: int
    y: int

    def __hash__(self):
        return hash(astuple(self))

    def __sub__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x - other.x, self.y - other.y)

    def angle(self) -> float:
        return (math.degrees(math.atan2(self.y, self.x)) + 180) % 360

    def angle_between(self, other: 'Vec') -> float:
        return (self - other).angle()

def scan(ast: Vec, vecs: Set[Vec]) -> Set[Vec]:
    angles = set()
    ret = set()
    for vec in vecs:
        if vec == ast:
            continue
        angle = ast.angle_between(vec)
        if angle in angles:
            continue

        angles.add(angle)
        ret.add(vec)

    return ret


def solution(input: Set[Vec]) -> Tuple[Vec, Set[Vec]]:
    best = set()
    bestv = None
    for vec in input:
        s = scan(vec, input)
        if len(s) > len(best):
            best = s
            bestv = vec

    return bestv, best


def parse(input: str) -> Set[Vec]:
    ret = set()
    for y, line in enumerate(input.strip().split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                ret.add(Vec(x, y))
    return ret
        


def main():
    with open('inputs/day10.txt') as fd:
       print(len(solution(parse(fd.read()))[1]))
