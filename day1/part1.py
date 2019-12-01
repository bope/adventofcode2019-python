from typing import List


def solution(input: List[int]) -> int:
    return sum((i // 3) - 2 for i in input)


def parse_input(input: str) -> List[int]:
    return list(map(int, input.split()))


if __name__ == '__main__':
    with open('input.txt') as fd:
        print(solution(parse_input(fd.read())))
