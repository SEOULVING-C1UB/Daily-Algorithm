import sys

sys.stdin = open("1953_탈주범검거_input.txt", "r")

from collections import deque

# bfs 방식으로 한칸씩 이동하며 결과를 result에 저장
def move():
    result = 0
    x, y = r, c
    
    # q에 맨홀의 위치를 넣고 출발
    q = deque()
    q.append((x, y))
    visit[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        # 현재 위치 t
        t = q.popleft()
        x, y = t[0], t[1]

        # 시간 a에 방문하게 되는 노드들은 visit에 a가 기록됨: visit에서 꺼낸 노드가 l+1이라면 시간 제한이 끝난 것
        if visit[x][y] == l+1:
            break 

        # 새로운 노드를 방문했으니 result에 1 추가
        result += 1

        # 이동: 상하좌우를 탐색하며 이동가능할 경우 큐에 넣음
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 먼저 지도에서 벗어나는지 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 다음으로 터널이 있는지, 방문했는지 체크
                if tunnel[nx][ny] and not visit[nx][ny]:
                    # 현재 지하터널에서 이동할 수 있는지 체크
                    if movable(i, tunnel[x][y], tunnel[nx][ny]):
                        q.append((nx, ny))
                        visit[nx][ny] = visit[x][y] + 1
    return result


# 주어진 방향에 대해 현재 터널에서 다음터널 갈 수 있는지 판정
def movable(direction, curtype, desttype):
    result = False

    if direction == 0:      # 위
        if curtype == 1:
            if desttype in [1, 2, 5, 6]:
                result = True
        elif curtype == 2:
            if desttype in [1, 2, 5, 6]:
                result = True
        elif curtype == 3:
            pass
        elif curtype == 4:
            if desttype in [1, 2, 5, 6]:
                result = True
        elif curtype == 5:
            pass
        elif curtype == 6:
            pass
        else:
            if desttype in [1, 2, 5, 6]:
                result = True
    elif direction == 1:    # 오른쪽
        if curtype == 1:
            if desttype in [1, 3, 6, 7]:
                result = True
        elif curtype == 2:
            pass
        elif curtype == 3:
            if desttype in [1, 3, 6, 7]:
                result = True
        elif curtype == 4:
            if desttype in [1, 3, 6, 7]:
                result = True
        elif curtype == 5:
            if desttype in [1, 3, 6, 7]:
                result = True
        elif curtype == 6:
            pass
        else:
            pass
    elif direction == 2:    # 아래
        if curtype == 1:
            if desttype in [1, 2, 4, 7]:
                result = True
        elif curtype == 2:
            if desttype in [1, 2, 4, 7]:
                result = True
        elif curtype == 3:
            pass
        elif curtype == 4:
            pass
        elif curtype == 5:
            if desttype in [1, 2, 4, 7]:
                result = True
        elif curtype == 6:
            if desttype in [1, 2, 4, 7]:
                result = True
        else:
            pass
    else:                   # 왼쪽
        if curtype == 1:
            if desttype in [1, 3, 4, 5]:
                result = True
        elif curtype == 2:
            pass
        elif curtype == 3:
            if desttype in [1, 3, 4, 5]:
                result = True
        elif curtype == 4:
            pass
        elif curtype == 5:
            pass
        elif curtype == 6:
            if desttype in [1, 3, 4, 5]:
                result = True
        else:
            if desttype in [1, 3, 4, 5]:
                result = True

    return result
    
t = int(input())    
for test_case in range(t):    
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    # 방문여부와 현재 시각을 기록하는 visit
    visit = [[0]*m for _ in range(n)]
    print('#' + str(test_case + 1), move())