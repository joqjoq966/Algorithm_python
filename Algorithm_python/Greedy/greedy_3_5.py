def combination(n):
	return int(n*(n-1)/2)

N, M = map(int, input().split())
balls = list(map(int,input().split()))

#전체 가능한 조합의 수
ans = combination(N)

# 1~max(가장 무거운 공의 무게)중 같은 무게의 공이 여러개 존재하면, 같은 무게를 가진 공 개수의 조합만큼 빼준다.
for i in range(1,max(balls)+1):
	if balls.count(i)>=2:
		ans -= combination(balls.count(i))

print(ans)