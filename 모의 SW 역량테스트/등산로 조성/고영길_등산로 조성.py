dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(len_trail, pos, sharped, prev_h):
    global answer
    movable = False
    for d in range(4):
        nr = pos[0] + dr[d]
        nc = pos[1] + dc[d]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if board[nr][nc] < prev_h:
                visited[nr][nc] = 1
                dfs(len_trail + 1, (nr, nc), sharped, board[nr][nc])
                visited[nr][nc] = 0
                movable = True
            else:
                if not sharped:
                    if board[nr][nc] - K < prev_h:
                        visited[nr][nc] = 1
                        dfs(len_trail + 1, (nr, nc), True, prev_h - 1)
                        visited[nr][nc] = 0
    if not movable:
        if answer < len_trail:
            answer = len_trail


for tc in range(int(input())):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    highest_height = max([max(row) for row in board])
    highest_poses = [(r, c) for r in range(N) for c in range(N) if board[r][c] == highest_height]
    answer = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for highest_pos in highest_poses:
        dfs(1, highest_pos, False, highest_height)
    print(f'#{tc + 1} {answer}')
