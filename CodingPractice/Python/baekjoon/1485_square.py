# 정사각형
# https://www.acmicpc.net/problem/1485

# ---------문제 설명----------------------------------------------------------------------
'''
문제
네 점이 주어졌을 때, 네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스는 네 줄로 이루어져 있으며, 점의 좌표가 한 줄에 하나씩 주어진다. 
점의 좌표는 -100,000보다 크거나 같고, 100,000보다 작거나 같은 정수이다. 
같은 점이 두 번 이상 주어지지 않는다.

출력
각 테스트 케이스마다 입력으로 주어진 네 점을 이용해서 정사각형을 만들 수 있으면 1을, 없으면 0을 출력한다.

예제 입력 1 
2
1 1
1 2
2 1
2 2
2 2
3 3
4 4
5 5

예제 출력 1 
1
0

'''

# ---------문제 해석----------------------------------------------------------------------
'''
점 네개가 순서대로 입력되지 않고, 무작위로 입력된다고 가정

'''

# ---------접근 방법----------------------------------------------------------------------
'''
점과 점 사이 좌표값 차이를 이용
점이 대각선으로 주어졌을 때를 대비한다 

'''
# ----------------------------------------------------------------------------------------
import sys

def solution():
	def input():
		caseNum = int(sys.stdin.readline())
		caseCount, caseList = 0, []
		while caseCount < caseNum:
			vertexCount = 0
			case = []
			while vertexCount < 4:
				case.append(list(map(int, sys.stdin.readline().split())))
				vertexCount += 1
			caseList.append(sorted(case))
			caseCount += 1
		return caseList

	caseList = input()
	answer = []

	for case in caseList:
		if abs(case[0][0]-case[3][0]) + abs(case[0][1]-case[3][1]) == \
					abs(case[1][0]-case[2][0]) + abs(case[1][1]-case[2][1]):

			distance = abs(case[0][0]-case[1][0]) + abs(case[0][1]-case[1][1])

			if abs(case[1][0]-case[3][0]) + abs(case[1][1]-case[3][1]) != distance or \
				abs(case[2][0]-case[3][0]) + abs(case[2][1]-case[3][1]) != distance:
				answer.append(0)
			
			else:
				answer.append(1)

		else:
			answer.append(0)


	print(*answer, sep="\n")
	

solution()

# ------------------------ 오답 -----------------------------------------------------------
'''
틀린풀이:
한 꼭지점의 좌표를 구하고, 나머지 꼭지점의 3개의 좌표를 고정된 값으로 구함

오답이유:
사각형이 회전한다는 생각을 하지 못함 

정답풀이:
1. 네 개의 좌표 정렬 (x좌표로 먼저 정렬 후, y좌표로 정렬)
2. 네 개의 꼭지점사이의 거리를 각각 비교 (첫 번쨰-두 번째, 두 번째-네 번째, 두 번째- 세 번째)
3. 대각선 꼭지점사이의 거리를 비교 (첫 번째-네 번째, 두 번째-세 번째) 


'''

# ---------------------------------------------------------------------------------------
'''
import sys


def solution():
	def input():
		caseNum = int(sys.stdin.readline())
		caseCount, caseList = 0, []
		while caseCount < caseNum:
			vertexCount = 0
			case = []
			while vertexCount < 4:
				case.append(list(map(int, sys.stdin.readline().split())))
				vertexCount += 1
			caseList.append(case)
			caseCount += 1
		return caseList


	caseList = input()
	
	# caseList = [[[1, 1], [3, 1], [1, 3], [2, 2]], [[1, 1], [4, 1], [1, 4], [2, 2]]]
	
	answer = []

	for vertexList in caseList:
		isSquare = False
		minX, minY = sys.maxsize, sys.maxsize
		length = 0
		for vertex in vertexList:
			if minX > vertex[0]:
				minX = vertex[0]
			if minY > vertex[1]:
				minY = vertex[1]

		if [minX, minY] in vertexList:
			count = 0
			for vertex in vertexList:
				if (vertex[0] == minX) and (vertex[1] != minY):
					length = vertex[1] - minY
					break
			for vertex in vertexList:
				if vertex == [minX, minY]:
					continue
				elif vertex == [minX, minY+length]:
					count += 1
				elif vertex == [minX+length, minY+length]:
					count += 1
				elif vertex == [minX+length, minY]:
					count += 1
				else:
					break
			if count >= 3:
				isSquare = True

		if isSquare:
			answer.append(1)

		else:
			X, Y, count = minX, 0, 0
			for vertex in vertexList:
				if vertex[0] == X:
					Y = vertex[1]
					break

			for vertex in vertexList:
				if (vertex[0] != X) and (vertex[1] == Y):
					length = (vertex[0] - X) / 2
					break

			for vertex in vertexList:
				if vertex == [X, Y]:
					continue
				elif vertex == [X+length, Y-length]:
					count += 1
				elif vertex == [X+length, Y+length]:
					count += 1
				elif vertex == [X+(length*2), Y]:
					count += 1
				else:
					break
			if count >= 3:
				answer.append(1)
			else:
				answer.append(0)

	print(*answer, sep="\n")

solution()

'''

# ----------------------------------------------------------------------------------------