N = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse = True)

i=0; answer=0

while i < N:
	if i+arr[i]>N:
		i+=1
	else:
		i+=arr[i]
		if(i<=N):
			answer+=1

print(answer)

# 배열의 마지막 처리 생각하는 것이 관건