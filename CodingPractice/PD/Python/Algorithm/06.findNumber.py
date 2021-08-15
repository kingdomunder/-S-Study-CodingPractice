
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

# def solution(numString):
#     num = []
#     PrimeNum = []

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

    # count = 0
    # while count < len(numString):
    #     for i in range(len(numString)):
    #         num.append(numString[i])
        
    #     PrimeNum.append(numString[count])

    #     num.pop(count)

    #     for j in range(num):
    #         PrimeNum.append(numString[j] + numString[j])


    # return num
    # return PrimeNum

# print(solution(numbers1))
# print(solution(numbers2))

# return 3
# return 2

# ----------1차 오답 ----------------------------------------------------------------- 

# 시도
# - 재귀함수를 구현해보고자 함
# 문제
# - numbers에 주어진 숫자열로 가능한 모든 경우의 수를 구하는 식을 짜려고 하였으나 실패함 
# - 숫자를 조합하면서 꺼낸 숫자가 중복되지 않도록 구현하는 것이 자릿수가 커질수록 어려웠음 

# ----------------------------------------------------------------------------------------

# 11번 타겟넘버에서 DFS를 성공적으로 구현해보았는데, 이번 문제에 적용해보고자 함 

# 접근 방법
# 문자열 numbers를 문자 단위로 나누고, 그 문자들로 가능한 모든 경우를 조합해 본다 
# 조합한 숫자들 중에서, 0이 맨 앞에 나온 경우는 제외한다. 0이 연속해서 나온 경우도 제외한다. ex) 00013
#<<<< DFS에서 마지막 노드를 검사한 후에, 조합한 숫자열을 검사하여 위의 경우를 걸러낸다 

# 조합한 숫자가 소수인지 확인하기 위해서, [2]부터 [자기자신-1]까지의 숫자 중에 약수가 있는지 확인한다
# 확실한 방법은 위의 범위 내 모든 숫자를 확인하면서, 나머지가 0인 경우를 완전탐색하는 것이다
# 나머지가 0인 경우가 나온다면, 그 숫자는 소수가 아니다
# 모든 경우를 확인해보아야 하므로, 특정한 target값을 구하는 이분탐색은 적합하지 않다
# [2]~[자기자신-1]의 범위를 순환하는 것 이외에 좀 더 효율적인 방법이 있을지 고민해 본다


# numbers1 = "17"
# numbers2 = "011"
# numbers3 = "1034"

# def solution(numbers):
#     answer = 0
#     numList = []
#     stack = []
#     sum = ""
    
#     for i in numbers:
#         stack.append([i,numbers.replace(i,""),sum])

#     while len(stack) > 0:
#         print(stack)
#         now = stack.pop()
#         print(now)
#         now[2] += now[0]
        
#         if not now[2].startswith("0"):
#             if not now[2] in numList:
#                 numList.append(now[2])
        
#         if len(now[1]) > 0:
#             for i in now[1]:
#                 stack.append([i,now[1].replace(i,""),now[2]])
# #----------------------------모든 경우의 수 생성 완료---------------------------------
#     print(numList)
#     # ['1', '10']

# # print(solution(numbers1))
# print(solution(numbers2))
# # print(solution(numbers3))

# ----------2차 오답 ----------------------------------------------------------------- 

# 문제
# - numbers2 = "011"에서 경우의수 생성 시, [1, 10, 11, 101, 110] 가 나와야 하는데 ['1', '10'] 만 출력됨
# 원인
# - numbers.replace를 사용하면 1 두개가 모두 제거되어 버려서 "011"이 "01"과 같은 결과로 나오게 됨

# ----------------------------------------------------------------------------------------

numbers1 = "17"
numbers2 = "011"
numbers3 = "1034"

def solution(numbers):
    answer = 0
    numList = []
    stack = []
    sum = ""

    for i in range(len(numbers)):
        stack.append([ numbers[i] , (numbers[ :i] + numbers[i+1: ]) , sum ]) # 
# 문자열(str)에는 pop, remove, del이 없고 replace만 있는데, replace(제거할 문자열,"")을 사용하면 입력하는 문자와 일치하는 문자는 index에 관계없이 한꺼번에 제거됨 
    
    while len(stack) > 0:
        # print(stack)
        now = stack.pop()
        # print(now)
        now[2] += now[0]
        
        if not now[2].startswith("0"):
            if not now[2] in numList:
                numList.append(now[2])
        
        if len(now[1]) > 0:
            for i in range(len(now[1])):
                stack.append([ now[1][i] , (now[1][ :i]+now[1][i+1: ]) , now[2] ])
#----------------------------모든 경우의 수 생성 완료---------------------------------  

    for num in numList:
        for i in range(2,int(num)):  
            if int(num) % i == 0:
                break
            elif i == (int(num) - 1):
                answer += 1
        

    return answer

print(solution(numbers1))
# print(solution(numbers2))
# print(solution(numbers3))

# return 3
# return 2

# 프로그래머스 코드정확도 채점 - 합계: 58.3 / 100.0
# 1.DFS로 경우의 수 모두 생성 -> 2.경우의 수 마다 소수인지 검사 
# 경우의 수 생성이나 소수검사 방법을 바꿔서 시간초과 문제 해결해보기 

