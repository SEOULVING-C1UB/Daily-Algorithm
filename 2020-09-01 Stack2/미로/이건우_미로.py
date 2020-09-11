import sys
sys.stdin = open('4875_input.txt', 'r')


#벽을 만나지 않거나 인덱스를 벗어나지 않으면 진행
def go(x,y):
    if 0<=x<N and 0<=y<N and (arr[x][y] == 0 or arr[x][y] == 3): return True
#시작점에서 부터 검색 시작
#만약에 시작점을 4번 이상 통과하면 (visit = 4) return 0
# 우, 하, 좌, 상 (시계방향)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def search(x,y):
    global flag
    if arr[x][y] == 3:          # 만약 3을 발견하면 flag에 1을 저장 후 함수를 끝낸다
        flag = 1
        return

    visit.append((x,y))         # 방문 처리를 해준다
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if (X,Y) not in visit and go(X,Y):          # 방문하지 않았고 go함수를 만족하면 delta만큼 증가함 X,Y를 이요하여 재귀호출
            search(X,Y)



for c in range(int(input())):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    # 2(시작점)의 좌표를 찾아준다
    for i in range(N-1,-1,-1):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
                break
        if arr[i][j] == 2:
            break
    visit = []
    flag = 0
    search(x,y)
    print('#{} {}'.format(c+1, flag))