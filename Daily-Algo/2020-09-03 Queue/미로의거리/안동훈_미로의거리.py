import sys
sys.stdin = open('미로의거리_input.txt')

# 간단한 bfs 문제 풀이
# 방향을 위한 보조 배열
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, maze, dist):
    queue = []
    dist[x][y] = 0
    cx, cy = x, y
    queue.append((cx, cy))
    while True: # queue가 빌 때까지 돌리기

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 범위를 벗어나지 않았으며, 벽이 아니고, 이미 방문한 곳이 아닐때,
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[cx][cy] + 1
                queue.append((nx,ny))
                if maze[nx][ny] == 3: # 도착할 경우 곧장 return
                    return
        if len(queue) == 0:
            break
        if len(queue) != 0:
            cx, cy = queue.pop(0)


# 0은 통로, 1은 벽, 2는 출발, 3은 도착이다.
T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    n = int(input())
    # maze 이차원 배열 선언 및 입력
    maze = [list(map(int, input())) for _ in range(n)]
    # 방문 처리 + 최소 거리를 위한 배열 선언
    dist = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2: # 출발 장소 구하기
                bfs(i, j, maze, dist)
                break

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 3: # 도착 장소 구하기
                answer = dist[i][j] - 1
                break

    # 도착 지점에 방문 하는 지 안하는 지 여부 판단
    if answer < 0:
        answer = 0
        print("#{0} {1}".format(test_case, answer))
    else:
        print("#{0} {1}".format(test_case, answer))

