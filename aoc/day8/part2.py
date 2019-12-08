from typing import List
from collections import Counter, defaultdict


def solution(input: List[str], size=(25, 6)) -> str:
    layer_size = size[0] * size[1]
    layers = len(input) // layer_size
    ret = [2] * layer_size

    for l in range(layers, 0, -1):
        end = l * layer_size
        start = end - layer_size

        for i, pixel in enumerate(input[start:end]):
            if pixel != 2:
                ret[i] = pixel

    return '\n'.join([''.join([str(i) for i in row]) for row in [ret[r*size[0]:(r+1)*size[0]] for r in range(size[1])]])


if __name__ == '__main__':
    with open('inputs/day8.txt') as fd:
        ret = solution(list(map(int, fd.read().strip())))
        ret = ret.replace('2', ' ').replace('0', '.').replace('1', 'X')
        print(ret)
