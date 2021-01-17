import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = 0
for i in range(N):
	s+=a[i]*b[i]

if s==0:
	print("Yes")
else:
	print("No")
