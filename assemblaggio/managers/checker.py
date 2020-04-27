#!/usr/bin/env python3

from itertools import accumulate
from parser import Parser
from sys import argv, exit, stderr
import json

if len(argv) != 3:
    print("Usage: %s input_file output_file" % argv[0], file=stderr)
    exit(1)


def check(a, b, shift):
        if shift >= len(b):
                return a
        ia = 0
        ib = shift
        while a[ia] == b[ib]:
                ia+=1;
                ib+=1;
                if ib >= len(b):
                        return a[ia:]
                if ia >= len(a):
                        return ""
        return False


task_input = open(argv[1], "r")
human_output = open(argv[2], "r")

# reading input file and generating correct output
T = int(task_input.readline())

outputs = []
for _ in range(T):
    # Solve
    N = int(task_input.readline().strip())
    s = []
    for _ in range(N):
            s.append(task_input.readline().strip())
    sol = s[0]
    start = 0
    for e in s:
            while check(e, sol, start) == False:
                    start += 1
            sol += check(e,sol, start)
            start += 1
    res = len(sol)
    outputs.append(res)


def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = stream.int()
    stream.end()
    if output == correct_output:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))
