import sys 
input = sys.stdin.readline

def prime(num):
    a = [False, False] + [True]*(num)
    p = []

    for i in range(2, num+1):
        if a[i]:
            p.append(i)
            for j in range(2*i, num+1, i):
                a[j] = False
    return p

def solve(n,k):
    ans = 1
    p = prime(3200)
    square_list = [ i**2 for i in p ]
    square_list = square_list[::-1]
    # print(square_list)
    for i in range(n):
        for j in square_list:
            if arr[i]%j == 0:
                arr[i] //= j
    # print(arr)
    s = set()
    for i in arr:
        if i not in s:
            s.add(i)
        else:
            ans += 1
            s = set([i])
    return ans

t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solve(n,k))
