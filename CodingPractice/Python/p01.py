# 1.두 정수 사이의 합

A=100
B=105
def solution(a,b):
    if a<b :
        for x in range(a+1,b+1):
            a += x
            answer = a
    elif a>b : 
        for x in range(b+1,a+1):
            b += x
            answer = b
    else:
        answer = a
        
    return answer
    
print(solution(A,B))