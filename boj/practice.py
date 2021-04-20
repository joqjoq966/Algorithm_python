import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    # 가로길이 M, 세로길이 N, 배추개수 K
    M, N, K = map(int, input().split())
    # 배추밭 만들기
    cab = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        cab[c][r] = 1

    # 델타 상, 좌
    dr = [-1, 0,1,0]
    dc = [0, -1,0,1]

    worm = 0
    for i in range(N):
        for j in range(M):
            if cab[i][j]:
                worm += 1
                for d in range(4):
                    row = i + dr[d]
                    col = j + dc[d]
                    if row == -1 or col == -1 or row >= N or col >= M:
                        continue
                    if cab[row][col]:
                        worm -= 1
                        cab[row][col]=0
                        break
    print(worm)