import sys
s = sys.stdin.readline().upper()
a_set = list(set(s))
count_list = []
for i in a_set:
    count_list.append(s.count(i))
    
if count_list.count(max(count_list))>1:
    print('?')
else:
    k = count_list.index(max(count_list))
    print(a_set[k])

print(count_list)
print(a_set)