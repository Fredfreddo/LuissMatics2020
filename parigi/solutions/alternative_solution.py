#!/usr/bin/env python3

#
# S LuissMatics 2020
# Task n.1 "Parigi"
# Fangqing Yuan
#
t=int(input())
solution=[]
for i in range(t):
    n=int(input())
    places=[]
    for j in range(n):
        places.append(input()[11:])
    count=[]
    for p in places:
        if p not in count:
            count.append(p)
    solution.append(len(count))
i = 0
while i < len(solution):
    print('Case #{}: '.format(i + 1) + str(solution[i]))
    i += 1

