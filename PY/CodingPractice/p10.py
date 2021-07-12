# 10. 평균 구하기 / 정수를 담고 있는 배열 arr의 평균값을 리턴 / 한줄로 풀어보기 

arr1 = [1,2,3,4]
arr2 = [5,5]

def solution(arr):
    answer = sum(arr[0:-1],arr[-1])/len(arr)
    return answer

# sum(arr[0:-1],arr[-1]) = sum(arr)

