import sys
sys.stdin = open('미로의거리_input.txt', 'r')

def start():            # 시작점(2)의 위치를 체크해주는 함수
    global x, y
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x,y = i,j
                return

# x,y 좌표가 index 내에서, maze[x][y]값이 0 또는 3일때 true를 반환해주는 함수
def go(x,y):
    if 0<=x<N and 0<=y<N and (maze[x][y] == 0 or maze[x][y] == 3):
        return True

# 2(시작점)에서 3(끝점)까지의 거리를 계산해주는 함수
def bfs(sx,sy):
    # 빈 큐를 정의해준다
    Q = []

    # 초기 2(시작점)의 좌표를 큐에 tuple형식(ex: (4,3))으로 push해준다
    Q.append((sx,sy))
    # visited 딕셔너리에 저장해준다 (ex: {(4,3):1})
    visited[(sx,sy)] = 1

    # 큐에 저장된 좌표를 모두 사용할 때 까지 실행해준다
    while Q:
        # 큐에 저장된 가장 첫번째 좌표를 pull해서 temp 변수에 저장한다 (ex: temp = (4,3))
        temp = Q.pop(0)
        # 위 좌표를 이용하여 상,하,좌,우를 확인해준다
        for i in range(4):
            # x,y 값을 temp에 저장된 좌표를 사용하여 초기화해준다
            x,y = temp[0],temp[1]
            # x,y에서 dx,dy만큼 이동한 X,Y 좌표를 정의해준다
            X = x + dx[i]
            Y = y + dy[i]
            if go(X,Y) and visited.get((X,Y),0) == 0:
                # if문을 들어왔으면 해당 (X,Y)좌표를 큐에 push한다(이는 while문이 돌아가는동안 (x,y)좌표로 활용될 것이다)
                Q.append((X,Y))
                # visited 딕셔너리에 해당좌표를 방문했다는 것을 표시하는 동시에, 몇칸을 갔는지까지 표시해준다.
                visited[(X,Y)] = visited[(x,y)] + 1
                # 만약 (X,Y) 좌표의 값이 3일 경우, visited 딕셔너리에 해당하는 value에서 2를 뺴준 값을 return 하면서 함수에서 빠져나온다.
                # 여기서 -2를 하는 이유는, 값을 더해 나갈때 시작지점(+1)과 도착지점(+1)에서 각각 1씩, 즉 2를 더했기 때문에,
                # 실질적으로 간 거리는 2를 빼준 값이다.
                if maze[X][Y] == 3:
                    return visited[(X,Y)]-2
    #만약 큐에 들어갈 수 있는 모든 좌표를 실행했는데도 3(도착지점)을 찾지 못했으면 메이즈가 연결되어 있지 않다는 표시로 0을 return 한다!
    return 0


for c in range(1,int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    x,y = 0, 0
    start()
    # 동서남북을 확인해주는 delta
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 방문한 좌표를 저장한 딕셔너리
    visited = {}
    print('#{} {}'.format(c,bfs(x,y)))
