
from collections import Counter


def solution(input: str, size=(25, 6)) -> int:
    layer_size = size[0] * size[1]
    steps = range(0, len(input) + 1, layer_size)
    layers = [input[s:e] for s, e in zip(steps, steps[1:])]
    layer = sorted(layers, key=lambda x: Counter(x)['0'])[0]
    lc = Counter(layer)
    return lc['1'] * lc['2']


def main():
    with open('inputs/day8.txt') as fd:
        print(solution(fd.read().strip()))
