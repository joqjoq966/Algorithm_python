s = input()

num_list = list(map(int,s))
answer = 0
for i in num_list:
	if i==0 or i==1 or answer==0 or answer==1:
		answer+=i
	else:
		answer*=i
print(answer)