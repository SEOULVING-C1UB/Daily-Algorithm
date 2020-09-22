T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    result = 0
    visited = [[0] * N for _ in range(N)]

    # 출발점, 도착점
    start_index = []
    end_index = []

    # maze 순회하며 출발점, 도착점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_index.append(i)
                start_index.append(j)
            if maze[i][j] == 3:
                end_index.append(i)
                end_index.append(j)

    # 네 방향
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    # 네 방향으로 순회, 방문했던 곳은 스킵
    def go(y, x):
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            # 배열의 인덱스 범위 내인지, 방문했는지 체크
            if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x]:
                # 도착점에 도착했을 때
                if maze[new_y][new_x] == 3:
                    visited[new_y][new_x] = 1
                    return

                # 그냥 길일 때
                if maze[new_y][new_x] == 0:
                    visited[new_y][new_x] = 1
                    go(new_y, new_x)

    # 시작점 방문
    visited[start_index[0]][start_index[1]] = 1
    go(start_index[0], start_index[1])

    # 도착점에 방문한 적이 있을 때 = 경로가 존재할 때
    if visited[end_index[0]][end_index[1]]:
        result = 1

    print('#{} {}'.format(t, result))
