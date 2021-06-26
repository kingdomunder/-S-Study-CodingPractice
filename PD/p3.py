# 3.서울에서 김서방 찾기

seoul = ["Jane","Kim"]

def solution(seoul):
    x = seoul.index("Kim")

    x = str(x)

    answer = '김서방은 ' + x + '에 있다'
    return answer

print(solution(seoul))


