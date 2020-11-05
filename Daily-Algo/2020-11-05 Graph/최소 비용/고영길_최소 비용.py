import heapq
import sys

sys.stdin = open('최소 비용_input.txt', 'r')
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for tc in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    wt = [[INF for c in range(N)] for r in range(N)]
    visited = [[0 for c in range(N)] for r in range(N)]
    wt[0][0] = 0
    q = [(wt[0][0], (0, 0))]
    while q:
        cur, (r, c) = heapq.heappop(q)
        visited[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nc < N and 0 <= nr < N and not visited[nr][nc]:
                if field[nr][nc] > field[r][c]:
                    if field[nr][nc] - field[r][c] + cur + 1 < wt[nr][nc]:
                        wt[nr][nc] = field[nr][nc] - field[r][c] + cur + 1
                        heapq.heappush(q, (wt[nr][nc], (nr, nc)))
                else:
                    if cur + 1 < wt[nr][nc]:
                        wt[nr][nc] = cur + 1
                        heapq.heappush(q, (wt[nr][nc], (nr, nc)))
    print('#{} {}'.format(tc + 1, wt[-1][-1]))
