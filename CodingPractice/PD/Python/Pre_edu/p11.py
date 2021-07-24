# 11. 행렬의 덧셈 / 행과 열의 크기가 같은 두 행렬 더하기

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

arr3 = [[1],[2]]
arr4 = [[3],[4]]

a1 = [[1,2],[3,4],[5,6]]
a2 = [[1,2],[3,4],[5,6]]

def solution(A1, A2):
    a = []
    answer = []
    for i in A1:
        for j in i:
            j = j + A2[A1.index(i)][i.index(j)]
            a.append(j)
        answer.append(a)
        a = []

    return answer

print(solution(a1,a2))

# def solution(A1, A2):
#     a = []
#     answer = []
#     for i in range(len(A1)):
#         for j in i:
#             answer[i][j].append(a)

#     return answer

# answer = [[A1[0][0] + A2[0][0] , A1[0][1] + A2[0][1]] , [A1[1][0] + A2[1][0] , A1[1][1] + A2[1][1]]]

#한 줄로 풀어보기 
