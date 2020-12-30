import math

t = int(input())
for i in range(t):
	n = int(input())
	trees = list(map(int,input().split()))
	diff = set()
	for i in trees:
		for j in trees:
			if i!=j:
				diff.add(abs(i-j))
	print(len(diff))