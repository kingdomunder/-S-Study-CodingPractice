# 7.가운데 글자 가져오기 / s의 가운데 글자 / 짝수면 가운데 두 개 / s 길이는 1 ~ 100

s1 = "abcde"
s2 = "qwer"

def solution(s):
    a = []
    for x in s:
        a.append(x)

    if len(a) % 2 == 0:
        answer = s[int(len(a)/2)-1] + s[int(len(a)/2)]
    else:
        answer = s[int((len(a)/2)-0.5)]

    return answer

# 문자열 슬라이싱 가능 ( str[ : ] )  
# // - 나누기 후 소수점 아래는 버림 