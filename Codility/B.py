def sub(A,B,char): # 사용된 문자의 개수를 1개 줄이고 남은 a,b값을 리턴
	if char =='a':
		A-=1
	elif char=='b':
		B-=1
	return A,B

def is_impossible(A,B): #불가능한 경우 예외처리 
	if A>2*B+2 or B>2*A+2:
		return True
	return False

def solution(A,B):
	if is_impossible(A,B)==True: # 만들어질 수 없는 경우 빈 문자열 리턴
		return ''

	s = ''; char ='' # s : a와 b로 이루어진 조건을 만족시키는 문자열 , char : a또는 b
	total = A+B # 문자열의 총 길이 임시저장
	if A>=B: #갯수가 더 많은 문자열부터 시작
		char = 'a'
	else:
		char = 'b'
	
	for i in range(total):
		s += char # a또는 b를 조건에 맞게 한 개씩 증가시킨다
		A,B = sub(A,B,char) # 사용된 것의 개수를 감소
		if A==0: # 다 쓴 문자가 있으면 다른 문자로 대체
			char ='b'
		elif B==0:
			char = 'a'
		
		if len(s)>=2 : # 만약 길이가 2보다 길면
			# 바로 전 인덱스 2개의 문자가 같은 경우 다른 문자로 변경
			if s[-1]==char and s[-2]==char:
				if char=='a':
					char ='b'
				else:
					char ='a'
	return s

print(solution(1,4))