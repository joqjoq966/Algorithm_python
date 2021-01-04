N = int(input())
recommend_num = int(input())
recommend_list = list(map(int,input().split()))
candidate = [[0,0,0]]*N # candidate : [후보index, 추천횟수, 들어온 시간]
final_candidate = [0]*N

for i in range(len(recommend_list)):
	# 추천되는 학생이 최종 후보에 있으면
	if recommend_list[i] in final_candidate:
		for c in candidate:
			# 추천횟수를 1 늘린다
			if c[0]==recommend_list[i]:
				c[1]+=1
				break
	# 추천되는 학생이 최종 후보에 없으면
	else:
		# 최종후보에서 한 명을 삭제하고 이번에 추천되는 학생을 등록
		final_candidate[final_candidate.index(candidate[N-1][0])] = recommend_list[i] 
		candidate[N-1] = [recommend_list[i],1,i]
	# 추천횟수, 들어온 시간 순으로 정렬 --> 둘다 큰 수가 앞에 와야하므로 '-'를 붙여서 정렬
	candidate = sorted(candidate, key=lambda x: (-x[1],-x[2]))
# 최종 후보를 오름차순으로 정렬
final_candidate = sorted(final_candidate)
print(*final_candidate)

# 시간 복잡도 : O(M*N)
# M : 추천받은 학생 리스트의 길이, N : 틀의 개수

##################################################

N = int(input())
recommend_num = int(input())
recommend_list = list(map(int,input().split()))
candidate = [[0,0,0]]*N # candidate : [추천횟수, 들어온 시간, 후보index]

for i in range(len(recommend_list)):
	for c in candidate:
		if c[2]==recommend_list[i]:
			c[0]+=1
			break
	# 추천되는 학생이 최종 후보에 없으면
	else:
		# 최종후보에서 한 명을 삭제하고 이번에 추천되는 학생을 등록
		# final_candidate[final_candidate.index(candidate[0][0])] = recommend_list[i] 
		candidate.sort()
		candidate[0] = [1,i,recommend_list[i]]
	
# 최종 후보를 오름차순으로 정렬
final_candidate = sorted(final_candidate)
print(*candidate)

##################################################

N = int(input())
recommend_num = int(input())
recommend_list = list(map(int,input().split()))
candidate = [[0,0,0]]*N # candidate : [추천횟수, 들어온 시간, 후보index]

for i in range(len(recommend_list)):
	check = False
	for c in candidate:
		if c[2]==recommend_list[i]:
			c[0]+=1
			check = True
			break
	
	if check==False:
		candidate[0] = [1,i,recommend_list[i]]
	candidate.sort()

ans = [c[2] for c in candidate]
ans.sort()
print(*ans)
