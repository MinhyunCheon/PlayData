문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.



# 각 수포자의 정답 패턴을 배열로 저장한 뒤 개별 점수 체크
def solution(answers):
    answer = []
    
    # 정답 패턴 저장
    u1 = [1, 2, 3, 4, 5]
    u2 = [2, 1, 2, 3, 2, 4, 2, 5]
    u3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 패턴의 마지막 체크를 위해 변수 선언
    u1_len = len(u1)
    u2_len = len(u2)
    u3_len = len(u3)
    # 패턴의 길이가 상이하기 때문에 개별 인덱스 적용
    u1_index = 0
    u2_index = 0
    u3_index = 0
    score_dict = {'1' : 0, '2' : 0, '3' : 0}    # 각 수포자의 데이터는 dict로 저장
    max_score = 0   # 최고 득점자를 판별하기 위해 점수 값 저장
    
    for x in answers:
        # 정답을 맞춘 수포자의 점수 증가
        if u1[u1_index] == x: score_dict['1'] += 1
        if u2[u2_index] == x: score_dict['2'] += 1
        if u3[u3_index] == x: score_dict['3'] += 1
        
        # 다음 정답을 참조하기 위해 인덱스 값 증가
        u1_index += 1
        u2_index += 1
        u3_index += 1
        
        # 인덱스가 len의 값과 같은 경우 마지막 정답을 참조했으므로 인덱스 초기화
        if u1_index == u1_len: u1_index = 0
        if u2_index == u2_len: u2_index = 0
        if u3_index == u3_len: u3_index = 0
            
    # 기존 최고 값 구하는 로직
    # for key, value in score_dict.items():
    #     if max_score < value: max_score = value
    
    # 반복문을 사용하지 않고 정렬 방식으로 변경
    max_score = sorted(score_dict.items(), key = lambda x : -x[1])[0][1]
            
    # 최고 득점한 사용자들을 answer에 저장
    for key, value in score_dict.items():
        if max_score == value: answer.append(int(key))
    
    return answer
