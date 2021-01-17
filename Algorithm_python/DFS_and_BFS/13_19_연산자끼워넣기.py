import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations
import copy

N = int(input())
numbers = deque(map(int,input().split()))
operation = list(map(int,input().split()))

op = []
temp = ["+","-","*","/"]
for i in range(4):
	op+=operation[i]*temp[i]

perm = permutations(op,len(op))

max_ans = -sys.maxsize
min_ans = sys.maxsize

for p in perm:
	data = deque([i for i in numbers])
	temp = data.popleft()
	for i in range(1,N):
		if p[i-1]=="+":
			temp+=data.popleft()
		if p[i-1]=="-":
			temp-=data.popleft()
		if p[i-1]=="*":
			temp*=data.popleft()
		if p[i-1]=="/":
			if temp<0:
				temp = (-temp)//data.popleft()
				temp *= -1
			else:
				temp//=data.popleft()
	# print("temp ",temp)
	min_ans = min(min_ans,temp)
	max_ans = max(max_ans,temp)
		
print(max_ans)
print(min_ans)