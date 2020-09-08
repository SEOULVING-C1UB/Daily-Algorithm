if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        rooms = []
        for _ in range(N):
            rooms.append(list(map(int, input().split())))

        dp = [[0 for i in range(N)] for j in range(N)]
        dy = [1, -1, 0, 0]
        dx = [0, 0, -1, 1]
        for j in range(N):
            for i in range(N):
                if dp[j][i]:  # visited
                    continue
                dp[j][i] = 1

                # Calculate the number of movable points from all points.
                # If meet calculated point in the course, add two values.
                q = [[j, i]]
                while q:
                    y, x = q.pop()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N:
                            if rooms[ny][nx] - rooms[y][x] == 1:
                                if dp[ny][nx]: # meet calculated point
                                    dp[j][i] += dp[ny][nx]
                                else:          # else : add 1, check visited
                                    dp[ny][nx] = -1
                                    dp[j][i] += 1
                                    q.append([ny, nx])
                                break

        # find largest value in dp
        max_y, max_x = 0, 0
        for j in range(0, N):
            for i in range(0, N):
                if dp[j][i] > dp[max_y][max_x]:
                    max_x, max_y = i,j
                elif dp[j][i] == dp[max_y][max_x]: # if has same value
                    if rooms[j][i] < rooms[max_y][max_x]:
                        max_x,max_y = i,j
        print(f'#{tc} {rooms[max_y][max_x]} {dp[max_y][max_x]}')
