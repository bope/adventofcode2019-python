from typing import List
from collections import Counter, defaultdict


def solution(input: str, size=(25, 6)) -> str:
    layer_size = size[0] * size[1]
    layers = len(input) // layer_size
    ret = ''

    for y in range(size[1]):
        for x in range(size[0]):
            p = '2'
            for l in range(layers-1, -1, -1):
                lp = input[(layer_size * l) + (size[0] * y) + x]
                if lp != '2':
                    p = lp
            ret += p
        ret += '\n'
    return ret.strip()


def main():
    with open('inputs/day8.txt') as fd:
        ret = solution(fd.read().strip())
        ret = ret.replace('2', ' ').replace('0', '.').replace('1', 'X')
        print(ret)
