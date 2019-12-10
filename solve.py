#!/usr/bin/env python
import sys
from importlib import import_module

days = sys.argv[1:]
if not days:
    days = ['day{}'.format(i) for i in range(1, 11)]

for day in days:
    print('#', day)
    p1 = import_module(f'aoc.{day}.part1')
    print('part1')
    p1.main()

    try:
        p2 = import_module(f'aoc.{day}.part2')
        print('part2')
        p2.main()
        print()
    except ModuleNotFoundError:
        pass
