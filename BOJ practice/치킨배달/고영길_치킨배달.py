from itertools import combinations as coms


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_nearest_store(house, stores):
    short_dist = (2 * N) ** 2
    for store in stores:
        if dist(house, store) < short_dist:
            short_dist = dist(house, store)
    return short_dist


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
houses = []
stores = []
for j in range(N):
    for i in range(N):
        if board[j][i] == 1:
            houses.append((j, i))
        elif board[j][i] == 2:
            stores.append((j, i))

ans = (2 * N) ** 2
for com in coms(stores, M):
    temp_sum = 0
    for house in houses:
        temp_sum += find_nearest_store(house, com)
    ans = min(ans, temp_sum)

print(ans)
