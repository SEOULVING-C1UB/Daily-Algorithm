# 좌 우 상 하를 순회하면서 cost를 갱신하면서 stack에 쌓고 진행
import collections


movement = [[1, 0], [-1, 0], [0, -1], [0, 1]]
INF = 9999999


for TC in range(int(input())):
    N = int(input())
    mountain = [list(map(int, input().split())) for i in range(N)]
    move_table = [[INF] * N for i in range(N)]
    positions = collections.deque()     # queue
    positions.append((0, 0))
    move_table[0][0] = 0
    while positions:
        x, y = positions.popleft()
        for move in movement:   # 우 좌 상 하를 이동하면서
            nx, ny = x + move[0], y + move[1]
            if -1 < nx < N and -1 < ny < N:     # 맵을 벗어나지 않을 경우
                cost = 1    # 기본 코스트 1
                if mountain[ny][nx] > mountain[y][x]:   # 더 높은 곳으로 이동해야 한다면
                    cost += mountain[ny][nx] - mountain[y][x]   # 해당 차이만큼 기본 코스트에 추가
                if move_table[ny][nx] > move_table[y][x] + cost:    # 앞서 기록해둔 코스트보다 작다면
                    move_table[ny][nx] = move_table[y][x] + cost    # 해당 코스트를 기록한다.
                    positions.append((nx, ny))
    print('#{} {}'.format(TC + 1, move_table[N - 1][N - 1]))


##### 좀만 더 다듬으면 되겠다
    # while not visit[N - 1][N - 2] or not visit[N - 2][N - 1]:  # N-1, N-1의 주변을 전부 방문하기 전까지
    #     # for (x, y) in positions:
    #         # leftX, leftY = now[0] + 1, now[1]
    #     x, y = positions.popleft()
    #     if not visit[y][x]:
    #         visit[y][x] = 1
    #         for move in movement:
    #             nextX, nextY = x + move[0], y + move[1]
    #             if -1 < nextX < N and -1 < nextY < N:
    #                 if not visit[nextY][nextX]:
    #                     if mountain[nextY][nextX] > mountain[y][x]:
    #                         if move_table[nextY][nextX] > move_table[y][x] + mountain[nextY][nextX] - mountain[y][x] + 1:
    #                             move_table[nextY][nextX] = move_table[y][x] + mountain[nextY][nextX] - mountain[y][x] + 1
    #                     else:
    #                         if move_table[nextY][nextX] > move_table[y][x] + 1:
    #                             move_table[nextY][nextX] = move_table[y][x] + 1
    #                     if (nextX, nextY) not in positions:
    #                         positions.append((nextX, nextY))
    # print('#{} {}' .format(TC+1, move_table[N - 1][N - 1]))


##### 우 하만 살펴보니 일부는 더 크게 나옴
# movement = [[1, 0], [0, 1]]
# for TC in range(int(input())):
#     N = int(input())
#     mountain = [list(map(int, input().split())) for i in range(N)]
#     stack = [(0, 0, mountain[0][0], 0)]    # x, y, height, cost
#     min_cost = 999999
#     while stack:
#         x, y, height, cost = stack.pop()
#         if cost >= min_cost - 1:
#             continue
#         height_diff = 1000
#         for move in movement:
#             nextX, nextY = x + move[0], y + move[1]
#             if -1 < nextX < N and -1 < nextY < N:
#                 if abs(height - mountain[nextY][nextX]) < height_diff:
#                     height_diff = abs(height - mountain[nextY][nextX])
#         for move in movement:
#             nextX, nextY = x + move[0], y + move[1]
#             if nextX == N - 1 and nextY == N - 1:
#                 if min_cost > cost + 1 + height_diff:
#                     min_cost = cost + 1 + height_diff
#                 continue
#             if -1 < nextX < N and -1 < nextY < N:
#                 if abs(height - mountain[nextY][nextX]) == height_diff:
#                     stack.append((nextX, nextY, mountain[nextY][nextX], cost + 1 + height_diff))
#     print('#{} {}' .format(TC+1, min_cost))
