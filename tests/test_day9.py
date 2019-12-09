from aoc.day9 import part1


def test_part1():
    t1i = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    e = part1.solution(part1.parse(t1i))
    assert ','.join(map(str, e.output)) == t1i

    t2i = "1102,34915192,34915192,7,4,7,99,0"
    e = part1.solution(part1.parse(t2i))
    assert len(str(e.output.pop())) == 16

    t2i = "104,1125899906842624,99"
    e = part1.solution(part1.parse(t2i))
    assert e.output.pop() == 1125899906842624
