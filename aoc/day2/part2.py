from typing import List, Tuple
from aoc.day2.part1 import solution as solution1


def solution(input: List[int], target: int) -> Tuple[int, int]:
    for noun in range(100):
        for verb in range(100):
            i = input.copy()
            i[1] = noun
            i[2] = verb
            if solution1(i)[0] == target:
                return noun, verb


def parse_input(input: str) -> List[int]:
    return list(map(int, input.split(',')))



if __name__ == '__main__':
    with open('inputs/day2.txt') as fd:
        input = parse_input(fd.read())
        noun, verb = solution(input, 19690720)
        print(100 * noun + verb)
