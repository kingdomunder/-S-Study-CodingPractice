# 문자열 내 p와 y의 개수 / 대소문자 무관

S = "oooo"

def solution(s):
    if s.count("p")+s.count("P") == s.count("y")+s.count("Y") or s.count("p")+s.count("P")+s.count("y")+s.count("Y") == 0 :
        return True
    else:
        return False

print(solution(S))




