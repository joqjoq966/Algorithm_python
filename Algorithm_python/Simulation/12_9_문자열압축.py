# Solution 1
def solution(s):
    s = list(s)
    ans = len(s)
    
    for cut in range(1,len(s)//2+1): #전체길이의 절반까지만 자르는 단위로 설정
        i = 0
        temp = len(s)
        while i+cut < len(s): 
            target = s[i:i+cut] #반복되는 문자열 중 제일 앞에 것을 target으로 설정
            cnt = 0
            while target == s[i:i+cut]: #target문자열이 반복되는 만큼 카운팅
                i+=cut
                cnt+=1
            if cnt>=2: #반복된 만큼 전체 길이에서 뺄셈
                temp -=(cnt-1)*cut
                temp += len(str(cnt))
    
        if temp < ans: #1~len(s)//2까지 최소값을 출력
            ans = temp
        
    return ans

# 시간 복잡도 : O(l*l/2) --> O(l^2)
# l : 주어진 문자열의 길이

# Solution 2
def solution(s):
    answer = 0
    result =""
    final_list = []

    if(len(s)==1):
        return 1

    for cut in range(1,len(s)//2 +1):
        temp = s[:cut]
        cnt = 1
        for i in range(cut,len(s),cut): # for문으로 cut만큼 건너뛰면서 실행
            if s[i:i+cut]==temp:
                cnt+=1
            else:
                if cnt == 1:
                    cnt=""
                result += str(cnt) + temp
                temp = s[i:i+cut] #다음 target문자열로 넘어감
                cnt = 1

        if cnt ==1:
            cnt=""
        result += str(cnt)+temp
        final_list.append(len(result)) #가능한 모든 길이를 저장
        result=""
    return min(final_list)

# 시간 복잡도 : O(l*l/2) --> O(l^2)
# l : 주어진 문자열의 길이