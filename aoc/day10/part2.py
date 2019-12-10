from typing import List, Tuple, Set

from .  import part1


def solution(input: Set[part1.Vec]) -> int:
    station = part1.solution(input)[0]
    destroyed = 0
    a200 = None

    while a200 is None:
        found = part1.scan(station, input)
        input -= found
        if len(found) + destroyed < 200:
            destroyed += len(found)
            continue
        
        o = sorted([f for f in found], key=lambda v: (v.angle_between(station)+270) % 360)
        a200 = o[200 - 1 - destroyed]

        break
    return (a200.x * 100) + a200.y




def main():
    with open('inputs/day10.txt') as fd:
       print(solution(part1.parse(fd.read())))
