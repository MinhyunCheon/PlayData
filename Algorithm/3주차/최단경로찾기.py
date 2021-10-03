# 영상에 제시된 LinkedList를 dict로 구현
linked_dict[1] = {'linked' : [2, 5, 6]}
linked_dict[2] = {'linked' : [1, 3, 11]}
linked_dict[3] = {'linked' : [2, 6, 7, 8]}
linked_dict[4] = {'linked' : [8, 12]}
linked_dict[5] = {'linked' : [1, 6, 9, 11]}
linked_dict[6] = {'linked' : [1, 3, 5, 12]}
linked_dict[7] = {'linked' : [3, 8, 10]}
linked_dict[8] = {'linked' : [3, 4, 7, 11]}
linked_dict[9] = {'linked' : [5, 10]}
linked_dict[10] = {'linked' : [7, 9]}
linked_dict[11] = {'linked' : [2, 5, 8]}
linked_dict[12] = {'linked' : [4, 6]}

def get_distance_cost(linked_dict, start, end):
    end_idx = end
    now_idx = start
    same_distance_cnt = 0 # 같은 레벨의 요소의 수 저장
    cost = 0 # 최단 거리 cost
    queue = [] # 요소를 저장할 list 선언

    while(True):
    #     queue.append([x for x in linked_dict[now_idx]['linked']]) # 배열로 요소가 저장되어 원하는 값을 얻지 못함
        # 현재 요소와 연결된 요소를 queue에 저장, 이미 queue에 포함된 값은 제외
        # 제시된 LinkedList는 거미줄처럼 연결되어 있기 때문에 이미 탐색한 요소의 값이 queue에 추가될 가능성 존재, 이에 대한 추가 처리 필요
        for x in linked_dict[now_idx]['linked']:
            if not x in queue: queue.append(x)

        # 현재 레벨의 요소를 모두 검사하면, same_distance_cnt를 현재 queue의 길이로 갱신하고 cost 1 증가
        if same_distance_cnt == 0:
            same_distance_cnt = len(queue)
            cost += 1

        # 현재 탐색 요소가 도착점과 같다면, 현재 cost를 반환
        # 도착점이 아닌 경우, queue의 첫번째 요소를 꺼내고 same_distance_cnt 1 감소
        if queue[0] == end_idx: return cost
        else:
            now_idx = queue.pop(0)
            same_distance_cnt -= 1
            
get_distance_cost(linked_dict, 1, 12)
