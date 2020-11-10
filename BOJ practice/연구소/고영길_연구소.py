from itertools import combinations as coms
from copy import deepcopy
from collections import deque

dys = [1, 0, -1, 0]
dxs = [0, 1, 0, -1]


def infected():
    global answer
    cnt = len_viruses
    for virus in viruses:
        q = deque([virus])
        while q:
            if cnt > answer:
                return 0
            y, x = q.popleft()
            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not room[ny][nx]:
                    cnt += 1
                    room[ny][nx] = 2
                    q.append((ny, nx))
    return cnt


N, M = map(int, input().split())
room_origin = [[int(x) for x in input().split()] for _ in range(N)]
viruses, walls, empties = [], [], []
len_viruses = 0
len_walls = 3
for r in range(N):
    for c in range(M):
        if room_origin[r][c] == 1:
            walls.append((r, c))
            len_walls += 1
        elif room_origin[r][c] == 2:
            viruses.append((r, c))
            len_viruses += 1
        else:
            empties.append((r,c))

answer = N * M - len_walls
for com in coms(empties, 3):
    room = deepcopy(room_origin)
    for r, c in com:
        room[r][c] = 1

    cnt_infected = infected()
    if cnt_infected and answer > cnt_infected:
        answer = cnt_infected
print(N*M-len_walls-answer)