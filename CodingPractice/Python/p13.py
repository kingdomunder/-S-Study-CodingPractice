# 13. 자릿수 더하기 / 자연수 N의 각 자릿수의 합을 return 

N1 = 123 #6
N2 = 987 #24

def solution(n):
    a = 0
    for i in range(len(str(n))-1,-1,-1):
        a += (n // 10**i)
        n -= (n // 10**i) * (10**i)
    return a
    

# print(solution(N1))

print(solution(N2))


# 몫을 구하는 연산자 //
# for문 range 역순으로 돌릴 때 - range(시작숫자,끝 숫자,-1) - (시작숫자-1)로 시작하지 않는다 , 끝 숫자 입력해야 한다
# 제곱연산자는 ^ 가 아니라 **
# 재귀함수 적용가능