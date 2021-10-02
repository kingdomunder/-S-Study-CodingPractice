# 31. 가장 먼 노드 / 플로이드 와샬과 다익스트라
# https://programmers.co.kr/learn/courses/30/lessons/49189
# ---------문제 설명----------------------------------------------------------------------
# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 
# 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.
# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.
# ---------제한 사항----------------------------------------------------------------------
# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

# 입출력 예
# n	vertex	
# 6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
# return 
# 3
# 입출력 예 설명

# 예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.
# -----------------------------------------------------------------------------------------------


# ---------문제 해석---------------------------------------------------------------------- 
# 간선은 양방향이다.
# 1번노드에서 가장 멀리 떨어진 노드들의 거리는 같다.
# 항상 1번노드에서 시작하고, 각 노드까지의 초단경로를 구해야 한다.

# ---------접근 방법---------------------------------------------------------------------- 
# 1번 노드에서 최단거리를 구하는 것이므로, 이전 문제들처럼 다익스트라를 활용한다.
# 양방향을 주의해서 무한루프에 빠지지 않도록 한다. 
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------

n1 = 6
vertex1 = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

import sys

def solution(n, node):
    answer = 0
    distance = [sys.maxsize for _ in range(n)]
    distance[0] = 0
    visited = [False for _ in range(n)]

    while False in visited:
        shortest = sys.maxsize
        for i in range(n):
            if (visited[i] == False) and (distance[i] < shortest):  
                shortest = distance[i]
                depart = i + 1
        visited[depart-1] = True

        for node1, node2 in node:
            if (node1 == depart) and (visited[node2-1] == False):
                distance[node2-1] = min(distance[node2-1], distance[node1-1]+1)
            elif (node2 == depart) and (visited[node1-1] == False):
                distance[node1-1] = min(distance[node1-1], distance[node2-1]+1)

    answer = len(list(filter(lambda x : x == max(distance), distance)))

    return answer

print(solution(n1,vertex1))

# return1 = 3

# ---------1차 오답---------------------------------------------------------------------- 
# 1. => 한 쪽 방향으로 depart가 계속 잡히면 최단거리 계산에 오류가 생김 


# ----------------------------------------------------------------------------------------
# import sys

# def solution(n, node):
#     answer = 0
#     distance = [sys.maxsize for _ in range(n)]
#     distance[0] = 0
#     visited = [False for _ in range(n)]
#     visited[0] = True
#     checkDis = []
#     checkNode = []
#     stack =[]

#     depart = 1
#     while False in visited:
#         checkDis = []
#         checkNode = []
#         for node1, node2 in node:
#             if (node1 == depart) and (visited[node2-1] == False):
#                 distance[node2-1] = min(distance[node2-1], distance[node1-1]+1)
#                 checkDis.append(distance[node2-1])
#                 checkNode.append(node2)

#             elif (node2 == depart) and (visited[node1-1] == False):
#                 distance[node1-1] = min(distance[node1-1], distance[node2-1]+1)
#                 checkDis.append(distance[node1-1])
#                 checkNode.append(node1)

#         if (checkNode == []) and (False in visited):
#             stack = stack[ :-1]
#             depart = stack[-1]
#             continue

#         shortestNode = checkNode[checkDis.index(min(checkDis))]
#         visited[shortestNode-1] = True
#         stack.append(shortestNode)
#         depart = shortestNode

#     answer = len(list(filter(lambda x : x == max(distance), distance)))

#     return answer

# print(solution(n1,vertex1))
# ----------------------------------------------------------------------------------------

# 테스트 1 〉	실패 (0.05ms, 10.3MB)
# 테스트 2 〉	실패 (런타임 에러)
# 테스트 3 〉	실패 (0.23ms, 10.3MB)
# 테스트 4 〉	통과 (3.86ms, 10.2MB)
# 테스트 5 〉	통과 (68.51ms, 10.4MB)
# 테스트 6 〉	실패 (576.58ms, 10.5MB)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)

# 프로그래머스 코드정확도 채점 - 합계: 22.2 / 100.0




