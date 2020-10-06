def find_holes():
    """
    Find every hole. Check this block if empty or not,
    then if block is empty
    1. If blocks touch the edge -> not hole
    2. else -> hole
    """
    global cnt, hole_exist
    hole_exist = False
    visited = [[0 for i in range(M)] for j in range(N)]
    holes = [[0 for i in range(M)] for j in range(N)]
    for j in range(N):
        for i in range(M):
            if board[j][i] or visited[j][i]:
                continue
            is_hole = True
            emptys = [(j, i)]
            q = [(j, i)]
            visited[j][i] = 1
            while q:
                y, x = q.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= nx < M and 0 <= ny < N:
                        if not board[ny][nx] and not visited[ny][nx]:
                            emptys.append((ny, nx))
                            q.append((ny, nx))
                            visited[ny][nx] = 1
                            if nx in [0, M - 1] or ny in [0, N - 1]:
                                is_hole = False
            if is_hole:
                hole_exist = True
                for y, x in emptys:
                    holes[y][x] = 1
    return holes


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# h : time taken, cnt : leftover board
h, cnt = 0, 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
cheese = [(j, i) for j in range(N) for i in range(M) if board[j][i]]
cnt = len(cheese)
hole_exist = True

while True:
    h += 1
    # first trial or hole existed prev time
    if hole_exist:
        holes = find_holes()
    melted = 0
    after_hour = []
    for y, x in cheese:
        touch_air = False
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= nx < M and 0 <= ny < N:
                if not board[ny][nx] and not holes[ny][nx]:
                    touch_air = True
                    melted += 1
                    break
        if not touch_air:
            after_hour.append((y, x))

    # cheese is totally melted.
    if not after_hour:
        print(h, cnt, sep='\n')
        break
    else:
        # melt
        for y, x in cheese:
            if (y, x) not in after_hour:
                board[y][x] = 0
        cnt -= melted
        cheese = after_hour



# ------------------------------------------
# this is better way
from collections import deque
n,m=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(n)]
di,dj=[0,1,0,-1],[1,0,-1,0]
t,x=0,0
while 1:
  v=[[0]*m for _ in range(n)]
  b=[]
  q=deque([(0,0)])
  v[0][0]=1
  while q:
    p=q.popleft()
    for k in range(4):
      i,j=p[0]+di[k],p[1]+dj[k]
      if 0<=i<n and 0<=j<m and v[i][j]==0:
        v[i][j]=1
        if a[i][j]: b.append((i,j))
        else: q.append((i,j))
  if b:
    t+=1
    for p in b: a[p[0]][p[1]]=0
    x=len(b)
  else:
    print(t); print(x)
    break