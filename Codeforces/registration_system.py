import sys
input = sys.stdin.readline

t =int(input())
reg_dict = dict()
for _ in range(t):
    s = input().rstrip()
    if s in reg_dict.keys():
        print(s+str(reg_dict[s]))
        reg_dict[s]+=1
    if s not in reg_dict.keys():
        reg_dict[s] = 1
        print('OK')

