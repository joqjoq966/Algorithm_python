import sys
input = sys.stdin.readline

a,b = map(int,input().split())

if abs(a-b)>=3:
	print("No")
else:
	print("Yes")
