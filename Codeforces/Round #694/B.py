def solution(n,x,arr):
	i=0; ans = 0
	temp = 1
	while True:
		if arr[i]%temp==0:
			ans +=arr[i]
			i=(i+1)%n
			if i==0:
				temp*=x
		else:
			break
	return ans

t = int(input())
for i in range(t):
	n,x = map(int,input().split())
	arr = list(map(int,input().split()))
	print(solution(n,x,arr))
	
	