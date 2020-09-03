from collections import deque

T = int(input())

for tc in range(1, T+1):

    N = int(input())  # 미로 크기

    # 미로와 같은 크기의 distance라는 배열을 만든다
    # 거기에 이동한 거리를 담을거임
    maze = [list(map(int, input())) for _ in range(N)]
    distance = [[0]*N for _ in range(N)]

    # 시작 X랑 Y값
    startX = startY= 0
    endX = endY = 0
    Q = deque()
    for i in range(N):
        if 2 in maze[i]:
            startX = maze[i].index(2)  # 시작점 찾아주기
            startY = i
        if 3 in maze[i]:
            endX = maze[i].index(3)     #끝위치 찾아주기
            endY = i

    # 먼저 시작위치를 넣어주고 방문처리한다
    Q.append((startY, startX))
    maze[startY][startX] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while Q:

        # Q의 첫번째를 꺼내서 현위치로 만든다
        current = Q.popleft()

        # 방향 탐색~
        for i in range(4):
            x = current[1] + dx[i]
            y = current[0] + dy[i]

            # 갈 수 있는 길이라면 그 위치를 방문처리하고
            # 거리 배열의 그 위치에 방금 있던 위치 값 + 1을 해준다 (그게 그 전 지점부터 이동한 거리니까)
            if 0<= x < N and 0 <= y < N and maze[y][x] == 0:
                maze[y][x] = 1
                distance[y][x] = distance[current[0]][current[1]] + 1
                Q.append((y, x))

            # 만약 현위치가 출구라면 거리는 그 이전 값이다
            elif 0<= x < N and 0 <= y < N and maze[y][x] == 3:
                distance[y][x] = distance[current[0]][current[1]]
                break


    if distance[endY][endX] == 0:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, distance[endY][endX]))





