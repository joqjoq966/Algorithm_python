import heapq
def solution(food_times, k):
    answer = 0 
    q = []; length = len(food_times)
    for i in range(len(food_times)):
	    heapq.heappush(q,(food_times[i],i+1))
	
    if sum(food_times) <= k:
        return -1
    first_time = 0 #남아있는 음식중 먹는 시간이 최소인 음식을 다 먹는데 걸리는 시간
    second_time = 0 #남아있는 음식중 먹는 시간이 두번째로 최소인 음식을 다 먹는데 걸리는 시간
    cnt = 0;
    while cnt <= k:
        first_time = second_time
        second_time = q[0][0]
        if cnt + (second_time-first_time)*length > k:
            break
        second_time = heapq.heappop(q)[0]
        cnt += (second_time-first_time)*length
        length-=1

    res = sorted(q,key = lambda x: x[1])
    
    return res[(k-cnt)%length][1]
    