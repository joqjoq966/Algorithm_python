import sys
input = sys.stdin.readline

def expressions(num):
 
    return len([i  for i in range(1,num+1,2) if num % i == 0])
n = int(input())
ans = expressions(n)

print(2*ans)