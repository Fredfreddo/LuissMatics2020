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
    N = int(task_input.readline().strip())
    x = " ".join([task_input.readline().strip() for _ in range(N)])
    x = x.strip()
    x = x.split(" ")
    x = [int(y) for y in x]
    people = x
    people = [int(x) for x in people]
    people = [x for x in zip(*(iter(people),) * 2)]
    Z = int(task_input.readline().strip())
    infected = " ".join([task_input.readline().strip() for _ in range(Z)])
    infected = infected.strip().split(" ")
    infected = [int(x) for x in infected]
    infected = [x for x in zip(*(iter(infected),) * 3)]
    D = int(task_input.readline().strip())
    
    max_score = -1
    res = -1
    for p in people:
        score = 0
        for inf in infected:
            if (p[0] - inf[0])**2 + (p[1] - inf[1])**2 <= D**2:
                score += inf[2]
        if score >= max_score:
            res = p
            max_score = score
    finalres = (people.index(res)+1)
    outputs.append(finalres)


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
