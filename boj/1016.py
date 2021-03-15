import math

a, b = map(int,input().split())
result = [1]*(b-a+1)
cnt = b-a+1
n = 2

while n**2 <= b:
    p = a//(n**2)
    if a%(n**2) != 0:
        p += 1
    
    while p*(n**2) <= b:
        result[p*(n**2)-a] = 0
        p+=1
    n+=1
print(sum(result))

# 1~1000 소수 리스트 만들기
# 소수 리스트 제곱시키기
