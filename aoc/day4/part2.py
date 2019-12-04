
def is_valid(num: int) -> bool:
    password = str(num)
    
    if len(password) != 6:
        return False

    found = False
    adj = 0
    for a, b in zip(password, password[1:]):
        if int(a) > int(b):
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
    valid = 0
    for num in range(min_val, max_val + 1):
        if is_valid(num):
            valid += 1
    return valid


if __name__ == '__main__':
    with open('inputs/day4.txt') as fd:
        print(solution(*map(int, fd.read().strip().split('-'))))
