from typing import List, Tuple
from itertools import permutations, cycle
from collections import deque

from aoc.intcode import Emulator


def run_with_phases(program: List[int], phases: List[int]) -> int:
    pipes = [deque() for _ in range(len(phases))]
    emulators = []
    for i, phase in enumerate(phases):
        pipes[i].append(phase)
        emulators.append(
            Emulator(
                program.copy(),
                pipes[i],
                pipes[(i+1) % len(pipes)]
            )
        )

    pipes[0].append(0)

    while not all(e.stopped for e in emulators):
        # while not emulators[-1].stopped:
        for e in emulators:
            e.run()
    return pipes[0].pop()


def solution(program: List[int]) -> Tuple[int, Tuple[int, int, int, int, int]]:
    max_signal = 0
    max_phases = None
    for phases in permutations(range(5, 10)):
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
