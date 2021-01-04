# 정수 삼각형을 위에서부터 0단계, 1단계,,, (N-1)단계라고 하자
# i번째 단계의 triangle에는 현재까지 선택된 수의 합이 최대인 값만 저장되어 있음
N = int(input())
#정수 삼각형을 나타내는 리스트
triangle = []

for i in range(N):
	t = list(map(int,input().split()))
	# 0번째 단계는 자기 자신 그대로 
	if i>=1:
		t[0]+=triangle[i-1][0]
		# i번째 단계에서는 ans_list의 i-1번째 단계의 왼쪽과 오른쪽 중 큰 것을 더함
		if i>=2:
			for j in range(1,i):
				t[j]+=max(triangle[i-1][j-1],triangle[i-1][j])
		# i번째 단계의 마지막 수는 i-1번째 단계의 제일 뒤의 값에 자기 자신을 더함
		t[-1]+=triangle[i-1][-1]
	
	triangle.append(t)
print(max(triangle[N-1]))
