문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.



# 문제 자체는 이분탐색을 의도한 것이지만, dict를 통한 해결이 더 효율적이라 판단
card1_cnt = input()
card1_list = input()
card1_list = card1_list.split(' ')  # 공백으로 구분하여 배열로 저장
card2_cnt = input()
card2_list = input()
card2_list = card2_list.split(' ')
answer = ''
card1_dict = {} # 각 요소별 중복 수 저장

# dict에 값이 없으면 1, 값이 있으면 +1
for x in card1_list:
    if card1_dict.get(x) is None: card1_dict[x] = 1
    else: card1_dict[x] += 1
        
for x in card2_list:
    answer += ' '
    if card1_dict.get(x) is None: answer += '0' # dict에 값이 없는 경우 0 추가
    else: answer += str(card1_dict[x])
        
print(answer[1:]) # 반복문에서 값의 앞에 공백을 넣기 때문에 필요없는 첫 공백을 제거한 내용부터 출력
