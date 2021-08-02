
# 6.소수찾기 / 완전탐색과 이분탐색 
# https://programmers.co.kr/learn/courses/30/lessons/42839

# ----------------------------------------------------------------------------------------

# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# 입출력 예
# numbers	return
# "17"  	  3
# "011"	      2

# 입출력 예 설명
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
# 11과 011은 같은 숫자로 취급합니다.

# ----------------------------------------------------------------------------------------

# 문제 해석
# 소수 : (素數, prime number) [1보다 큰 자연수] 중 1과 자기자신만을 약수로 가지는 수.

# 접근 방법
# 문자열 numbers를 문자 단위로 나누고, 그 문자들로 가능한 모든 경우를 조합해 본다 
# 조합한 숫자들 중에서, 0이 맨 앞에 나온 경우는 제외한다. 0이 연속해서 나온 경우도 제외한다. ex) 00013
# 조합한 숫자가 소수인지 확인하기 위해서, [2]부터 [자기자신-1]까지의 숫자 중에 약수가 있는지 확인한다
# 확실한 방법은 위의 범위 내 모든 숫자를 확인하면서, 나머지가 0인 경우를 완전탐색하는 것이다
# 나머지가 0인 경우가 나온다면, 그 숫자는 소수가 아니다
# 모든 경우를 확인해보아야 하므로, 특정한 target값을 구하는 이분탐색은 적합하지 않다
# [2]~[자기자신-1]의 범위를 순환하는 것 이외에 좀 더 효율적인 방법이 있을지 고민해 본다

# ----------------------------------------------------------------------------------------

# numbers1 = "17"
# numbers2 = "011"
numbers2 = "1234"

def solution(numString):
    num = []
    PrimeNum = []

    # for a in range(len(numString)):
    #     num.append(numString[a])
        
    # for i in range(len(numString)):
    #     N = ["1","2","3","4"]
    #     N.pop(i)

    #     for j in range(len(N)):
    #         PrimeNum.append(num[i] + N[j])

    # count = 0
    # while count < len(numString):
    #     num.append(numString[count])
    #     count += 1

    # count = 0
    # while count < len(numString):
    #     num.pop(count)
    #     num.append(num[count] + )

    #     count += 1

    count = 0
    while count < len(numString):
        for i in range(len(numString)):
            num.append(numString[i])
        
        PrimeNum.append(numString[count])

        num.pop(count)

        for j in range(num):
            PrimeNum.append(numString[j] + numString[j])


    return num
    # return PrimeNum

# print(solution(numbers1))
print(solution(numbers2))

# return 3
# return 2

# 프로그래머스 코드정확도 채점 - 합계: 100.0