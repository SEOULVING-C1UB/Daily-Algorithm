N = int(input())
b = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for c in range(N)] for r in range(N)]
for c in range(1, N):
    if b[0][c]:
        break
    dp[0][c][0] = 1

for r in range(1, N):
    for c in range(2, N):
        if not any([b[r][c], b[r - 1][c], b[r][c - 1]]):
            dp[r][c][1] = sum(dp[r - 1][c - 1])     # diagonal
        if not b[r][c]:
            dp[r][c][0] = sum(dp[r][c-1][:2])       # horizontal
            dp[r][c][2] = sum(dp[r-1][c][1:])       # vertical
print(sum(dp[-1][-1]))

# DFS is too slow for this problem.
# def move(r, c, stat):
#     # stat: direction the pipe is facing
#     if stat == 0:  # vertical
#         if c + 1 < N and not b[r][c + 1]:
#             yield r, c + 1, 0
#         if r + 1 < N and c + 1 < N:
#             if not any([b[r][c + 1], b[r + 1][c], b[r + 1][c + 1]]):
#                 yield r + 1, c + 1, 2
#     elif stat == 1:  # horizontal
#         if r + 1 < N and not b[r + 1][c]:
#             yield r + 1, c, 1
#         if r + 1 < N and c + 1 < N:
#             if not any([b[r][c + 1], b[r + 1][c], b[r + 1][c + 1]]):
#                 yield r + 1, c + 1, 2
#     else:  # diagonal
#         if c + 1 < N and not b[r][c + 1]:
#             yield r, c + 1, 0

#         if r + 1 < N and not b[r + 1][c]:
#             yield r + 1, c, 1
#         if r + 1 < N and c + 1 < N:
#             if not any([b[r][c + 1], b[r + 1][c], b[r + 1][c + 1]]):
#                 yield r + 1, c + 1, 2
#
#
# def dfs(r, c, stat):
#     global ans
#     for nr, nc, nstat in move(r, c, stat):
#         if [nr, nc] == [N - 1, N - 1]:
#             ans += 1
#         else:
#             dfs(nr, nc, nstat)
#
#
# N = int(input())
# b = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# dp = [[0 for c in range(N)] for r in range(N)]
# dfs(0, 1, 0)
# print(ans)
