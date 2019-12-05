from typing import List, Tuple


class Emulator:
    def __init__(self, program: List[int], input: List[int]):
        self.output = []
        self._ptr = 0
        self._program = program
        self._input = iter(input)

    def _parse_instruction(self, instruction: int) -> Tuple[List[int], int]:
        ins = '{:05d}'.format(instruction)
        modes = list(map(int, ins[:-2]))
        op = int(ins[-2:])
        return modes[::-1], op

    def _get(self, mode: int, pos: int) -> int:
        if mode:
            return pos
        return self._program[pos]

    def run(self) -> None:
        while True:
            start_ptr = self._ptr
            instruction = self._next()
            modes, op = self._parse_instruction(instruction)
            modes[2] = 1

            if op == 99:
                return

            if op == 1:
                p1, p2, p3 = self._params(3, modes)
                self._program[p3] = p1 + p2
            elif op == 2:
                p1, p2, p3 = self._params(3, modes)
                self._program[p3] = p1 * p2
            elif op == 3:
                p1 = self._next()
                self._program[p1] = next(self._input)
            elif op == 4:
                (p1,) = self._params(1, modes)
                self.output.append(p1)
            elif op == 5:
                p1, p2, = self._params(2, modes)
                if p1 != 0:
                    self._ptr = p2
            elif op == 6:
                p1, p2, = self._params(2, modes)
                if p1 == 0:
                    self._ptr = p2
            elif op == 7:
                p1, p2, p3 = self._params(3, modes)
                self._program[p3] = int(p1 < p2)
            elif op == 8:
                p1, p2, p3 = self._params(3, modes)
                self._program[p3] = int(p1 == p2)
 
    def _next(self) -> int:
        v = self._program[self._ptr]
        self._ptr += 1
        return v

    def _params(self, count: int, modes: List[int]):
        return [self._get(modes[c], self._next()) for c in range(count)]


def solution(program: List[int], input: List[int]) -> str:
    e = Emulator(program, input)
    e.run()
    return ''.join(map(str, e.output))


def parse_input(input: str) -> List[int]:
    return list(map(int, input.split(',')))



if __name__ == '__main__':
    with open('inputs/day5.txt') as fd:
        print(solution(parse_input(fd.read().strip()), [5]))
