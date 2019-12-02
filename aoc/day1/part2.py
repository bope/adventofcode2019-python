from typing import List


def fuel_by_mass(mass: int) -> int:
    fuel = max((mass // 3) - 2, 0)
    if fuel > 0:
        fuel += fuel_by_mass(fuel)
    return fuel


def solution(input: List[int]) -> int:
    return sum(fuel_by_mass(i) for i in input)


def parse_input(input: str) -> List[int]:
    return list(map(int, input.split()))


if __name__ == '__main__':
    with open('inputs/day1.txt') as fd:
        print(solution(parse_input(fd.read())))
