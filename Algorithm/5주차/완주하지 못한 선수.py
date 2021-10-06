문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.



def solution(participant, completion):
    # dict에 참가자 목록을 저장한 뒤, 완주한 목록을 탐색하며 값 감소
    player_dict = {}
    for x in participant: player_dict[x] = player_dict[x] + 1 if x in player_dict else 1
    for x in completion: player_dict[x] = player_dict[x] - 1
    
    # 단 한명의 선수를 제외하고 모두 완주했기 때문에 값으로 내림차순 정렬하면 첫번째 값이 정답
    player_dict = sorted(player_dict.items(), key = lambda x : -x[1])
    answer = player_dict[0][0]
    
    return answer
