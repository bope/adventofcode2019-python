from typing import List


class Emulator:
    def __init__(self, program: List[int], input: List[int]):
        self.output = []
        self._ptr = 0
        self._program = program
        self._input = iter(input)

    def _parse_instruction(self, instruction):
        ins = '{:05d}'.format(instruction)
        mode_3, mode_2, mode_1 = map(int, ins[:-2])
        op = int(ins[-2:])
        return mode_3, mode_2, mode_1, op

    def _get(self, mode, pos):
        if mode:
            return pos
        return self._program[pos]

    def run(self):
        while True:
            start_ptr = self._ptr
            instruction = self._next()
            mode_3, mode_2, mode_1, op = self._parse_instruction(instruction)

            if op == 99:
                return

            if op == 1:
                p1 = self._next()
                p2 = self._next()
                p3 = self._next()
                self._program[p3] = self._get(mode_1, p1) + self._get(mode_2, p2)
            elif op == 2:
                p1 = self._next()
                p2 = self._next()
                p3 = self._next()
                self._program[p3] = self._get(mode_1, p1) * self._get(mode_2, p2)
            elif op == 3:
                p1 = self._next()
                self._program[p1] = next(self._input)
            elif op == 4:
                p1 = self._next()
                self.output.append(self._get(mode_1, p1))
    
    def _next(self):
        v = self._program[self._ptr]
        self._ptr += 1
        return v


def solution(program, input):
    e = Emulator(program, input)
    e.run()
    return ''.join(map(str, e.output))

def parse_input(input: str):
    return list(map(int, input.split(',')))



if __name__ == '__main__':
    with open('inputs/day5.txt') as fd:
        print(solution(parse_input(fd.read().strip()), [1]))
