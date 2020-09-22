def dfs(pos, s):
    # end condition
    if len(s) == 7:
        ans.add(s)
        return

    # move to four direction from current point, recursion
    for i in range(4):
        ny = pos[0] + dy[i]
        nx = pos[1] + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs([ny, nx], s + board[ny][nx])


T = int(input())
for tc in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    ans = set()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    # every point of board, recursion
    for j in range(4):
        for i in range(4):
            dfs([j, i], board[j][i])
    print(f'#{tc} {len(ans)}')
