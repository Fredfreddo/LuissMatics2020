#!/usr/bin/env python3

#
# Soluzione LuissMatics 2020
# Task n.2 "COVID-19"
# Michele Lizzit
#

T = int(input())
for t in range(T):
	N = int(input())
	x = " ".join([input() for _ in range(N)])
	x = x.strip()
	x = x.split(" ")
	x = [int(y) for y in x]
	people = x
	people = [int(x) for x in people]
	people = [x for x in zip(*(iter(people),) * 2)]
	Z = int(input())
	infected = " ".join([input() for _ in range(Z)])
	infected = infected.strip().split(" ")
	infected = [int(x) for x in infected]
	infected = [x for x in zip(*(iter(infected),) * 3)]
	D = int(input())
	
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
	case = t+1
	print(f"Case #{case}: {finalres}")
