def dfs(pos, dis):
    """
    Find route to destination and counting the distance.
    Compare 'ans' and 'dis' to find minimum distance from 's' to 'e'.
    :param pos: Current position
    :param dis: The past distance
    :return: None
    """
    global ans
    if pos == e:
        ans = dis - 1 if not ans or dis < ans else ans
        return

    # Backtracking
    if ans and dis > ans:
        return

    # Check the point visited
    visited[pos[0]][pos[1]] = 1
    for i in range(4):
        ny = pos[0] + dy[i]
        nx = pos[1] + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            #  If the new point is not wall and not visited
            if maze[ny][nx] != 1 and not visited[ny][nx]:
                dfs([ny, nx], dis + 1)
    visited[pos[0]][pos[1]] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if maze[j][i] == 2:
                # s : start point
                s = [j, i]
            elif maze[j][i] == 3:
                # e : end point
                e = [j, i]

    ans = 0
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited = [[0 for i in range(N)] for j in range(N)]
    dfs(s, 0)
    print(f'#{tc} {ans}')
