import sys

sys.stdin = open('미로_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, list(input()))))

    # Find start & end point
    for j in range(N):
        for i in range(N):
            if maze[j][i] == 3:
                end = [j, i]
            elif maze[j][i] == 2:
                start = [j, i]


    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[0 for j in range(N)] for i in range(N)]

    # From start point, search whether four directions are walls or not
    q = [start]
    ans = 0
    while q:
        y, x = q.pop()
        # end condition
        if [y, x] == end:
            ans = 1
            break

        # exclude the point visited before
        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] != 1 and not visited[ny][nx]:
                    q.append([ny, nx])

    print(f'#{tc} {ans}')
