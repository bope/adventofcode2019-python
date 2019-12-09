from typing import List, Tuple, Optional
from collections import deque
from aoc.intcode import Emulator


def solution(program: List[int], input: Optional[List[int]] = None) -> Emulator:
    e = Emulator(program, deque(input or []))
    e.run()
    return e


def parse(input: str) -> List[int]:
    return list(map(int, input.split(',')))


def main():
    with open('inputs/day9.txt') as fd:
        print(solution(parse(fd.read()), [2]).output.pop())
