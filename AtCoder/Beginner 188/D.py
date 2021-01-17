import sys
input = sys.stdin.readline

N,C = map(int,input().split())
plan = []
for i in range(N):
	a,b,c = map(int,input().split())
	plan.append((a,b,c))
plan.sort()

first_day = 10**9
last_day = 0

for p in plan:
	if first_day > p[0]:
		first_day = p[0]
	if last_day < p[1]:
		last_day = p[1]

total_day = last_day - first_day +1
pay = [0]*total_day

for p in plan:
	for i in range(first_day,last_day+1):
		

for p in range(len(pay)):
	if pay[p] > C:
		pay[p] = C
print(pay)
print(sum(pay))
	