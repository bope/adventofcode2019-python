from typing import List

from aoc.intcode import Emulator



def solution(input: List[int]) -> int:
    input[0] = 2
    e = Emulator(input)
    
    score = 0
    paddle_x = None
    ball_x = None

    while not e.stopped:
        e.run()
        if len(e.output) >= 3:
            while len(e.output) > 2:
                x = e.output.popleft()
                y = e.output.popleft()
                tid = e.output.popleft()
                if (x, y) == (-1, 0):
                    score = tid
                    continue

                if tid == 3:
                    paddle_x = x
            
                elif tid == 4:
                    ball_x = x

        else:
            if ball_x > paddle_x:
                e.input.append(1)
            elif ball_x < paddle_x:
                e.input.append(-1)
            else:
                e.input.append(0)
        
    return score


def parse(input: str) -> List[int]:
    return list(map(int, input.strip().split(',')))

def main():
    with open('inputs/day13.txt') as fd:
        print(solution(parse(fd.read())))
