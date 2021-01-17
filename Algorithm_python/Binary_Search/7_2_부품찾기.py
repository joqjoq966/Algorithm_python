import sys
input = sys.stdin.readline

def binary_search(arr,target,start,end):
	while start<=end:
		mid = (start+end)//2

		if arr[mid]==target:
			return "yes"
		elif target < arr[mid]:
			end = mid-1
		else:
			start = mid+1
	return "no"

N = int(input())
have = list(map(int,input().split()))
M = int(input())
need = list(map(int,input().split()))

have.sort()
for item in need:
	result = binary_search(have,item,0,N-1)
	print(result)