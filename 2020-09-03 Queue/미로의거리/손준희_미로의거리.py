movement = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 좌 우 상 하


def find_start_pos(N):      # 종착지 찾는 서브함수
    for y in range(N):
        if 3 in maze[y]:
            return [maze[y].index(3), y]
    return 0


def maze_runner(maze):      # 미로 탈출하는 서브함수
    que = [[0, find_start_pos(N)]]      # [거리 0, 종착점]
    check_list = []
    while len(que):
        step, [x, y] = que.pop(0)       # [지금까지 움직인 발자국, 현재 위치]
        for move in movement:
            nextX, nextY = x + move[0], y + move[1] # 다음 위치 nextX, nextY
            if -1 < nextX < N and -1 < nextY < N:   # 다음 위치가 미로 내부라면
                if maze[nextY][nextX] == 2:         # 만약 2라면 출발지에 도착한 것이므로
                    return step                     # 지금까지 움직인 발자국을 반환
                if not maze[nextY][nextX] and not [nextX, nextY] in check_list:
                    que.append([step+1, [nextX, nextY]])    # 벽이 아니고(길이고) 지났던 길이 아니면 queue에 추가
        if not [x, y] in check_list:
            check_list.append([x, y])   # 지나간 길이라고 체크
    return 0    # 위에꺼 다 했는데 중간에 반환하지 못했다? 길이 막힌 것이므로 0 반환


testcase = int(input())
for i in range(testcase):
    N = int(input())
    maze = [list(map(int, input()))[:N] for j in range(N)]
    print('#{} {}'.format(i + 1, maze_runner(maze)))