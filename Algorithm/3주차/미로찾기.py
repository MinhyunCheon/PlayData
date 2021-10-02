map = [[0, 0, 0, 0, 0, 0]
       , [1, 0, 1, 1, 1, 0]
       , [0, 0, 1, 0, 1, 0]
       , [0, 1, 1, 0, 0, 0]
       , [0, 0, 1, 1, 1, 1]
       , [1, 0, 0, 0, 0, 0]]

# 탈출할 수 있는 미로인 경우 True, 아닌 경우 False 리턴
def check_map(map):
    x_idx = 0
    y_idx = 0
    stack = []
    max_idx = len(map) - 1
    
    # 시작 점이 이동 불가능한 지역인 경우 즉시 종료
    if map[0][0] == 1: return False
    
    while(True):
        # 회귀를 방지하기 위해 현재 위치를 이동 불가능한 상태로 변경
        map[x_idx][y_idx] = 1
        # 우측 방향 검사
        if y_idx < max_idx and map[x_idx][y_idx + 1] == 0: stack.append([x_idx, y_idx + 1])
        # 아래 방향 검사
        if x_idx < max_idx and map[x_idx + 1][y_idx] == 0: stack.append([x_idx + 1, y_idx])
        # 좌측 방향 검사
        if y_idx > 0 and map[x_idx][y_idx - 1] == 0: stack.append([x_idx, y_idx - 1])
        # 위 방향 검사
        if x_idx > 0 and map[x_idx - 1][y_idx] == 0: stack.append([x_idx - 1, y_idx])
        
        # stack에 내용이 없는 경우, 이동이 불가하기 때문에 종료
        if len(stack) == 0: return False
        # 스택의 마지막 값을 가져와 idx에 반영
        else:
            stack_idx = stack.pop()
            x_idx = stack_idx[0]
            y_idx = stack_idx[1]
        
        # map의 최종 위치에 도착한 경우 성공 처리
        if x_idx == max_idx and y_idx == max_idx: return True
