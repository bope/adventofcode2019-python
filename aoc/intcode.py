from typing import List, Optional, Tuple
from collections import deque
from dataclasses import dataclass


class Mem(list):
    def resolve_ptr(self, mode: int, ptr: int, rptr: int) -> int:
        if mode == 0:
            ptr = self[ptr]
        elif mode == 1:
            ptr = ptr
        elif mode == 2:
            ptr = self[ptr] + rptr
        else:
            raise Exception(f'unknown mode: {mode}')

        return ptr

    def check_mem(self, ptr: int) -> None:
        if ptr < 0:
            raise Exception(f'negative pointer: f{ptr}')

        if ptr >= len(self):
            self += [0] * ((ptr + 1) - len(self))

    def get(self, mode: int, ptr: int, rptr: int) -> int:
        ptr = self.resolve_ptr(mode, ptr, rptr)
        self.check_mem(ptr)
        return Addr(self, mode, ptr)


@dataclass
class Addr:
    mem: Mem
    mode: int
    ptr: int

    def read(self) -> int:
        return self.mem[self.ptr]

    def write(self, value: int):
        if self.mode == 1:
            raise Exception(f'immediate write: {self.ptr}: {value}')
        self.mem[self.ptr] = value


class Emulator:
    def __init__(self, program: List[int], input: Optional[deque] = None, output: Optional[deque] = None):
        self.mem = Mem(program)
        self.input = input
        self.ptr = 0
        self.rptr = 0
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
            9: self._rel_base_offset,
        }

    def _p(self, count: int, modes: List[int]) -> List[Addr]:
        return [self.mem.get(modes[i], self.ptr + i, self.rptr) for i in range(count)]

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
            if not self.step():
                return

    def step(self) -> bool:
        op, modes = self._parse_instruction(
            self.mem.get(1, self.ptr, self.rptr).read()
        )
        self.ptr += 1

        if op not in self._op_funcs:
            raise Exception(f'invalid opcode: {op}')

        return self._op_funcs[op](modes)

    def _break(self, modes: List[int]) -> bool:
        self.stopped = True
        return False

    def _add(self, modes: List[int]) -> bool:
        p = self._p(3, modes)
        self.ptr += 3
        p[2].write(p[0].read() + p[1].read())
        return True

    def _mul(self, modes: List[int]) -> bool:
        p = self._p(3, modes)
        self.ptr += 3
        p[2].write(p[0].read() * p[1].read())
        return True

    def _input(self, modes: List[int]) -> bool:
        try:
            input = self.input.popleft()
        except IndexError:
            self.ptr -= 1
            return False

        p = self._p(1, modes)
        self.ptr += 1
        p[0].write(input)
        return True

    def _output(self, modes: List[int]) -> bool:
        p = self._p(1, modes)
        self.ptr += 1
        self.output.append(p[0].read())
        return True

    def _jumptrue(self, modes: List[int]) -> bool:
        p = self._p(2, modes)
        self.ptr += 2
        if p[0].read() != 0:
            self.ptr = p[1].read()
        return True

    def _jumpfalse(self, modes: List[int]) -> bool:
        p = self._p(2, modes)
        self.ptr += 2
        if p[0].read() == 0:
            self.ptr = p[1].read()
        return True

    def _lessthan(self, modes: List[int]) -> bool:
        p = self._p(3, modes)
        self.ptr += 3
        p[2].write(int(p[0].read() < p[1].read()))
        return True

    def _equals(self, modes: List[int]) -> bool:
        p = self._p(3, modes)
        self.ptr += 3
        p[2].write(int(p[0].read() == p[1].read()))
        return True

    def _rel_base_offset(self, modes: List[int]) -> bool:
        p = self._p(1, modes)
        self.ptr += 1
        self.rptr += p[0].read()
        return True
