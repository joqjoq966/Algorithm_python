def permutation(cnt):
    if cnt==m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return 
    
    for i in range(1,n+1):
        if visit[i] == False:
            visit[i] = True
            arr[cnt] = i
            permutation(cnt+1)
            visit[i] = False


n, m = map(int, input().split())
visit = [False]*(n+1)
arr = [0]*9
permutation(0)