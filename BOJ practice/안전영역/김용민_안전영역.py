import copy
import sys
sys.setrecursionlimit(100000)
N = int(input())
zone = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_value = 1


def check(x, y):                        # 범위 체크
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


def find_zone(x, y):
    global size
    delta_x = [-1, 1, 0, 0]             # 상하좌우
    delta_y = [0, 0, -1, 1]
    visit[x][y] = 1                     # 방문 처리
    for d in range(4):
        # 범위 True이며 잠기지 않고 방문하지 않았을 때
        if check(x+delta_x[d], y+delta_y[d]) and copy_zone[x+delta_x[d]][y+delta_y[d]] > max_height and visit[x+delta_x[d]][y+delta_y[d]] == 0:
            size += 1                               # 한개의 안전영역의 크기 증가
            visit[x+delta_x[d]][y+delta_y[d]] = 1   # 방문처리
            find_zone(x+delta_x[d], y+delta_y[d])   # 재귀


# 최대 높이 구하기
max_height = 0
for i in range(N):
    for j in range(N):
        if zone[i][j] >= max_height:
            max_height = zone[i][j]

# 높이가 가장 높을 때부터 가장 낮을 때까지
while max_height:
    copy_zone = copy.deepcopy(zone)
    visit = [[0] * N for _ in range(N)]
    tmp = 0
    size = 1
    # 모든 인덱스 안전영역 탐색
    for x in range(N):
        for y in range(N):
            # 잠기지 않고 방문하지 않은 경우
            if copy_zone[x][y] > max_height and visit[x][y] == 0:
                find_zone(x, y)
                if size != 0:   # size가 0이 아니면 안전영역이라는 의미
                    tmp += 1    # 안전영역의 개수 증가
    max_height -= 1             # while 탈출하기 위해 1씩 감소
    if tmp >= max_value:        # 각 높이마다 최대 값 찾기
        max_value = tmp

print(max_value)
