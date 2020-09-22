def dfs(cnt, n):
    """
    Row order recursive function, add minimum number in row,
    non-duplicated vertically.
    :param cnt: indicate number of rows
    :param n: indicate sum of chosen numbers
    :return: None
    """
    global ans
    if cnt == N:
        ans = min(ans, n)
        return

    # Backtracking
    if n > ans:
        return

    for i in range(N):
        if not check[i]:
            check[i] = True
            dfs(cnt + 1, n + board[cnt][i])
            check[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # check : (list) check weather vertical lines overlap
    check = [False] * N
    ans = 101
    dfs(0,0)
    print(f'#{tc} {ans}')