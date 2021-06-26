# 문자열 내 p와 y의 개수 / 대소문자 무관

S = "pPoooyY"

def solution(s):
    answer = bool(s.count("p")+s.count("P") == s.count("y")+s.count("Y") or s.count("p")+s.count("P")+s.count("y")+s.count("Y") == 0)
    return answer
print(solution(S))




