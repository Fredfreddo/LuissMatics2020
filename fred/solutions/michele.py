#!/usr/bin/env python3

#
# LuissMatics 2020
# Solution to "fred"
# Michele Lizzit
#

T = int(input())

for t in range(T):
	M = int(input())
	u = input().strip().split(" ")
	np = [int(x) for x in input().strip().split(" ")]
	p = []
	l = []
	like_per_user = {}
	for tmp in u:
		like_per_user[tmp] = 0
	for nnp in np:
		p.append([])
		l.append([])
		for _ in range(nnp):
			p[-1].append(input())
			l[-1].append(input())
			for tmp in l[-1][-1].split(" "):
				like_per_user[tmp] += 1

	max_coef = -1
	max_user = None
	for u_posts, u_likes, u_name in zip(p, l, u):
		ws = 0
		wn = 0
		for post in u_posts:
			wn += 1
			ws += len(post.split(" "))
		la = 0
		for like in u_likes:
			like = like.split(" ")
			try:
				like.remove(u_name)
			except ValueError:
				pass
			la += len(like)
		wavg = ws/wn
		coef = (wavg*la)/(like_per_user[u_name]+1)
		if (coef > max_coef) or ((coef == max_coef) and (u_name < max_user)):
			max_coef = coef
			max_user = u_name
	print(f"Case #{t+1}: {max_user}")
