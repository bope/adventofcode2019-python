#!/usr/bin/env python
import sys
from importlib import import_module

days = sys.argv[1:]
if not days:
    days = ['day{}'.format(i) for i in range(1, 9)]

for day in days:
    print('#', day)
    print('part1')
    p1 = import_module(f'aoc.{day}.part1')
    p1.main()
    print('part2')
    p2 = import_module(f'aoc.{day}.part2')
    p2.main()
    print()
