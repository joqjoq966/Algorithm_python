import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

val = 0
max_a =0
max_b=0
for i in range(n):
	max_a = max(a[i],max_a)
	val = max(val, max_a*b[i])
	print(val)




