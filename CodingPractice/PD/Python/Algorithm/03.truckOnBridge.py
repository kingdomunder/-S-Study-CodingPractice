#3.다리를 지나는 트럭 #스택과 큐(stack & prices) 
# https://programmers.co.kr/learn/courses/30/lessons/42583

# ----------------------------------------------------------------------------------------
# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	        []	                []          	[7,4,5,6]
# 1~2   	[]              	[7]         	[4,5,6]
# 3	        [7]	                [4]	            [5,6]
# 4	        [7]	                [4,5]	        [6]
# 5	        [7,4]	            [5]	            [6]
# 6~7	    [7,4,5]	            [6]	            []
# 8     	[7,4,5,6]	        []	            []
# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 
# 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

# 입출력 예
# bridge_length	weight	truck_weights	                 return
# 2	            10	    [7,4,5,6]	                     8
# 100	        100	    [10]                             101
# 100	        100 	[10,10,10,10,10,10,10,10,10,10]	 110
# ----------------------------------------------------------------------------------------

# 문제 해석
# 앞 쪽의 트럭들이 먼저 나가야 하므로, 큐의 방식을 적용해본다
# 입출력 예 첫 번째에서 7kg의 트럭이 다리 위에 있던 시간은 1, 2초 이고, 다리를 완전히 건너면 3초가 된다
# 고로 [다리길이+1]이 다리를 건너기 위한 [기본 시간]이다 
# 트럭 한 대가 다리를 건너기 위해서는 [기본 시간]이 모두 경과해야 한다
# 무게제한에 걸리지 않는다면, 뒤의 트럭이 들어올 때마다 [기본 시간]은 초기화된다
# 무게제한에 걸린다면, 다리를 지나는 트럭이 완전히 통과해야 뒤의 트럭이 들어올 수 있다 
# return 은 계속 초기화되는 [기본 시간]이 모두 경과했을 때의 값이다
# 트럭의 무게는 해당 트럭 고유의 [기본 시간]이 모두 경과했을 때 사라진다

# 접근 방법
# return 값을 구하기 위해서, 함수가 돌아가는 내내 누적되는 [전부 건너는 데 걸리는 시간] 값을 설정한다
# 한 트럭이 다리 위에 올라왔을 때 (1초 경과), 다음 트럭이 올라올 수 있는지 무게의 합을 계산한다
# 무게의 합을 계산하여, [기본 시간]이 초기화 될 지(뒤의 트럭 진입), 완전히 경과하고 새로 더할 지(진입 불가) 결정한다
# 진입했을 때와 다리를 건넜을 때의 시간계산에 유의하며 식을 세워본다

# ----------------------------------------------------------------------------------------

# bridge_length1 , bridge_length2 , bridge_length3 = 2 ,         100 ,   100
# weight1 ,        weight2 ,        weight3        = 10 ,        100 ,   100
# truck_weights1 , truck_weights2 , truck_weights3 = [7,4,5,6] , [10] , [10,10,10,10,10,10,10,10,10,10]  # 10대

# def solution(bridgeLen, bridgeWeight, truckWeight):
#     time = 0              # 전부 건너는 데 걸리는 시간
#     onBridgeTruck = []    # 다리 위 트럭들의 큐
#     lenRemain = []        # 각 트럭이 건너야 할 남은 길이의 큐 (각각 건너는데 필요한 시간)

#     while len(truckWeight) != 0:     # 모든 대기 트럭이 다리 위에 올라갈 때까지 반복
#         if ((sum(onBridgeTruck[:]) + truckWeight[0]) <= bridgeWeight) and (bridgeLen > len(onBridgeTruck)): 
# # { [다리 위 트럭들의 무게]+[다음 트럭의 무게]가 [다리가 견딜 수 있는 무게]와 같거나 가벼우면 and [다리길이]가 [다리 위 트럭들의 길이]보다 길면 } = (트럭이 더 올라올수 있으면)
            
