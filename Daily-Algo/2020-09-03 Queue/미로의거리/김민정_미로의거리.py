import sys
sys.stdin = open('미로의거리_input.txt', 'r')

tc = int(input())

def findstart(arr) :
    for y in range(num) :
        for x in range(num) :
            if arr[y][x] == 2 :
                return y, x

def boundary(y,x) :
    if 0 <= y < num and 0 <= x < num and ( arr[y][x] == 0 or arr[y][x] == 3 ) :
        return True

def maze(y, x) :
    dy = [0, 1, 0, -1]  # 오른쪽 아래 왼쪽 위
    dx = [1, 0, -1, 0]
    queue = []
    visited = {}

    queue.append((y,x))
    visited[(y,x)] = 1

    while queue :
        now = queue.pop(0)
        ny, nx = now[0], now[1]

        for i in range(4) :     # 상하좌우 4번 돌린다.

            Y = ny + dy[i]      # 지금 값에다가 상하좌우 넣어서 새로운 x,y 형성
            X = nx + dx[i]

            if boundary(Y,X) == True and visited.get((Y,X), 0) == 0 :   # 방문 및 값 확인
                queue.append((Y,X))                 # 진행해야하므로 큐에 또 넣어준다.
                visited[(Y,X)] = visited[(ny, nx)] + 1

                if arr[Y][X] == 3 :         # 도착했으면 리턴. 추가적으로 포함된 값 때문에 2 빼준다.
                    return visited[(Y,X)] - 2
    return 0        # 도착 못하면 0

for t in range(tc) :

    num = int(input())
    arr = [list(map(int, input())) for _ in range(num)]

    y, x = findstart(arr)
    result = maze(y,x)

    print("#{} {}".format(t+1,result))