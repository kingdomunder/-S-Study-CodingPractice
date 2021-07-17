# 8. x만큼 간격이 있는 n개의 숫자 / x부터 시작해 x 씩 증가하는 숫자를 n 개 가지는 리스트 리턴

x1 = 2
n1 = 5

x2 = 4
n2 = 3

x3 = -4
n3 = 2

x4 = 0 
n4 = 4

def solution(x, n):
    a = []

    for i in range(1,n+1):
        a.append(x*i)
    
    answer = a
    return answer


print(solution(x1,n1))

print(solution(x2,n2))

print(solution(x3,n3))

print(solution(x4,n4))
