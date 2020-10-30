# back tracking using dp.

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 250
    # dp : sum of consumed battery to get this location
    dp = [[-1 for i in range(N)] for j in range(N)]

    # q : [y, x, consumed battery]
    q = [(0, 0, board[0][0])]
    while q:
        y, x, cb = q.pop()
        # back tracking
        if dp[y][x] == -1 or dp[y][x] > cb:
            dp[y][x] = cb
        else:
            continue

        # end condition
        if y == N - 1 and x == N - 1:
            ans = min(ans, cb)
            continue

        if x != N - 1:
            q.append((y, x + 1, cb + board[y][x + 1]))
        if y != N - 1:
            q.append((y + 1, x, cb + board[y + 1][x]))
    print('#{} {}'.format(tc, ans))
