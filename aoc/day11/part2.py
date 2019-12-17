from typing import List
from dataclasses import dataclass, astuple

from aoc.intcode import Emulator
from aoc.day11.part1 import Vec, dirs, parse_input


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


def main():
    with open('inputs/day11.txt') as fd:
        print(solution(parse_input(fd.read())))
