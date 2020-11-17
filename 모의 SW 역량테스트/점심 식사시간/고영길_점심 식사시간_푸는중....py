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
                group1.append([people[i][0], people[i][1], dist(people[i], stairs[assigned[i][:1]])])
            else:
                group2.append([people[i][0], people[i][1], dist(people[i], stairs[assigned[i][:1]])])

        group1 = deque(sorted(group1, key=lambda x: x[2]))
        group2 = deque(sorted(group2, key=lambda x: x[2]))

        waiting = [deque(), deque()]
        cur_time = 0
        while group1 or group2:
