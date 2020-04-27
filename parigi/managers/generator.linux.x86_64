#!/usr/bin/env python3

#
# Generatore LuissMatics 2020
# Task n.1 "Parigi"
# Michele Lizzit
#

import string
import random
import time
from datetime import datetime,timedelta

MAXT = 20
MAXN = 100

T = 10
#T = random.randint(1, MAXT+1)

print(T)

for t in range(T):
	N = random.randint(50,MAXN)
	if t == 0:
		N = 5
	elif t == 1:
		N = 10
	elif t == 2:
		N = 15
	elif t == 3:
		N = 20
	elif t == 4:
		N = 25
	print(N)
	d = datetime.fromtimestamp(1549756800)

	monList = []
	for n in range(random.randint(20,MAXN)):
		mon = ''.join([random.choice(string.ascii_letters)] + [random.choice(string.ascii_letters + " ") for _ in range(8)] + [random.choice(string.ascii_letters)])
		monList.append(mon)

	for n in range(N):
		d = d + timedelta(random.randint(0,7), 0)
		s = d.strftime("%Y-%m-%d")
		m = random.choice(monList)
		print(f"{s} {m}")
