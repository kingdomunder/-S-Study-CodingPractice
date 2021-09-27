# 30. 특정 거리의 도시 찾기 / 플로이드 와샬과 다익스트라
# https://www.acmicpc.net/problem/18352
# ---------문제 설명----------------------------------------------------------------------
# 어떤 나라에는 1번부터 [N]번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 [K]인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 

# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
# 예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.
# 이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.  2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.
# ----------------------------------------------------------------------------------------
# 입력

# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. 
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

# 출력

# X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
# 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
# ----------------------------------------------------------------------------------------


# ---------문제 해석---------------------------------------------------------------------- 
# 입력 첫째 줄은 기본 정보, 둘째 줄 아래로는 도로를 의미한다 
# 출력은 한 줄에 도시번호 하나씩 출력해야 하므로, 줄바꿈을 사용한다
# 1번 도시가 아닌, X번 도시에서 출발한다 
# 도로는 단방향이다 

# ---------접근 방법---------------------------------------------------------------------- 
# X번 도시를 중심으로 거리를 계산해야하므로 다익스트라를 이용하여 길이를 누적시킨다 
# 단방향 도로이므로 다시 돌아오지 않도록 구성한다.
# 입력값에 들어있는 공백도 주의한다.
# 거리가 K인 도시들을 리스트로 만들어서 오름차순으로 정렬한 후에, 하나씩 출력하도록 한다. 

# 지니간 도시는 다시 돌아오지 않도록 하기 위해, 한 번 지난 길은 체크해서 두 번 지날 수 없도록 해 본다. 
# ----------------------------------------------------------------------------------------
"""
입력1
4 4 2 1
1 2
1 3
2 3
2 4
입력2
4 3 2 1
1 2
1 3
1 4
입력3
4 4 1 1
1 2
1 3
2 3
2 4
"""
import sys

N = 0
M = 0 
K = 0
X = 0
roadList = []   #2번째 줄부터 시작하는 도로정보를 담을 리스트

count = 0
while True:   #도로길이+1 만큼 input반복
    input = list(map(int,sys.stdin.readline().split(" ")))
    if len(input) == 4: #첫 번째 입력값을 따로 설정 
        (N, M, K, X) = (input[0], input[1], input[2], input[3])
    else:
        roadList.append(input)
    if count == M:
        break
    count += 1

def solution(city,limit,center,road):
    distance = [300000 for _ in range(city)]   #각 도시까지의 거리 기본값을 최대치로 설정
    distance[center-1] = 0  #시작하는 도시까지의 거리는 0
    stack = [center]    #출발도시 시작점
    
    while True:    
        depart = stack[-1]
        stack = stack[ :-1] 
        for r in road:
            if r != 'passed':
                if depart == r[0]:    #출발도시가 같으면 
                    distance[r[1]-1] = min(distance[r[1]-1], distance[depart-1]+1)  #[도착도시까지의 기존 거리], [출발도시까지의 거리 +1] 중 최솟값 선택
                    road[road.index(r)] = 'passed'
                    if r[1] not in stack:
                        stack.append(r[1]) #도착도시를 스택에 저장 
                elif r[0] not in stack:
                    stack.append(r[0])
        if road.count('passed') == len(road):
            break
    if limit not in distance: 
        print(-1) 
    else:
        for i in range(len(distance)):
            if distance[i] == limit:
                print(i+1)

solution(N,K,X,roadList)

"""
return1
4
return2
-1
return3 
2
3
"""

# ---------1차 오답---------------------------------------------------------------------- 
# 백준 채점 - 시간 초과
# 1. => .pop 메소드 없애보기
# 2. => 단방향이므로 반대로 갈 수 없음
# ----------------------------------------------------------------------------------------

# N = 0
# M = sys.maxsize #input 반복문을 시작하기 위해서 최댓값으로 설정
# K = 0
# X = 0
# roadList = []   #2번째 줄부터 시작하는 도로정보를 담을 리스트

# count = 0
# while count <= M:   #도로길이+1 만큼 input반복
#     input = list(map(int,sys.stdin.readline().split(" ")))
#     if len(input) == 4: #첫 번째 입력값을 따로 설정 
#         (N, M, K, X) = (input[0], input[1], input[2], input[3])
#     else:
#         roadList.append(input)
#     count += 1


# def solution(city,limit,center,road):
#     distance = [sys.maxsize for _ in range(city)]   #각 도시까지의 거리 기본값을 최대치로 설정
#     distance[center-1] = 0  #시작하는 도시까지의 거리는 0
#     stack = [center]    #출발도시 시작점
    
#     while len(road) > 0:    
#         depart = stack.pop()    
#        = 0
#         while len(road) >    #지나간 도로를 리스트에서 remove해야 하므로 while문과  1씩 증가하는 변수 index를 사용
#             if depart == road[0]:    #출발도시가 같으면 
#                 distance[road[1]-1] = min(distance[road[1]-1], distance[depart-1]+1)  #[도착도시까지의 기존 거리], [출발도시까지의 거리 +1] 중 최솟값 선택
#                 stack.append(road[1]) #탐색할 출발도시를 스택에 저장 
#                 road.pop     #지나간 도로이므로 삭제 
#             elif depart == road[1]:
#                 distance[road[0]-1] = min(distance[road[0]-1], distance[depart-1]+1)
#                 stack.append(road[0])
#                 road.pop
#             else:
#                += 1  #출발할 도로정보가 없으면 다음 도로정보로 이동

#     if limit not in distance: 
#         print(-1) 
#     else:
#         for i in range(len(distance)):
#             if distance[i] == limit:
#                 print(i+1)

# solution(N,K,X,roadList)






