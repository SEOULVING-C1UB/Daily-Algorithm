def asd(board, start, t):
    goal = [start]
    while goal: # len(goal) != 0인 동안
        i, j = goal.pop()

        visited[i][j] = 1 # i, j 값을 방문한 것으로

        x = [-1, 0, 1, 0]
        y = [0, -1, 0, 1]

        for q in range(4):
            ni = x[q] + i
            nj = y[q] + j
            if (ni >= 0 and t > ni) and (nj >= 0 and t > nj): # 위치 제한
                if board[ni][nj] != 1 and visited[ni][nj] == 0: # 벽이 아니고, 방문한 적 없을 때
                    goal.append([ni, nj]) # goal에 추가
                elif board[ni][nj] == 2: # 도착하면 길이 존재한다고 1을 리턴하기
                    return 1
    return 0

T = int(input())

for tc in range(1,1+T):
    t=int(input())
    board = []
    for _ in range(t):
        board.append(list(map(int, input())))

    visited = [[0] * t for _ in range(t)] # 방문 확인용

    for i in range(t):
        for j in range(t):
            if board[i][j] == 3:
                start = [i, j] # 3 에서 시작

    print('#{} {}'.format(tc, asd(board, start, t)))