from typing import List, Tuple
from collections import deque

from aoc.intcode import Emulator


def solution(program: List[int], input: List[int]) -> str:
    e = Emulator(program, deque(input))
    e.run()
    return e.output.pop()


def parse_input(input: str) -> List[int]:
    return list(map(int, input.split(',')))


def main():
    with open('inputs/day5.txt') as fd:
        print(solution(parse_input(fd.read().strip()), [5]))
