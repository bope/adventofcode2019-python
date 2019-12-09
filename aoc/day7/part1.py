from typing import List, Tuple
from collections import deque
from itertools import permutations

from aoc.intcode import Emulator


def run_with_phases(program: List[int], phases: List[int]) -> int:
    pipes = [deque() for _ in range(len(phases) + 1)]
    for i, phase in enumerate(phases):
        pipes[i].append(phase)

    pipes[0].append(0)
    emulators = [
        Emulator(program.copy(), input, output)
        for input, output in zip(pipes, pipes[1:])
    ]

    while not all(e.stopped for e in emulators):
        for e in emulators:
            e.run()

    return pipes[-1].pop()


def solution(program: List[int]) -> Tuple[int, Tuple[int, int, int, int, int]]:
    max_signal = 0
    max_phases = None
    for phases in permutations(range(5)):
        signal = run_with_phases(program, phases)
        if signal > max_signal:
            max_signal = signal
            max_phases = phases
    return max_signal, max_phases


def parse_input(input: str) -> List[int]:
    return list(map(int, input.split(',')))


def main():
    with open('inputs/day7.txt') as fd:
        print(solution(parse_input(fd.read().strip()))[0])
