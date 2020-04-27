#!/usr/bin/env python3

#
# solution 
# task 'covid'
# Fangqing Yuan
#

t=int(input())
for kkk in range(t):
	n=int(input())
	people=[]
	for i in range(n):
		coo=[int(i) for i in input().split(' ')]
		people.append(coo)
	p=int(input())
	points=[]
	for i in range(p):
		coos=[int(i) for i in input().split(' ')]
		points.append(coos)
	d=int(input())
	D=d**2
	counts=[]
	index=1
	for person in people:
		count=0
		for point in points:
			distance=(person[0]-point[0])**2+(person[1]-point[1])**2
			if distance<=D:
				count+=point[2]
		counts.append((-count,index))
		index+=1
	counts.sort()
	solution=counts[0][1]
	print('Case #{}: {}'.format(kkk+1,solution))
			
	
