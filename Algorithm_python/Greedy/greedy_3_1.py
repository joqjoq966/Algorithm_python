N = map(int, input().split())
arr = list(map(int,input().split()))

arr.sort(reverse = True)

i=0; answer=0
while i < len(arr):
	i+=arr[i]
	if(i<=len(arr)):
		answer+=1

print(answer)
