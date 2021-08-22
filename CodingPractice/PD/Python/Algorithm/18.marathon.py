# 18. 완주하지 못한 선수 / 해시
# https://programmers.co.kr/learn/courses/30/lessons/42576

# ----------------------------------------------------------------------------------------

# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

# 입출력 예 
# participant	                                          completion	                            return
# ["leo", "kiki", "eden"]                           	["eden", "kiki"]	                        "leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"] 	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]             	["stanko", "ana", "mislav"]             	"mislav"

# 입출력 예 설명
# 예제 #1
# "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #2
# "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #3
# "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.


# ----------------------------------------------------------------------------------------

# 문제 해석
# 배열 participant에는 모든 선수들의 이름이 들어있고, 배열 completion에는 participant 선수들 중 한 명이 없다
# completion에 없는 한 명의 선수이름을 return으로 구해야 한다 

# 접근 방법
# 두 배열의 원소들을 비교하면 선수 이름을 쉽게 찾을 수 있지만, 동명이인일 경우를 생각해야 한다.
# 동명이인의 선수가 있다면 [참가한 순서 = index] 값으로 구분해야 하므로, [해시 = dictionary]를 이용한다.
# key-value를 어떤 것으로 삼을지 고민해본다.

# ----------------------------------------------------------------------------------------

participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]

participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]

participant3 = ["mislav", "stanko", "mislav", "ana"]
completion3 = ["stanko", "ana", "mislav"]  

def solution(participant, completion):
    answer = ''
    ptHash = dict()
    
    for i in range(len(participant)):
       ptHash[i] = participant[i]
    
    for i in completion:
        if i in ptHash.values():
            key = [k for k,v in ptHash.items() if v == i]
            del ptHash[key[0]]

    answer = [v for v in ptHash.values()]
    
    return answer[0]

print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))

# return "leo"
# return "vinko"
# return "mislav"

# ----------------------------------------------------------------------------------------

# 프로그래머스 코드정확도 채점 - 정확성 : 50.0, 효율성 0.0, 합계: 50.0 / 100.0
# 참고 사이트 : 
# https://wikidocs.net/16#key-in
# https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=222007663089



