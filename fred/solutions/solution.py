#!/usr/bin/env python3

#
# Soluzione LuissMatics 2020
# Task n.3 "Fred"
# Fangqing Yuan
#
solution=[]
t=int(input())
for i in range(t):
    m=int(input())
    username=input().split(' ')
    ns=[int(i) for i in input().split(' ')]
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
            content=input().split(' ')
            clen=len(content)
            content_length[user].append(clen)
            likes=input().split(' ')
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
    solution.append(popular)
i=0
while i<len(solution):
    print('Case #{}: '.format(i+1)+solution[i])
    i+=1
