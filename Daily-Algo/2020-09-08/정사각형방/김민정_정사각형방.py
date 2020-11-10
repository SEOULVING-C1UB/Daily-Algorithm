T = int(input())

dy = [0, 1, 0, -1] #오른쪽 아래 왼쪽 위
dx = [1, 0, -1, 0]


def isWall(y,x) :
    if y < 0 or x < 0 or y == N or x == N : return False
    return True

def bfs(s):
    Q = [s]
    visited = {}
    visited[s] = 1
    global lengthi, mini
    while Q :
        now = Q.pop(0)
        for i in range(4) :
            Y = now[0] + dy[i]
            X = now[1] + dx[i]
            if isWall(Y,X) and visited.get((Y,X), 0) == 0 and (arr[Y][X] - arr[now[0]][now[1]]  == 1 ) :
                visited[(Y,X)] = visited[now] + 1
                already[(Y,X)] = 1
                Q.append((Y,X))
    for v in visited.items() :
        if v[1] > lengthi :
            lengthi = v[1]
            mini = arr[s[0]][s[1]]
        elif v[1] == lengthi :
            if mini > arr[s[0]][s[1]] :
                mini = arr[s[0]][s[1]]
for tc in range(1, T+1) :
    N = int(input())
    lengthi = 0
    mini = 9999
    arr = []
    for i in range(N) :
        temp = list(map(int, input().split()))
        arr.append(temp)
    already = {}
    maxi = 0
    for i in range(N) :
        for j in range(N) :
            if already.get((i, j), 0) == 0 :
                bfs((i, j))
    print("#{} {} {}".format(tc, mini, lengthi))