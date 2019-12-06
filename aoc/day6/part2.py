from typing import List, Tuple, Optional
from dataclasses import dataclass
from functools import reduce


@dataclass
class Node:
    name: str
    parent: Optional['Node'] = None
    children: List['Node'] = None

    def depth(self) -> int:
        c = self
        d = 0
        while (c:=c.parent) != None:
            d += 1
        return d

    def path(self) -> int:
        c = self
        while (c:=c.parent) != None:
            yield c.name


def solution(input: List[Tuple[str, str]]) -> int:
    nodes = {}
    for (parent, child) in input:
        if parent not in nodes:
            nodes[parent] = Node(parent)

        if child not in nodes:
            nodes[child] = Node(child)

        nodes[child].parent = nodes[parent]

    me = nodes['YOU']
    santa = nodes['SAN']

    me_path = list(me.path())
    santa_path = list(santa.path())
    steps = len(me_path) + len(santa_path)

    for a, b in zip(reversed(me_path), reversed(santa_path)):
        if a != b:
            break
        steps -= 2

    return steps


def parse_input(input: str) -> List[Tuple[str, str]]:
    return [tuple(p.split(')')) for p in input.split('\n')]


if __name__ == '__main__':
    with open('inputs/day6.txt') as fd:
        print(solution(parse_input(fd.read().strip())))
