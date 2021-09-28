문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.



# 스택/큐를 활용한 다른 방식으로의 접근을 생각해봤으나 이점을 찾지 못해 중첩 반복문으로 진행
def solution(prices):
    answer = []
    prices_len = len(prices)    # len 함수 중복 호출을 막기 위해 변수에 저장(Java에서 쓰던 방식)
    
    for idx in range(0, prices_len):
        sec = 0 # 각 인덱스의 가격마다 가격이 떨어지지 않은 초기 시간 0 설정
        for idx2 in range(idx+1, prices_len):   # 비교 대상 수의 다음 인덱스부터 마지막까지 비교
            sec += 1
            if prices[idx] > prices[idx2]: break;   # 가격이 떨어진 순간 해당 인덱스에 대한 반복 종료
        answer.append(sec)  # 결과를 answer에 입력
        
    return answer
