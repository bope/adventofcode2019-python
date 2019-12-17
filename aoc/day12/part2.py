from typing import List
from itertools import combinations
from dataclasses import dataclass, astuple
from copy import deepcopy
from aoc.day12.part1 import Moon, parse, step


def check_state(set1, set2):
    for a, b in zip(set1, set2):
        if a != b:
            return False
    return True

def solution(moons: List[Moon]) -> int:
    state = deepcopy(moons)
    steps = 0
    while True:
        step(moons)
        steps += 1
        if steps % 10000 == 0:
            print(steps)
        if check_state(state, moons):
            return steps

def main():
    with open('inputs/day12.txt') as fd:
        print(solution(parse(fd.read())))
