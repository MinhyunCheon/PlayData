문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.



from collections import deque

stack = []
queue = deque() # 속도 향상을 위해 deque 사용
linked_dict = {}

# 입력 정보 저장
input_1 = input().split(' ')
start = int(input_1[2])
now = start
input_len = int(input_1[1])
node_cnt = int(input_1[0]) # 노드 수 저장, 모든 노드를 탐색한 경우 즉시 종료
search_complete_list = [] # 탐색한 노드 저장

for idx in range(0, input_len):
    input_2 = input().split(' ')
    # int로 형변환을 하지 않는 경우 정렬이 의도대로 되지 않음
    key = int(input_2[0])
    value = int(input_2[1])

    # 양방향 리스트이므로 key와 value를 저장한 뒤, 순서를 반전하여 값 저장
    if linked_dict.get(key) is None: linked_dict[key] = [value]
    elif not value in linked_dict.get(key): linked_dict[key].append(value)

    if linked_dict.get(value) is None: linked_dict[value] = [key]
    elif not key in linked_dict.get(value): linked_dict[value].append(key)
     
# DFS
while True:
    # node의 연결정보가 있는 경우만 실행, 탐색한 노드에 없는 노드만 stack에 추가
    if linked_dict.get(now) is not None:
        for x in sorted(linked_dict[now], reverse = True):
            if x in search_complete_list: continue
            stack.append(x)

    # 현재 노드가 탐색 리스트에 없는 경우 추가
    if not now in search_complete_list: search_complete_list.append(now)
    
    # 스택이 비어있거나, 모든 노드를 탐색한 경우 정답 출력 후 종료
    if not stack or len(search_complete_list) == node_cnt:
        print(' '.join(list(map(str, search_complete_list))))
        break

    if stack: now = stack.pop() # stack에 내용이 있는 경우 pop()

# 비교 변수 초기화
search_complete_list.clear()
now = start
        
# BFS
while True:
    if linked_dict.get(now) is not None:
        for x in sorted(linked_dict[now]):
            if x in search_complete_list: continue
            queue.append(x)
 
    if not now in search_complete_list: search_complete_list.append(now)

    if not queue or len(search_complete_list) == node_cnt:
        print(' '.join(list(map(str, search_complete_list))))
        break

    if queue: now = queue.popleft()
