#!/usr/bin/env python3

#
# Soluzione LuissMatics 2020
# Task n.4 "Assemblaggio"
# Fangqing Yuan
#

solution=[]
t=int(input())
for i in range(t):
    n=int(input())
    start=input()
    dna=start
    i=2
    point=0
    while i<=n:
        nextline=input()
        #print(nextline)
        p=len(nextline)
        if dna[point+1:].find(nextline)!=-1:
            point=dna[point+1:].find(nextline)+point+1
            if point+p-1>len(dna)-1:
                dna=dna[:point]+nextline
            #print(point)
        else:
            while p>=1:
                if nextline[:p]==dna[-p:] and len(dna)-p>point:
                    point=len(dna)-p
                    dna=dna+nextline[p:]
                    break
                else: p-=1
            if p==0: 
                point=len(dna)
                dna=dna+nextline
            #print(p)
        #print(dna)
        i+=1
    solution.append(len(dna))
#print(solution)
i = 0
while i < len(solution):
    print('Case #{}: '.format(i + 1) + str(solution[i]))
    i += 1
