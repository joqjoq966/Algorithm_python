def solution(n,x,friends,presents):
	friends.sort(reverse=True)
	ans = 0; cnt=0
	visited = [False]*n
	for f in friends:
		if cnt<f and visited[cnt]==False:
			ans += presents[cnt]
			visited[cnt] = True
			cnt += 1
		else:
			ans+=presents[f-1]
	return ans

t = int(input())
for i in range(t):
	n,x = map(int,input().split())
	friends = list(map(int,input().split()))
	presents = list(map(int,input().split()))
	
	print(solution(n,x,friends,presents))
	
	