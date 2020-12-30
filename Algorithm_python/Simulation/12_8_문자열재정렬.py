s = list(input())

capital = [] #대문자 담을 리스트
num = [] #숫자 담을 리스트
for i in s:
	if i.isalpha(): #문자이면
		capital.append(i)
	else: #숫자이면
		num.append(int(i))

capital.sort()
print(''.join(capital) + str(sum(num))) #오름차순+숫자더한값 출력

#시간복잡도 : l = len(s)라고 하면 O(l+l*log(l)) ==> O(l*log(l))