from typing import List



def solution(input: List[int]) -> List[int]:
    i = iter(input)

    while True:
        op = next(i)
        if op == 99:
            break

        a = next(i)
        b = next(i)
        pos = next(i)

        if op == 1:
            input[pos] = input[a] + input[b]
        elif op == 2:
            input[pos] = input[a] * input[b]

        else:
            raise Exception(f'invalid opcode: {op}')


    return input


def parse_input(input: str) -> List[int]:
    return list(map(int, input.split(',')))



if __name__ == '__main__':
    with open('inputs/day2.txt') as fd:
        input = parse_input(fd.read())
        input[1] = 12
        input[2] = 2
        result = solution(input)
        print(result[0])
