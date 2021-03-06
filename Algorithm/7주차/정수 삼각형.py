문제 설명
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.



def solution(triangle):
    answer = 0
    # triangle_copy = [] + triangle[:]  # 원본 보존을 위해 copy()를 여러 방법으로 수행했지만 값이 동기화됨
    # list 내부에 list 형식으로 선언되어 있어 내부 주소 값을 공유하기 때문에 발생하는 문제

    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            left = triangle[row][col] + triangle[row + 1][col]
            right = triangle[row][col] + triangle[row + 1][col + 1]
            triangle[row][col] = left if left > right else right
            
    answer = triangle[0][0]
            
    # print(id(triangle_copy))
    # print(triangle_copy)
    # print(id(triangle))
    # print(triangle)
    
    # sum_list = [triangle[0]]
    
    # 하향식 요소 4개부터 값이 틀어짐
#     for row in range(1, len(triangle)):
#         temp = []
#         row_len = len(triangle[row])

#         for col in range(pow(2, row_len)):
#             if col != 0:
#                 temp.append(triangle[row][col] + sum_list[row - 1][col - 1])
#             if col != row_len - 1:
#                 temp.append(triangle[row][col] + sum_list[row - 1][col])

#         sum_list.append(temp)
#     print(sum_list)
#     answer = max(sum_list[-1])

    return answer
