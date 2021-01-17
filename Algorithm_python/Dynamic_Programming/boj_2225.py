import sys
input = sys.stdin.readline

N,K = map(int,input().split())

combi = [[1],[1,1]]

for i in range(2,N+K):
	temp = [1]
	for j in range(len(combi[i-1])-1):
		temp.append((combi[i-1][j]+combi[i-1][j+1])%(10**9))
	temp.append(1)
	combi.append(temp)
	temp.clear

print(combi[N+K-1][N])
