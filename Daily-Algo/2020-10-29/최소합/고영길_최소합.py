for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 250
    q = [(0, 0, board[0][0])]
    while q:
        y, x, n = q.pop()
        if y == N - 1 and x == N - 1:
            ans = min(ans, n)
            continue

        if x != N - 1:
            q.append((y, x + 1, n + board[y][x + 1]))
        if y != N - 1:
            q.append((y + 1, x, n + board[y + 1][x]))
    print('#{} {}'.format(tc, ans))