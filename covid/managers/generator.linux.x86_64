#!/usr/bin/env python3

import random

#
# Generatore LuissMatics 2020
# Task n.2 "COVID-19"
# Michele Lizzit
#


MAXN = 100
MAXT = 20
MAXL = 100
MAXD = 10
MAXI = 10
MAXZ = 100

T = random.randint(1,MAXT + 1)
T = 10
print(T)

for t in range(T):
	N = random.randint(1,MAXN)
	print(N)
	curmaxL = MAXL
	curmaxD = MAXD
	curmaxZ = MAXZ
	curmaxI = MAXI

	if T == 0:
		N = 5
		curmaxL = 10
		curmaxD = 5
		curmaxZ = 10
		curmaxI = 5
	elif T == 1:
		N = 10
		curmaxL = 20
		curmaxD = 5
		curmaxZ = 10
		curmaxI = 5
	elif T == 2:
		N = 20
		curmaxL = 30
		curmaxD = 5
		curmaxZ = 10
		curmaxI = 5
	r = []
	for n in range(N):
		a = random.randint(0,curmaxL)
		r.append(a)
		a = random.randint(0,curmaxL)
		r.append(a)
		print(f"{r[-2]} {r[-1]}")
	#print(" ".join([str(x) for x in r]))

	r = []
	Z = random.randint(1,curmaxZ)
	print(Z)
	for n in range(Z):
		a = random.randint(0,curmaxL)
		r.append(a)
		a = random.randint(0,curmaxL)
		r.append(a)
		inf = random.randint(0,curmaxI)
		r.append(inf)
		print(f"{r[-3]} {r[-2]} {r[-1]}")
	#print(" ".join([str(x) for x in r]))

	D = random.randint(1,curmaxD)
	print(D)