#             if len(lenRemain) != 0:     # 다리 위에 트럭이 있으면 
#                 for i in range(len(lenRemain)):
#                     lenRemain[i] -= 1   # 남은 길이가 1씩 감소 (이동하는 중)     
#             onBridgeTruck.append(truckWeight[0])   # 다음 트럭이 올라옴
#             time += 1             # 올라오면 1초가 경과                                              
#             lenRemain.append(bridgeLen)  # 올라온 트럭이 건너야 할 길이 추가 (건너는데 필요한 시간)     
#             truckWeight.pop(0)   # 올라온 트럭을 대기트럭 큐에서 꺼냄

#         else :      # 다음 트럭이 올라올 수 없으면 
#             time += (lenRemain[0])  # 선두 트럭이 남은 길이를 이동 = 이동한 만큼 시간이 경과
#             for i in range(len(lenRemain)):     
#                 lenRemain[i] -= lenRemain[0]  # 모든 트럭에 이동한만큼 남은 거리를 차감 
#             lenRemain.pop(0)
#             onBridgeTruck.pop(0)    # 선두 트럭 통과
      
#     while len(onBridgeTruck) != 0:   # 대기 트럭이 없을 때, 다리 위 트럭들이 모두 건널 때까지 반복
#         time += (lenRemain[0]) 
#         for i in range(len(lenRemain)):     
#             lenRemain[i] -= lenRemain[0]  
#         lenRemain.pop(0)
#         onBridgeTruck.pop(0)   
    
#     answer = time
#     return answer

# print(solution(bridge_length1, weight1, truck_weights1))
# print(solution(bridge_length2, weight2, truck_weights2))
# print(solution(bridge_length3, weight3, truck_weights3))

# ----------1차 오답 -- [11], [101], [965]
# 시도
# - 선두 트럭이 이동한 거리만큼 뒤따르는 트럭들도 똑같은 거리를 차감
# 문제
# - for i in range(len(lenRemain)) : lenRemain[i] -= lenRemain[0] 
# - 위의 식을 사용하면 lenRemain[0] 의 값이 0으로 저장되어 그 뒤의 값들은 아무 변화가 없음
# ----------------------------------------------------------------------------------------

# bridge_length1 , bridge_length2 , bridge_length3 = 2 ,         100 ,   100
# weight1 ,        weight2 ,        weight3        = 10 ,        100 ,   100
# truck_weights1 , truck_weights2 , truck_weights3 = [7,4,5,6] , [10] , [10,10,10,10,10,10,10,10,10,10]  # 10대

# def solution(bridgeLen, bridgeWeight, truckWeight):
#     time = 0              # 전부 건너는 데 걸리는 시간
#     onBridgeTruck = []    # 다리 위 트럭들의 큐
#     lenRemain = []        # 각 트럭이 건너야 할 남은 길이의 큐 (각각 건너는데 필요한 시간)

#     while len(truckWeight) != 0:     # 모든 대기 트럭이 다리 위에 올라갈 때까지 반복
#         if ((sum(onBridgeTruck[:]) + truckWeight[0]) <= bridgeWeight) and (bridgeLen > len(onBridgeTruck)): 
# # { [다리 위 트럭들의 무게]+[다음 트럭의 무게]가 [다리가 견딜 수 있는 무게]와 같거나 가벼우면 and [다리길이]가 [다리 위 트럭들의 길이]보다 길면 } = (트럭이 더 올라올수 있으면)
            
#             if len(lenRemain) != 0:     # 다리 위에 트럭이 있으면 
#                 for i in range(len(lenRemain)):
#                     lenRemain[i] -= 1   # 남은 길이가 1씩 감소 (이동하는 중)      
#             onBridgeTruck.append(truckWeight[0])   # 다음 트럭이 올라옴
#             time += 1             # 올라오면 1초가 경과                                              
#             lenRemain.append(bridgeLen)  # 올라온 트럭이 건너야 할 길이 추가 (건너는데 필요한 시간)     
#             truckWeight.pop(0)    # 올라온 트럭을 대기트럭 큐에서 꺼냄

