#!/usr/bin/env python3

def check(a, b, shift):
	if shift >= len(b):
		return a
	ia = 0
	ib = shift
	while a[ia] == b[ib]:
		ia+=1;
		ib+=1;
		if ib >= len(b):
			return a[ia:]
		if ia >= len(a):
			return ""
	return False

T = int(input())

for t in range(T):
	N = int(input())
	s = []
	for _ in range(N):
		s.append(input())
	sol = s[0]
	start = 0
	for e in s:
		while check(e, sol, start) == False:
			start += 1
		sol += check(e,sol, start)
		start += 1
	tt = t+1
	#print(s)
	#print(sol)
	res = len(sol)
	print(f"Case #{tt}: {res}")
