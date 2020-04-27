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
    m=int(task_input.readline().strip())
    username=task_input.readline().strip().split(' ')
    ns=[int(i) for i in task_input.readline().strip().split(' ')]
    content_length={}
    like_receive = {}
    like_give = {}
    for user in username:
        content_length[user]=[]
        like_give[user]=0
        like_receive[user]=0
    i=0
    while i<m:
        user=username[i]
        for jj in range(ns[i]):
            content=task_input.readline().strip().split(' ')
            clen=len(content)
            content_length[user].append(clen)
            likes=task_input.readline().strip().split(' ')
            for u in likes:
                if u!=user:
                    like_receive[user]+=1
                like_give[u]+=1
        i+=1
    for us in content_length:
        content_length[us]=sum(content_length[us])/len(content_length[us])
    fred_coef=[]
    for user in username:
        fco=content_length[user]*like_receive[user]/(like_give[user]+1)
        fred_coef.append((-fco,user))
    fred_coef.sort()
    #print(fred_coef)
    popular=fred_coef[0][1]
    outputs.append(popular)


def evaluate(num, stream):
    correct_output = outputs[num-1]
    output = stream.str()
    stream.end()
    if output == correct_output:
        return 1.0
    else:
        return 0.0


parser = Parser(evaluate, T, human_output, int_max_len=20, strict_spaces=False)

print(json.dumps(parser.run()))
