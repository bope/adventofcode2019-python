from typing import List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Node:
    parent: Optional['Node'] = None
    children: List['Node'] = None

    def depth(self) -> int:
        c = self
        d = 0
        while (c:=c.parent) != None:
            d += 1
        return d


def solution(input: List[Tuple[str, str]]) -> int:
    nodes = {}
    for (parent, child) in input:
        if parent not in nodes:
            nodes[parent] = Node()

        if child not in nodes:
            nodes[child] = Node()

        nodes[child].parent = nodes[parent]

    return sum(n.depth() for n in nodes.values())


def parse_input(input: str) -> List[Tuple[str, str]]:
    return [tuple(p.split(')')) for p in input.split('\n')]


def main():
    with open('inputs/day6.txt') as fd:
        print(solution(parse_input(fd.read().strip())))
