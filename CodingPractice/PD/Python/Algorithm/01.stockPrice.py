#1.주식가격 #스택과 큐(stack & prices) 
# https://programmers.co.kr/learn/courses/30/lessons/42584

# ----------------------------------------------------------------------------------------
# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

# 입출력 예
# prices	        return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.\

# ----------------------------------------------------------------------------------------
# 문제 해석
# 배열 prices 안의 원소들은 먼저 들어온 것일수록 측정 할 수 있는 기간이 길어지고, 나중에 들어온 것일 수록 측정 기간이 짧아진다. 
# 그리고 가장 마지막에 들어온 원소는 이후에 측정할 기간이 없으므로 무조건 0으로 반환된다.

# 접근 방법
# 큐 방식을 적용하여, 먼저 들어온 원소를 먼저 내보내면서 나머지 남은 원소들과 비교하도록 계획을 세워본다.
# 마지막 원소를 내보낼 때는 남은 원소가 없어 0을 반환하도록 해야한다.
# ----------------------------------------------------------------------------------------
# Prices = [1, 2, 3, 2, 3]

# def solution(prices):
#     answer = []    # 결과(return)를 담을 리스트
#     time = 0       # 가격이 떨어지지 않은 기간 (측정할 가격 <= 비교대상 가격)
#     for i in prices:               # 가장 먼저 들어온 원소부터 순서대로
#         print('i',i)
#         prices.pop(0)
#         print(prices)
#         for j in prices:           # 남은 원소들을 비교
#             if i <= j : time += 1  # 꺼낸 원소가 남은 원소보다 작거나 같으면 기간 +1 
#         print(time)
#         answer.append(time)        # 남은 원소와 모두 비교한 후, 측정한 기간을 append  
#         time = 0                   # 기간을 초기화하고, 다음 원소를 측정할 준비 
#         print(prices)
#     return answer
# print(solution(Prices))

# ---------1차 오답 [4, 2, 1] 
# 시도 
# - 꺼낸 원소를 .pop를 이용해 제거하면서 계산하도록 만듦
# 문제
# - for문 중에 range의 iterable에 pop로 원소를 제거하면, i의 index값은 변화하지 않으면서, range의 원소들만 변화하기 때문에 어긋남. 
# ----------------------------------------------------------------------------------------
# Prices = [1, 2, 3, 2, 3]

# def solution(prices):
#     answer = []    
#     time = 0       
#     for i in prices:               
#         for j in prices[1:]:       # 꺼낸 원소를 제외하도록 범위 지정
#             print(prices[1:])
#             if i <= j : time += 1   
#         answer.append(time)      
#         time = 0                  
#     return answer
# print(solution(Prices))

# ---------2차 오답 [4, 4, 2, 4, 2] - 비교할 남은 원소들이 점점 줄어야 하는데, 
# 시도
# - 원소를 꺼낸 후에 비교할 대상 리스트를 prices[1:]로 줄이도록 시도
# 문제
# - prices[1:]로 지정하면 1회차만 줄어들고, 2회차부터는 비교대상이 계속 똑같음
# ----------------------------------------------------------------------------------------
# Prices = [1, 2, 3, 2, 3]

# def solution(prices):
#     answer = []    
#     time = 0       
#     for i in prices:
#         print(prices.index(i))
#         for j in prices:      
#             if prices.index(i) == prices.index(j) : continue
#             elif i <= j : time += 1   
#         answer.append(time)      
#         time = 0                  
#     return answer
# print(solution(Prices))

# ---------3차 오답 [4, 2, 0, 2, 0]
# 시도
# - if문을 추가해 i와 j의 index가 같으면 다음 순환을 진행하도록 시도
# 문제
# - for문 내에 순환하는 i의 값으로 index를 출력하면 i의 고유 index가 아닌, i값과 동일한 prices내의 원소의 index를 출력
# ----------------------------------------------------------------------------------------
Prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []    
    time = 0       
    for i in range(len(prices)):                # index 0부터 시작 = 가장 먼저 들어온, 첫 번째 원소부터 꺼냄
        for j in range(len(prices)):      
            if i < j :                          # index를 비교해서 꺼낸 원소보다 뒤에 있는 원소들만 비교하도록 설정
                if prices[i] <= prices[j] :     # 값을 비교해서 가격이 떨어지지 않은 경우를 조건으로 설정
                    time += 1      
        answer.append(time)         
        time = 0                   
    return answer

print(solution(Prices))

# return = [4, 3, 1, 1, 0]

# 프로그래머스 코드정확도 채점 - 합계: 6.7 / 100.0
# 재귀함수를 적용해서도 풀 수 있을 것 같은데, 한 번 생각해보기 
# 프로그래머스 답안 중에 answer = [0]*len(prices) 다음에도 생각해보기 => [0,0,0,0,0]  / 리스트끼리 더하기도 가능