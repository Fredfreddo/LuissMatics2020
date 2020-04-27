#!/usr/bin/env python3

#
# Generatore LuissMatics 2020
# Task n.3 "Fred"
# Fangqing Yuan
#

import string
import random
#import names
alphau=list(string.ascii_uppercase)
alphal=list(string.ascii_lowercase)
wordlist=['Hi','Hello','Bye','Ciao','Luiss','Good','Roma','False', 'None', 'True', 'and', 'as', 'assert', 'apple', 'await', 'break', 'class', 'continue', 'Coronavirus','define', 'dad', 'extra', 'else', 'except', 'finally', 'for', 'from', 'global', 'hope','if', 'import', 'in', 'is', 'just','keep','lambda', 'love','like','no', 'not', 'or', 'open','pass', 'quit','raise', 'return','sun','son', 'try','use','video', 'while', 'with','xray', 'yield','yes','zoo']

t=20
print('{}'.format(str(t)))
contlenmax=[3,3,3,5,5,5,8,8,8,13,13,13,21,21,21,44,44,44,50,50]
ms=[2,3,4,5,6,7,8,9,10,random.randint(11,13),random.randint(14,16),random.randint(17,20),random.randint(21,25),random.randint(26,30),random.randint(31,36),random.randint(37,42),random.randint(43,49),random.randint(50,60),random.randint(61,80),random.randint(81,100)]
for j in range(t):
    m = ms[j]
    #print(m)
    username = []
    for i in range(m):
        user = ''
        user += random.choice(alphau)
        user += random.choice(alphal)
        user += random.choice(alphal)
        user += random.choice(alphal)
        user += random.choice(alphal)
        username.append(user)
    username.sort()
    i=1
    while i<len(username):
        while username[i]==username[i-1]:
            user = ''
            user += random.choice(alphau)
            user += random.choice(alphal)
            user += random.choice(alphal)
            user += random.choice(alphal)
            user += random.choice(alphal)
            username[i]=user
        i+=1
    print('{}'.format(str(m)))
    line2=" ".join(i for i in username)
    print(line2)
    ns=[]
    for i in range(m):
        ns.append(random.randint(1,min(m,10)))
    line3 = " ".join(str(i) for i in ns)
    print(line3)
    i=0
    while i < m:
        jj=ns[i]
        for k in range(jj):
            content_length=random.randint(1,contlenmax[j])
            content=''
            for c in range(content_length):
                content+=random.choice(wordlist)+' '
            content=content[:-1]
            print(content)
            like_number=random.randint(1,m)
            likes=random.sample(username,k=like_number)
            linex = " ".join(str(i) for i in likes)
            print(linex)
        i+=1

