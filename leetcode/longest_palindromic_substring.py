s = input()
idx, l = 0, 0

for i in range(len(s)):
    if s[i-l:i+1] == s[i-l:i+1][::-1]:
        idx = i-l
        l += 1
    elif i-l > 0 and s[i-l-1:i+1] == s[i-l-1:i+1][::-1]:
        idx = i-l-1
        l += 2
    
print(s[idx:idx+l])















# arr=[]
# idx, l = 0, 1
# for i in range(len(s)-1):
#     # if s[i]==s[i+1]:
#     #     l += 1
#     idx = i
    
#     for j in range(1,i+1):
#         if i+j < len(s) and s[i]==s[i+j]:
#             idx-=1
#             l+=2
        
#         if i+j+1 < len(s) and s[i-j] == s[i+j+1]:
#             idx-=1
#             l+=2
    
#     if len(arr)==0 or len(arr[-1]) < l:
#         arr.append(s[idx:idx+l])
#     l = 1

# print(arr)