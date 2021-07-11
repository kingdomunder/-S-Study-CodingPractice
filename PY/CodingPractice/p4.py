# 4.약수의 합

N = 12

def solution(n):
    answer = 0
    for x in range(1,n+1):
        if n % x == 0:
            answer += x

    return answer

print(solution(N))


