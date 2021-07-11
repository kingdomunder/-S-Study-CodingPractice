# 2.수박수박수

N = 11

def solution(n):
    answer = "수"
    if n == 1:
        return answer
        
    for x in range(1,n):
        if x % 2 == 1:
            answer += "박"
        elif x % 2 == 0:
            answer += "수"

    return answer
    
print(solution(N))