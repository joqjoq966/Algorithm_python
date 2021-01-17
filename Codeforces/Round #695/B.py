def get_hills(n,arr):
	hill = 0
	for i in range(1,n-1):
		if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
			hill+=1
	return hill

def get_valleys(n,arr):
	valley=0
	for i in range(1,n-1):
		if arr[i]<arr[i+1] and arr[i]<arr[i-1]:
			valley+=1
	return valley

def solution(n,arr):
	ans = get_hills(n,arr)+get_valleys(n,arr)
	
	for i in range(1,n-1):
		if arr[i]>arr[i+1] and arr[i]>arr[i-1]:

	return ans
	
	
t = int(input())
for i in range(t):
	n = int(input())
	arr = list(map(int,input().split()))
	print(solution(n,arr))