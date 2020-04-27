#!/usr/bin/env python3

from itertools import accumulate
from parser import Parser
from sys import argv, exit, stderr
import json

if len(argv) != 3:
    print("Usage: %s input_file output_file" % argv[0], file=stderr)
    exit(1)

task_input = open(argv[1], "r")
human_output = open(argv[2], "r")

# reading input file and generating correct output
T = int(task_input.readline())

outputs = []
for _ in range(T):
    # Solve
    N = int(task_input.readline())
    visited = set()
    res = 0
    for n in range(N):
        mon = task_input.readline().strip().split(" ")
        mon = " ".join(mon[1:])
        if mon not in visited:
            res += 1
            visited.add(mon)
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