#         else :      # 다음 트럭이 올라올 수 없으면 
#             time += (lenRemain[0])  # 선두 트럭이 남은 길이를 이동 = 이동한 만큼 시간이 경과
#             for i in range(len(lenRemain)-1,0,-1):     
#                 lenRemain[i] -= lenRemain[0]  # 모든 트럭에 이동한만큼 남은 거리를 차감 
#             lenRemain.pop(0)
#             onBridgeTruck.pop(0)    # 선두 트럭 통과
      
#     while len(onBridgeTruck) != 0:   # 대기 트럭이 없을 때, 다리 위 트럭들이 모두 건널 때까지 반복
#         time += (lenRemain[0]) 
#         for i in range(len(lenRemain)-1,0,-1):     
#             lenRemain[i] -= lenRemain[0]  
#         lenRemain.pop(0)
#         onBridgeTruck.pop(0)   
    
#     answer = time
#     return answer

# print(solution(bridge_length1, weight1, truck_weights1))
# print(solution(bridge_length2, weight2, truck_weights2))
# print(solution(bridge_length3, weight3, truck_weights3))

# ----------2차 오답 -- [10], [101], [110]
# 시도
# - 대기 트럭이 다리에 올라올 때마다 1을 추가하여 앞의 트럭이 진행하도록 식을 구현
# 문제
# - 무게 제한으로 트럭들이 한꺼번에 올라오지 못했을 때 계산 오류가 발생
# - 다리 위의 선두 트럭이 다리를 건너서 내려가면, 동시에 대기 트럭이 다리에 올라와야 하는데(무게제한에 걸리지 않으면), 올라오기 전에 다리위의 트럭들을 1씩 이동시켜버려 새로운 트럭과 1초의 공백이 추가
# ----------------------------------------------------------------------------------------

# 문제 해석 오류 

# 문제 해석
# 앞 쪽의 트럭들이 먼저 나가야 하므로, 큐의 방식을 적용해본다
# 입출력 예 첫 번째에서 7kg의 트럭이 다리 위에 있던 시간은 1, 2초 이고, 다리를 완전히 건너면 3초가 된다
# 고로 [다리길이+1]이 다리를 건너기 위한 [기본 시간]이다 
# ---- 이 부분 해석에서 [다리길이+1]이 아닌 [다리길이]로 수정
# ---- 3초는 마지막 차량이 통과하고 +1 한 것으로 보아야 한다 
# ---- 왜냐하면 다리 위에 있던 시간이 2초이고, 2초가 경과하고 나서 [측정하는 순간의 시간]이 3초이기 때문이다

# [다리길이]를 [기본 시간]으로 할 경우 (측정시간 고려)
# 0	        []	                []          	[7,4]
# 1     	[]              	[7]         	[4]
# 2     	[]              	[7]         	[4]
# ------------------------------------------------------------ 7 트럭이 이동한 시간 (2초)
# 3	        [7]	                [4]	            []      ------ 7 트럭이 건너는 데 걸린 시간 (3초)
# 4	        [7]	                [4]	            []
# ------------------------------------------------------------ 4 트럭이 이동한 시간 (2초)
# 5	        [7,4]	            []	            []      ------ 7,4 트럭이 건너는 데 걸린 시간 (5초)
# ----------------------------------------------------------------------------------------
# [다리길이+1]을 [기본 시간]으로 할 경우 (측정시간은 고려하지 않음)
# 0	        []	                []          	[7,4]
# 1     	[]              	[7]         	[4]
# 2     	[]              	[7]         	[4]
# 3	        []	                [7]	            []   
# ------------------------------------------------------------ 7 트럭이 이동한 시간 = 7 트럭이 건너는 데 걸린 시간 (3초)
# 4	        [7]	                [4]	        []
# 5	        [7]	                [4]	        []     
# 6  	    [7]  	            [4]	        []
# ------------------------------------------------------------ (7 트럭이 이동한 시간 + 4 트럭이 이동한 시간) = 7,4 트럭이 건너는 데 걸린 시간 (6초)

