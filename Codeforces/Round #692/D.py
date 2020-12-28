def sub_01(s):
	answer=0
	for i in range(len(s)):
		if s[i]=='0':
			for j in range(i+1,len(s)):
				if s[j]=='1':
					answer+=1
	return answer

def sub_10(s):
	answer=0
	for i in range(len(s)):
		if s[i]=='1':
			for j in range(i+1,len(s)):
				if s[j]=='0':
					answer+=1
	return answer

def check(s,idx):
	for i in range(0,idx):
		if s[i]=='?':
			return False
	return True

def question_01(s,idx): # idx번째 index가 ? 이면 0또는 1을 대입해서 출력
	if idx ==len(s):
		arr.add(s)
		return

	for i in range(idx,len(s)):
		if s[i]=='?' and check(s,i):
			question_01(s[:i]+'0'+s[i+1:],i+1)
			question_01(s[:i]+'1'+s[i+1:],i+1)
			break
		elif check(s,i):
			question_01(s,i+1)
	

s = input()
x,y = map(int,input().split())

arr=set()
ans = 9999
question_01(s,0)
# print(arr)
for i in arr:
	if ans > x*sub_01(i)+y*sub_10(i):
		ans = x*sub_01(i)+y*sub_10(i)
print(ans)
