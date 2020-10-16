from copy import deepcopy
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def check(y, x, d, room):
    new_room = deepcopy(room)
    ny = y + dy[d]
    nx = x + dx[d]
    while 0 <= ny < N and 0 <= nx < M:
        if new_room[ny][nx] == 6:
            break
        elif new_room[ny][nx]:
            pass
        else:
            new_room[ny][nx] = '#'
        ny += dy[d]
        nx += dx[d]
    return new_room


def count_zero(room):
    return sum([r.count(0) for r in room])


def sol(idx, room):
    global answer
    if idx == cnt_cctv:
        answer = min(answer, count_zero(room))
        return

    y, x = cctvs[idx]

    if room[y][x] == 5:
        new_room = check(y, x, 0, room)
        new_room = check(y, x, 1, new_room)
        new_room = check(y, x, 2, new_room)
        new_room = check(y, x, 3, new_room)
        sol(idx + 1, new_room)
    else:
        for d in range(4):
            if room[y][x] == 1:
                new_room = check(y, x, d, room)
            elif room[y][x] == 2:
                new_room = check(y, x, d, room)
                new_room = check(y, x, d - 2, new_room)
            elif room[y][x] == 3:
                new_room = check(y, x, d, room)
                new_room = check(y, x, d - 1, new_room)
            elif room[y][x] == 4:
                new_room = check(y, x, d, room)
                new_room = check(y, x, d - 1, new_room)
                new_room = check(y, x, d - 2, new_room)
            sol(idx + 1, new_room)



N, M = map(int, input().split())
rooms = [list(map(int, input().split())) for j in range(N)]
cctvs = [(j, i) for j in range(N) for i in range(M) if 1 <= rooms[j][i] <= 5]
cnt_cctv = len(cctvs)
answer = N * M

sol(0, rooms)
print(answer)
