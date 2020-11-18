from collections import deque


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def assign(assigned_stairs, idx):
    if idx == number_of_people:
        yield [int(x) for x in assigned_stairs]
    else:
        idx += 1
        yield from assign(assigned_stairs + '0', idx)
        yield from assign(assigned_stairs + '1', idx)


def timelapse(time):
    g1 = [[x[0], x[1], x[2] - time] for x in group1]
    g2 = [[x[0], x[1], x[2] - time] for x in group2]
    group1, group2 = g1, g2
    while going_down[0]:
        if going_down[0][0] < dis:
            going_down[0].popleft()
    while going_down[1]:
        if going_down[1][0] < dis:
            going_down[1].popleft()
    while waiting[0] and len(going_down[0]) < 3:
        going_down.append(waiting[0].popleft())
    while waiting[1] and len(going_down[1]) < 3:
        going_down.append(waiting[1].popleft())
    if len(going_down[assigned_stairs]) < 3:
        going_down[assigned_stairs].append(stairs[assigned_stairs][2])
    else:
        waiting[assigned_stairs].append(stairs[assigned_stairs][2])


def find_nearest_person():
    if not group1:
        return group2.popleft()
    elif not group2:
        return group1.popleft()
    else:
        if group1[0][2] < group2[0][2]:
            return group1.popleft()
        else:
            return group2.popleft()


for tc in range(int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stairs = []
    for r in range(N):
        for c in range(N):
            if not room[r][c]:
                continue
            elif room[r][c] == 1:
                people.append((r, c))
            else:
                stairs.append((r, c, room[r][c]))
    number_of_people = len(people)
    answer = 0xFFFFFFFF
    for assigned in assign('', 0):
        check = [0] * number_of_people
        group1, group2 = [], []
        for i in range(number_of_people):
            if assigned[i] == 0:
                group1.append([people[i][0], people[i][1], dist(people[i], stairs[assigned[i][:1]]), assigned[i]])
            else:
                group2.append([people[i][0], people[i][1], dist(people[i], stairs[assigned[i][:1]]), assigned[i]])

                group1 = deque(sorted(group1, key=lambda x: x[2]))
                group2 = deque(sorted(group2, key=lambda x: x[2]))

        waiting = [deque(), deque()]
        going_down = [deque(), deque()]
        cur_time = 0
        while group1 or group2:
            r, c, dis, assigned_stairs = find_nearest_person()
            cur_time += dis
            timelapse(dis)
            