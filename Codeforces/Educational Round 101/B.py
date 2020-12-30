def partial_sum(arr):
	temp=0;ans=0
	for i in range(0,len(arr)):
		temp+=arr[i]
		if temp > ans:
			ans = temp	

	return ans

N = int(input())

for n in range(N):
	red = int(input())
	r = list(map(int, input().split()))
	blue = int(input())
	b = list(map(int, input().split()))

	print(partial_sum(r)+partial_sum(b))