# => 측정시간을 고려해서 식을 다시 구상해본다 
# ----------------------------------------------------------------------------------------

bridge_length1 , bridge_length2 , bridge_length3 = 2 ,         100 ,   100
weight1 ,        weight2 ,        weight3        = 10 ,        100 ,   100
truck_weights1 , truck_weights2 , truck_weights3 = [7,4,5,6] , [10] , [10,10,10,10,10,10,10,10,10,10]  # 10대

def solution(bridgeLen, bridgeWeight, truckWeight):
    time = 0              # 전부 건너는 데 걸리는 시간
    onBridgeTruck = []    # 다리 위 트럭들의 큐
    lenRemain = []        # 각 트럭이 건너야 할 남은 길이의 큐 (각각 건너는데 필요한 시간)

    while len(truckWeight) != 0:     # 모든 대기 트럭이 다리 위에 올라갈 때까지 반복
        if ((sum(onBridgeTruck[:]) + truckWeight[0]) <= bridgeWeight) and (bridgeLen > len(onBridgeTruck)): 
# { [다리 위 트럭들의 무게]+[다음 트럭의 무게]가 [다리가 견딜 수 있는 무게]와 같거나 가벼우면 and [다리길이]가 [다리 위 트럭들의 길이]보다 길면 } = (트럭이 더 올라올 수 있으면)
            onBridgeTruck.append(truckWeight[0])   # 다음 트럭이 올라옴

            # time += 1 # 올라오면 1초가 경과---- 삭제                                           
            lenRemain.append(bridgeLen)  # 올라온 트럭이 건너야 할 길이 추가 (건너는데 필요한 시간)

            truckWeight.pop(0)    # 올라온 트럭을 대기트럭 큐에서 꺼냄

            if len(lenRemain) != 0:     # 다리 위에 트럭이 있으면 
                for i in range(len(lenRemain)):
                    lenRemain[i] -= 1   # 남은 길이가 1씩 감소 (이동하는 중)       
                time += 1 #---- 추가 - 이동한 만큼 시간이 경과     

        else :      # 다음 트럭이 올라올 수 없으면 
            time += (lenRemain[0])  # 선두 트럭이 남은 길이를 이동 = 이동한 만큼 시간이 경과
            for i in range(len(lenRemain)-1,0,-1):     
                lenRemain[i] -= lenRemain[0]  # 모든 트럭에 이동한만큼 남은 거리를 차감 
            lenRemain.pop(0)
            onBridgeTruck.pop(0)    # 선두 트럭 통과
      
    while len(onBridgeTruck) != 0:   # 대기 트럭이 없을 때, 다리 위 트럭들이 모두 건널 때까지 반복
        time += (lenRemain[0]) 
        for i in range(len(lenRemain)-1,0,-1):     
            lenRemain[i] -= lenRemain[0]  
        lenRemain.pop(0)
        onBridgeTruck.pop(0)   

    time += 1 #---- 추가 - 마지막 트럭이 통과하고 측정하는 시간대 추가 
    
    answer = time
    return answer

print(solution(bridge_length1, weight1, truck_weights1))
print(solution(bridge_length2, weight2, truck_weights2))
print(solution(bridge_length3, weight3, truck_weights3))

# return1 = 8
# return2 = 101
# return3 = 110

# 프로그래머스 코드정확도 채점 - 합계: 71.4 / 100.0
# 문제 해석하는 능력을 더 길러보자 
# 코드를 축약하지 않고 일부러 풀어서 썼는데, 단순하게 짜는 방법 생각해보기 