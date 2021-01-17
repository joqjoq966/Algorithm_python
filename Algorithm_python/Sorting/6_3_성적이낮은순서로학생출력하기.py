N = int(input())
arr = [0]*N
for i in range(N):
	name,score = input().split()
	arr[i] = (name,int(score))

ans = sorted(arr,key = lambda x: x[1])
for i in ans:
	print(i[0],end=' ')