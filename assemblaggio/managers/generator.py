#!/usr/bin/env python3

#
# Generatore LuissMatics 2020
# Task n.4 "Assemblaggio"
# Michele Lizzit
#


import random

MAXT = 20
MAXN = 10000

ns=[2,3,4,8,16,32,64,128,256,512,1024,2048,4096,4500,5000,6000,7000,8000,9000,10000]

#T = random.randint(1,MAXT + 1)
T = MAXT

def genDNA():
	res = ""
	for i in range(random.randint(2,20)):
		res += random.choice(['A', 'T', 'G', 'C'])
	return res

print(T)

for t in range(T):
	N = ns[t]
	print(N)
	for n in range(N):
		print(genDNA())

