def uni(s): # 입력 문자열의 uni값을 계산
	s = list(s)
	cnt=0
	for i in s:
		if s.count(i)==1: # 그 문자가 1개만 있을 때만 카운팅
			cnt += 1
	return cnt


def solution(S):
	ans = 0
	for i in range(len(S)):
		for j in range(i+1,len(S)+1):
			ans += uni(S[i:j])
			ans %= 10**9+7

	return ans

s = "a"
print(solution(s))


def uni(s): # 입력 문자열의 uni값을 계산
	s = list(s)
	cnt=0
	for i in s:
		if s.count(i)==1: # 그 문자가 1개만 있을 때만 카운팅
			cnt += 1
	return cnt

def alpha_order(s):
	return ord(s)-ord('A')

def solution(S):
	ans = 0; cnt = 0
	exist_cnt = []
	already_exist = []
	for i in range(26):
		exist_cnt.append(0) # 몇 번 존재했었는지 카운트
		already_exist.append(-1) # 이미 존재했던 문자열이면 가장 가까운 인덱스 저장
	
	for i, val in enumerate(S):
		# 현재 인덱스에서 가장 최근에 존재했던 인덱스의 위치 차이
		now = i - already_exist[alpha_order(val)]
		cnt += now - exist_cnt[alpha_order(val)] 
		
		# 해당 알파벳의 가장 최근 인덱스를 업데이트
		already_exist[alpha_order(val)] = i
		# 해당 알파벳의 카운트를 업데이트
		exist_cnt[alpha_order(val)] = now
		
		ans += cnt
	return ans

s="ACAX"
print(solution(s))

