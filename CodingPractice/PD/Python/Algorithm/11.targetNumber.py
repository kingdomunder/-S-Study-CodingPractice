# 11.타겟넘버 / DFS와 BFS
# https://www.acmicpc.net/problem/2606

# ----------------------------------------------------------------------------------------

# 문제 설명
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

# 입출력 예
# numbers	      target  return
# [1, 1, 1, 1, 1]	3	    5

# ----------------------------------------------------------------------------------------

# 문제 해석
# 타겟넘버는 numbers안의 원소(노드)들이 빠짐없이 전부 조합되어 계산해야 한다
# numbers안의 원소들은 값이 동일하더라도, 인덱스 번호에 따라 서로 다른 객체이기 때문에 중복연산을 주의하여야 한다 

# 접근 방법
# DFS와 BFS를 각각 적용해보되, 전체 경우의 수를 모두 순환해야 하기 때문에 return 검사는 마지막회차에서 진행한다(numbers의 마지막 인덱스 원소)
# = 제일 깊은 곳의 노드까지 검사한다는 말과 같다 
# DFS에는 스택을, BFS에는 큐를 사용해본다 

# ----------------------------------------------------------------------------------------
# DFS 풀이

numbers1 = [1, 1, 1, 1, 1]
target1 = 3

def solution(numbers, target):
    answer = 0   # 방법의 수(return) = [마지막 노드까지 더했을 때, target값이 나온다면 +1]
    stack = []   # 비교할 노드들을 스택으로 저장 
    routine = 0  # 순환 = [numbers의 인덱스번호] 
    sum = 0      # 누적합계 -> target값을 목표로 더해감

    stack.append([-numbers[routine],routine,sum])   # 첫 번째 인덱스의 노드들을 미리 저장하고 시작
    stack.append([numbers[routine],routine,sum])    # [노드, 인덱스(routine), 누적합계]를 같이 저장
    
    while len(stack) > 0: # 비교할 노드들이 계속 스택으로 쌓이기 때문에, 스택이 비워지면 모든 노드를 검사한 셈이 됨 
        # print(stack) 확인용
        now = stack.pop()   # 검사할 노드를 스택에서 꺼냄
        routine = now[1]    # 해당 노드의 순환번호를 현재로 대입 (그래야 해당 지점으로 거슬러 올라가게 됨)
        sum = now[2]        # 누적합계 또한 당시 합계로 리셋

        sum += now[0]      # 누적합계 + 현재값 (순환 마지막에 target값과 비교)
        routine += 1       # 순환 +1

#----------------------------현재 노드를 꺼냈으므로, 검사 진행-------------------------------------

        if routine >= len(numbers):  # 순환번호가 대상의 인덱스번호를 초과하면 = [마지막회차] = 제일 깊은 곳의 노드까지 검사완료
            if sum == target:        # target값과 같으면
                answer += 1          #  방법의 수(return) +1
                # print(answer) 확인용
        else:                   # 순환이 인덱스 안이라면 = [마지막회차가 아님] = 더 깊은 노드 검사 필요
            stack.append([-numbers[routine],routine,sum])   # 검사할 다음 노드들을 스택에 추가
            stack.append([numbers[routine],routine,sum])

    return answer

print(solution(numbers1,target1))

# return 5

# 프로그래머스 코드정확도 채점 - 합계: 100.0 / 100.0
# 처음에는 해당 노드들만 스택에 저장하는 방식으로 진행하면서 막혔었고,
# 노드에 해당하는 순환번호를 같이 저장하니 순조롭게 풀이가 진행되었다. 
# 스택에 리스트를 쌓는 방법 말고도, 다른방법 연구해보기 
# BFS로도 풀어보기 
