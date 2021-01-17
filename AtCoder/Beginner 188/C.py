import sys
import copy
input = sys.stdin.readline

def fight(arr):
	res = []
	for i in range(0,len(arr),2):
		if arr[i]>arr[i+1]:
			res.append(arr[i])
		else:
			res.append(arr[i+1])			
	return res

N = int(input())
a = list(map(int,input().split()))
temp = copy.copy(a)

while len(temp)>2:
	temp = fight(temp)
temp.sort()
print(a.index(temp[0])+1)

