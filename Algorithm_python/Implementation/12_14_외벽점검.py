from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak)
    ans = len(dist)+1 # dist최대 개수보다 많으면 -1을 반환하기 위한 초기값 설정

    for i in range(weak_len): #시계방향 반시계방향을 무시하고 항상 오른쪽으로만 가도록 설정하기 위해 전처리
        weak.append(weak[i]+n)
        
    #시작점을 달리해가면서 오른쪽으로만 가도록 weak를 자름
    for start in range(weak_len):
        traverse_list = [weak[j] for j in range(start,start+weak_len)] 
        #친구들이 갈 수 있는 거리를 순열로 계산해 모든 경우를 계산
        perm = permutations(dist,len(dist))    
        #각 순열마다 외벽을 모두 수리할 수 있는지 점검
        for p in perm:
            friend_idx, friend_cnt = 0,1
            cover = traverse_list[0] + p[friend_idx] #처음 친구가 수리할 수 있는 길이
            for i in range(weak_len):
                # 외벽의 위치가 친구가 수리할 수 있는 위치를 넘어서면 친구 한 명 추가
                if traverse_list[i] > cover:
                    friend_cnt += 1
                    # 친구 수가 주어진 친구보다 커지면 break and return -1
                    if friend_cnt > len(p):
                        break
                    # 한 명 추가된 친구가 점검할 수 있는 최대거리 계산
                    friend_idx+=1
                    cover = traverse_list[i] + p[friend_idx]
            #투입되는 최소의 친구 계산
            ans = min(ans,friend_cnt)
            
    if ans > len(dist):
        return -1
    
    return ans

# 시간 복잡도 : d를 후보 친구들(dist)의 수, w을 낡은 외벽의 수라고 할 때, O(d!*w^2)
# 문제의 조건 d<=8 and weak<=15
# 8!*15^2 == 40320 * 225 = 9072000(약 900만)
# 파이썬에서는 1초에 2000만번의 연산을 기준으로 하기 때문에 팩토리얼이 들어가는 시간복잡도를 갖지만 
# 1초 안에 이 문제를 통과할 수 있다.