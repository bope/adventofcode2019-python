from typing import List

from aoc.intcode import Emulator



def solution(input: List[int]) -> int:
    e = Emulator(input)
    e.run()
    blocks = set()

    while e.output:
        x = e.output.popleft()
        y = e.output.popleft()
        tid = e.output.popleft()
        if tid == 2:
            blocks.add((x,y))
        
    
    return len(blocks)


def parse(input: str) -> List[int]:
    return list(map(int, input.strip().split(',')))

def main():
    with open('inputs/day13.txt') as fd:
        print(solution(parse(fd.read())))
