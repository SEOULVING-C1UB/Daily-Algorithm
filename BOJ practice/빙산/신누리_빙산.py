'''
[컨셉]
1) 두 덩이 이상으로 조각나거나, 다 녹을 때까지 [녹이고-확인하는] 과정을 거침
2) 녹이는 함수는 melt()
   - 4방향으로 돌면서 0인 공간을 세서 temp에 담아뒀다가, 나중에 줄이면서 빙하의 개수를 세서 반환한다.
   - 나중에 줄이는 이유는, 더 앞에 있는 칸 때문에 영향받는 것을 방지하기 위해
3) 2번에서 센 빙하의 개수가 0개라면 break 
4) 그렇지 않다면, 확인은 dfs()
   - 빙하가 있는 칸에서 시작해서 dfs를 하면서 개수를 세서, melt에서 센 빙하 개수랑 일치하는지 확인한다.
   - 만약에 일치하지 않으면, 빙하가 두 덩이 이상 있는 것이니 break
'''

def melt():
    temp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                for k in range(4):
                    if 0 <= i+dir1[k] < N and 0 <= j+dir2[k] < M:
                        if not arr[i+dir1[k]][j+dir2[k]]:
                            temp[i][j] += 1
    result = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j]:
                arr[i][j] -= temp[i][j]
                if arr[i][j] < 0 :
                    arr[i][j] = 0
            if arr[i][j]:
                result +=1
    return result


def dfs():
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                x, y = i, j
    visited = [[0]*M for _ in range(N)] 
    stack = [(x,y)]
    result = 0
    while stack:
        a, b = stack.pop()
        if arr[a][b] and not visited[a][b]:
            visited[a][b] = 1
            result += 1
            for k in range(4):
                p, q = a+dir1[k], b+dir2[k]
                if 0 <= p < N and 0 <= q < M:
                    if arr[p][q] and not visited[p][q]:
                        stack.append((p,q))
    return result


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir1 = [1, 0, -1, 0]
dir2 = [0, 1, 0, -1]

time = 0
while True:
    # 우선 녹인다
    cnt = melt()
    time += 1
    # 다 녹지 않았으면, 빙하 한 덩어리에 몇 칸인지 센다
    if cnt:
        one = dfs()
        if one != cnt :
            break
    # 다 녹지 않았으면 탈출하면서 0으로 바꾸기. 
    else:
        time = 0
        break
print(time)