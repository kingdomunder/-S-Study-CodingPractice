# 5.문자열 내 p와 y의 개수가 같으면 true, 다르면 false /  대소문자 무관 / p y 가 하나도 없으면 true / 한 줄로 짜보기

S = "pPoooyY"

def solution(s):
    answer = bool(s.count("p")+s.count("P") == s.count("y")+s.count("Y") or s.count("p")+s.count("P")+s.count("y")+s.count("Y") == 0)
    return answer
print(solution(S))




