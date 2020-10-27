def dfs(day, pf):
    global maxi_pf
    if day > N:
        return
    elif day == N:
        maxi_pf = max(maxi_pf, pf)
        return

    dfs(day + csts[day][0], pf + csts[day][1] )
    dfs(day + 1, pf)


N = int(input())
csts = [list(map(int, input().split())) for _ in range(N)]
maxi_pf = 0
dfs(0, 0)
print(maxi_pf)

# -----------------------------------------------------
# better way by using dp.
N = int(input())

dp = [0] * (n+5)
for i in range(n):
    t, p = map(int, input().split())
    if t > 1:
        dp[i+1] = max(dp[i], dp[i+1])
    dp[i+t] = max(dp[i+t], dp[i]+p)

print(max(dp[:N+1]))