# 6.같은 숫자는 싫어 / 연속되는 숫자는 하나만 남기고 모두 제거 / 제거되더라도 남은 숫자들의 배열 순서는 유지 

arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]

def solution(arr):
    answer = []
    answer.append(arr[0])
    i = 0
    for x in arr:
        if x != answer[i]:
            answer.append(x)           
            i = i + 1
    return answer

print(solution(arr1))






