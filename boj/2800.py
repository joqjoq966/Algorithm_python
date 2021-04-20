import sys
input = sys.stdin.readline
from itertools import combinations

equation = list(input().rstrip())
bracket = []
num_op = []
br_stack = []

for i in range(len(equation)):
    if equation[i] == "(":
        br_stack.append(i)
    elif equation[i] == ")":
        bracket.append((br_stack.pop(), i))
    else:
        num_op.append(i)

ans = set()

for i in range(1, len(bracket)+1):
    for j in combinations(bracket, i):
        eq = equation[:]
        for l, r in j:
            eq[l] = ''
            eq[r] = ''
        ans.add(''.join(eq))
ans = sorted(ans)
for i in ans:
    print(i)
