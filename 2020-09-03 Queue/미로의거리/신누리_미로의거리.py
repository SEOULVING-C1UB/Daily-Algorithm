import sys
sys.stdin = open("(5105)미로의 거리_input.txt")


# bfs 로직 사용
def maze(startx, starty):
    # Queue를 만들어 시작점을 넣어주기
    Q = []
    Q.append((startx, starty))
    # 방문 처리
    visited[startx][starty] = 1
    # 큐가 비어있지 않다면
    while Q:
        # 노드를 꺼내서
        a, b = Q.pop(0)
        # 도착점인지 확인하고
        if a == endx and b == endy:
            break
        # 4방향에 대해 움직인다
        for k in range(4):
            p = dir1[k]
            q = dir2[k]
            # 배열의 범위 내에 있고
            if 0 <= a+p < N and 0 <= b+q < N:
                # 통로이며, 방문하지 않은 노드일 경우
                if arr[a+p][b+q] == '0' and visited[a+p][b+q] == 0:
                        # 큐에 넣고
                        Q.append((a+p, b+q))
                        # visited에 (직전노드의 visited값 +1)을 넣어줌.
                        visited[a+p][b+q] = visited[a][b] + 1


T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(input()))
    # 출발점, 도착점을 찾고 갈 수 있는지 확인하기 쉽게 0으로 바꿈.
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
    # 출발점에서부터의 거리 담을 배열
    visited = [[0]*N for _ in range(N)]
    # 4방향 움직이기 위한 배열
    dir1 = [1, 0, -1, 0]
    dir2 = [0, 1, 0, -1]
    maze(startx, starty)
    # visited[도착점]의 값을 result에 담음
    result = visited[endx][endy]
    # 만약 방문 했다면
    if result > 0:
        # 출발점, 도착점 제외
        result -= 2
    print('#{} {}' .format(t+1, result))
