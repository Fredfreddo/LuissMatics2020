#!/usr/bin/env python3

#
# Soluzione LuissMatics 2020
# Task n.1 "Parigi"
# Michele Lizzit
#

T = int(input())

for t in range(T):
	N = int(input())
	visited = set()
	res = 0
	for n in range(N):
		mon = input().split(" ")
		mon = " ".join(mon[1:])
		if mon not in visited:
			res += 1
			visited.add(mon)
	case = t+1
	print(f"Case #{case}: {res}")
