def is_valid(num: int) -> bool:
    password = str(num)
    
    if len(password) != 6:
        return False

    found = False
    adj = 0
    for a, b in zip(password, password[1:]):
        if a > b:
            return False

        if a == b:
            adj += 1
        else:
            if adj == 1:
                found = True
            adj = 0
    if adj == 1:
        found = True
    return found


def solution(min_val: int, max_val: int) -> int:
    return sum(map(is_valid, range(min_val, max_val + 1)))


# minified
from collections import Counter

def small(min_val, max_val):
    return sum(map(lambda n: len(str(n)) == 6 and str(n) == ''.join(sorted(str(n))) and any(i == 2 for i in Counter(str(n)).values()), range(min_val, max_val + 1)))

if __name__ == '__main__':
    with open('inputs/day4.txt') as fd:
        print(solution(*map(int, fd.read().strip().split('-'))))

