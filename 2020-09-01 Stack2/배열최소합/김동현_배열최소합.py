def bfs(v,cursum):
    global min_sum
    if cursum > min_sum:
        return
    if v == n:
        if cursum < min_sum:
            min_sum = cursum
        return

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            bfs(v+1,cursum+board[v][i])
            visit[i] = 0

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    min_sum = 9 * n

    bfs(0,0)
    print('#{} {}'.format(tc,min_sum))

