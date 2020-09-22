
grid = [list(map(int,input().split()))for _ in range(4)]

def perm(N,k):  # depth k
    if k == 7:
        if p in result: return
        result.append(p)
    else:
        for i in range(0, N):
            A[k] = 1
            perm(N,k + 1)
            p[k] = pool[i]
            perm(N,k+1)

dr = [-1,0,1,0]
dc = [0,-1,0,1]
result = []
A = [0] * 7
for r in range(4):
    for c in range(4):
        pool = []
        p = [0] * 7
        print(r,c)
        pool.append(grid[r][c])
        for i in range(4):
            nr = r + dr[i]; nc = c + dc[i]
            if nr < 0 or nr ==4 or nc < 0 or nc == 4: continue
            if grid[nr][nc] in pool : continue
            pool.append(grid[nr][nc])
        print(pool)
        print()
        perm(len(pool),0)

print(result)





