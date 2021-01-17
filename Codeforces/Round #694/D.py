import math
def solution(n,arr,query,q):
	temp = [0]*n
	ans = 0
	for i in range(n):
		temp[i]=arr[i]
	cnt= 1
	while q>=1:
		for i in range(n):
			cnt=1
			for j in range(i+1,n):
				if arr[i]>=arr[j]:
					val = arr[i]/arr[j]
				else:
					val = arr[j]/arr[i]
				if math.ceil(math.sqrt(val))==math.sqrt(val):
					cnt+=1
					temp[i]*=arr[j]
					temp[j]*=arr[i]
			ans = max(ans,cnt)
		
		for i in range(n):
			arr[i]=temp[i]
		q-=1
	return ans

t = int(input())
for i in range(t):
	n = int(input())
	arr = list(map(int,input().split()))
	query = int(input())
	q = int(input())
	print(solution(n,arr,query,q+1))
	
	