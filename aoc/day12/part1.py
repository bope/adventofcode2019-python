from typing import List
from itertools import combinations
from dataclasses import dataclass, astuple


@dataclass
class Vec:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash(astuple(self))

    def __sub__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def resize(self) -> 'Vec':
        return Vec(
            (int(self.x / abs(self.x))) if self.x else 0,
            (int(self.y / abs(self.y))) if self.y else 0,
            (int(self.z / abs(self.z))) if self.z else 0,
        )
    
    def energy(self):
        return sum(map(abs, astuple(self)))


@dataclass
class Moon:
    pos: Vec
    vel: Vec

    def __hash__(self):
        return hash(astuple(self.pos) + astuple(self.vel))

    def apply_gravity(self, other: 'Moon'):
        self.vel += (other.pos - self.pos).resize()
    
    def apply_velocity(self) -> None:
        self.pos += self.vel

    def energy(self) -> int:
        return self.pos.energy() * self.vel.energy()

def step(moons: List[Moon]):
    for a, b in combinations(moons, 2):
        a.apply_gravity(b)
        b.apply_gravity(a)

    for moon in moons:
        moon.apply_velocity()


def solution(moons: List[Moon]) -> int:
    for _ in range(1000):
        step(moons)

    return sum(moon.energy() for moon in moons)


def parse(input: str) -> List[Moon]:
    ret = []
    for line in input.strip().split('\n'):
        vs = [int(v.split('=')[1]) for v in line[1:-1].split(',')]
        ret.append(Moon(Vec(*vs), Vec(0, 0, 0)))
    return ret


def main():
    with open('inputs/day12.txt') as fd:
        print(solution(parse(fd.read())))
