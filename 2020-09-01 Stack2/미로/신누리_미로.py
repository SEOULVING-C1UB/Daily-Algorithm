import sys
sys.stdin = open("(4875)미로_input.txt")


def maze(startx, starty):
    # dfs와 유사. 일단 시작점을 stack에 넣는다.
    s = []
    s.append((startx, starty))
    # stack이 비어있지 않은 동안
    while s :
        # 있는 원소를 빼서
        a, b = s.pop()
        # 방문 체크를 하고
        if visited[a][b] == 0:
            visited[a][b] = 1
            # 만약 도착점이라면 끝낸다.
            if a == endx and b == endy:
                break;
            # 현재 위치에서 4방향으로 움직여본다
            for k in range(4):
                p = dir1[k]
                q = dir2[k]
                # arr의 범위 내에 있고
                if 0<= a+p < N and 0 <= b+q < N:
                    # 통로인데 방문한 적이 없다면
                    if arr[a+p][b+q] == "0" and visited[a+p][b+q] == 0:
                        # 스택에 추가한다.
                        s.append((a+p, b+q))


T = int(input())
for t in range(T):
    N = int(input())
    # arr에 주어진 배열을 가져오고
    arr = []
    for i in range(N):
        arr.append(list(input()))
    # arr을 순회하며 시작점과 도착점을 찾는다
    # 방문 확인을 편하게 하기 위해, 시작점과 도착점을 0으로 변경
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "2":
                startx = i
                starty = j
                arr[i][j] = "0"
            elif arr[i][j] == "3":
                endx = i
                endy = j
                arr[i][j] = "0"
    # 방문 여부를 체크할 2차원 배열을 만들어주고
    visited = [[0]*N for _ in range(N)]
    # 4방향으로 움직이도록 dir을 만들어둔다.
    dir1 = [1, 0, -1, 0]
    dir2 = [0, 1, 0, -1]
    # maze를 시작점에서 실행해, 시작점에서 갈 수 있는 경로를 탐색
    maze(startx, starty)
    # 시작점에서 maze를 실행한 결과 도착점에 방문했는지를 확인
    result = visited[endx][endy]
    print('#{} {}' .format(t+1, result))
