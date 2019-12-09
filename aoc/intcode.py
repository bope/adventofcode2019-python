from typing import List, Optional, Tuple
from collections import deque


class Emulator:
    def __init__(self, program: List[int], input: Optional[deque] = None, output: Optional[deque] = None):
        self._mem = program
        self._ptr = 0
        self.input = input
        self.output = output
        self.stopped = False

        if self.input is None:
            self.input = deque()

        if self.output is None:
            self.output = deque()

        self._op_funcs = {
            99: self._break,
            1: self._add,
            2: self._mul,
            3: self._input,
            4: self._output,
            5: self._jumptrue,
            6: self._jumpfalse,
            7: self._lessthan,
            8: self._equals,
        }

    def _g(self, mode: int, ptr: int) -> int:
        if mode == 1:
            return self._mem[ptr]
        return self._mem[self._mem[ptr]]

    def _p(self, count: int, modes: List[int]) -> List[int]:
        return [self._g(modes[i], self._ptr + i) for i in range(count)]

    def _parse_instruction(self, instruction: int) -> Tuple[int, List[int]]:
        op = instruction % 100
        modes = [
            instruction // 100 % 10,
            instruction // 1000 % 10,
            instruction // 10000 % 10,
        ]
        return op, modes

    def run(self) -> None:
        while not self.stopped:
            op, modes = self._parse_instruction(self._mem[self._ptr])
            self._ptr += 1

            if op not in self._op_funcs:
                raise Exception(f'invalid opcode: {op}')

            if not self._op_funcs[op](modes):
                return

    def _break(self, modes: List[int]) -> bool:
        self.stopped = True
        return False

    def _add(self, modes: List[int]) -> bool:
        modes[2] = 1
        p = self._p(3, modes)
        self._ptr += 3
        self._mem[p[2]] = p[0] + p[1]
        return True

    def _mul(self, modes: List[int]) -> bool:
        modes[2] = 1
        p = self._p(3, modes)
        self._ptr += 3
        self._mem[p[2]] = p[0] * p[1]
        return True

    def _input(self, modes: List[int]) -> bool:
        try:
            input = self.input.popleft()
        except IndexError:
            self._ptr -= 1
            return False

        modes[0] = 1
        p = self._p(1, modes)
        self._ptr += 1
        self._mem[p[0]] = input
        return True

    def _output(self, modes: List[int]) -> bool:
        p = self._p(1, modes)
        self._ptr += 1
        self.output.append(p[0])
        return True

    def _jumptrue(self, modes: List[int]) -> bool:
        p = self._p(2, modes)
        self._ptr += 2
        if p[0] != 0:
            self._ptr = p[1]
        return True

    def _jumpfalse(self, modes: List[int]) -> bool:
        p = self._p(2, modes)
        self._ptr += 2
        if p[0] == 0:
            self._ptr = p[1]
        return True

    def _lessthan(self, modes: List[int]) -> bool:
        modes[2] = 1
        p = self._p(3, modes)
        self._ptr += 3
        self._mem[p[2]] = int(p[0] < p[1])
        return True

    def _equals(self, modes: List[int]) -> bool:
        modes[2] = 1
        p = self._p(3, modes)
        self._ptr += 3
        self._mem[p[2]] = int(p[0] == p[1])
        return True
