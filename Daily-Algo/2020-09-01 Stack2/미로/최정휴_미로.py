# 미로를 탐색할 재귀함수
# x, y는 기준 좌표, idx는 왔던 방향으로 돌아가지 않기 위한 변수
def maze(lst, x, y, idx):
    # 우, 하, 좌, 상 델타 검색. 
    dx = [1, 0, -1 ,0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        # 4방향에 대하여 좌우, 상하가 페어로 등장하면 idx와 i의 값이 2차이나므로 그러지 않게 하고
        # 인덱스 범위를 넘어가지않는 범위에서 탐색
        if abs(idx - i) != 2 and 0<= x+dx[i] <= n-1 and 0<= y+dy[i] <= n-1:
            # 길이 열려있으면 재귀 호출
            if lst[y+dy[i]][x+dx[i]] == 0:
                maze(lst, x+dx[i], y+dy[i], i)
            # 3을 만나면 ans에 넣음
            elif lst[y+dy[i]][x+dx[i]] == 3:
                ans.append(1)

t = int(input())

for i in range(1,t+1):
    n = int(input())
    maze_lst =[]
    # ans에 0을 미리 넣어 3을 못만나면 0을 출력, 3을 만나면 1을 출력하게끔 처리
    ans = [0]
    for j in range(n):
        maze_lst.append(list(map(int,input())))
        # maze_lst에 각 행 넣어가며 2있는지 확인하여 시작점으로
        # index에서 에러날 수 있으므로 try사용
        try:
            x = maze_lst[-1].index(2)
            y = j
        except:
            pass
    maze(maze_lst, x, y, 10)
    print(f'#{i} {ans[-1]}')