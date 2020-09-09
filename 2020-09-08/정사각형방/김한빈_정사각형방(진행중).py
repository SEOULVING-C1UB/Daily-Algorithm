import sys

def check(r, c):
    visited = [[0]*N for _ in range(N)]
    stack = []
    stack.append((r, c))
    visited[r][c] = 1
    while stack:
        a, b = stack.pop()
        for i in range(4):
            x = a + dr[i]
            y = b + dc[i]
            if 0 <= x < N and 0 <= y < N:
                if arr[x][y] == arr[a][b] + 1 and not visited[x][y]:
                    visited[x][y] = visited[a][b] + 1
                    stack.append((x, y))
    return visited[a][b]


# #1
# def check(arr, r, c, n):
#     dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
#     visited[r][c] = n # 방에 이동횟수 저장
#     for i in range(4):
#         if 0 <= (r + dr[i]) < len(arr) and 0 <= (c + dc[i]) < len(arr[0]):
#             if arr[r + dr[i]][c + dc[i]] == arr[r][c] + 1: # 상하좌우 확인해서 +1인 방 찾기
#                 if visited[r + dr[i]][c + dc[i]] != 0: # 이미 방문했던 방일 경우
#                     return n + visited[r + dr[i]][c + dc[i]] # 저장된 이동횟수 + 지금까지 이동한 횟수 n 후 리턴
#                 else:
#                     n += 1 # 이동횟수 추가
#                     r = r + dr[i] # 이동
#                     c = c + dc[i] # 이동
#                 return check(arr, r, c, n) # 이동해서 재탐색
#     return n # 상하좌우 해당 사항 없을 경우 이동횟수 리턴

#2
# def check(r, c, n):
#     dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
#     flag = [1, 0, 0, 0]
#     while len([f for f in flag if f == 1]) > 0:
#         flag = [0, 0, 0, 0]
#         visited[r][c] = n  # 방에 이동횟수 저장
#         for i in range(4):
#             if 0 <= (r + dr[i]) < len(arr) and 0 <= (c + dc[i]) < len(arr[0]):
#                 if arr[r + dr[i]][c + dc[i]] == arr[r][c] + 1: # 상하좌우 확인해서 +1인 방 찾기
#                     flag[i] = 1
#                     if visited[r + dr[i]][c + dc[i]] != 0: # 이미 방문했던 방일 경우
#                         return n + visited[r + dr[i]][c + dc[i]] # 저장된 이동횟수 + 지금까지 이동한 횟수 n 후 리턴
#                     else:
#                         n += 1 # 이동횟수 추가
#                         r = r + dr[i] # 이동
#                         c = c + dc[i] # 이동
#                         continue
#                 else:
#                     flag[i] = 0
#             else:
#                 flag[i] = 0
#     return n # 상하좌우 해당 사항 없을 경우 이동횟수 리턴



sys.stdin = open('정사각형 방.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
    result = 1 # 이동횟수 저장
    room = N ** 2 + 1 # 최대 방 번호  + 1
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            # visited = [[0] * N for _ in range(N)]
            n = check(r, c)
            # print(n)
            if n > result:
                result = n
                room = arr[r][c]
            elif n == result:
                if room > arr[r][c]:
                    room = arr[r][c]
    print(room, result)





