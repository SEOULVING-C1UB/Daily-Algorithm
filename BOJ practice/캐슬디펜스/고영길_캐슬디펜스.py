from itertools import combinations as coms
from copy import deepcopy


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_nearest_enemy(pos):
    shortest = D
    sh_idx = None
    for i, enemy in enumerate(enemies):
        if not alive[i]:
            continue

        d = dist(pos, enemy)
        if d < shortest:
            shortest = d
            sh_idx = i
        elif d == shortest:
            if sh_idx is None or enemy[1] < enemies[sh_idx][1]:
                shortest = d
                sh_idx = i
    return sh_idx


def shoot(archers):
    global kill
    shooted = set()
    for archer in archers:
        shooted.add(find_nearest_enemy(archer))
    for s in list(shooted):
        if s is not None:
            alive[s] = False
            kill += 1


def move(enemies):
    for i in range(len(enemies)):
        if alive[i]:
            if enemies[i][0] < N - 1:
                enemies[i][0] += 1
            else:
                alive[i] = False


N, M, D = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

s_enemies = []
for r in range(N):
    for c in range(M):
        if field[r][c]:
            s_enemies.append([r, c])

answer = 0

for archers in coms(zip([N] * M, range(M)), 3):
    kill = 0
    enemies = deepcopy(s_enemies)
    alive = [True] * len(enemies)
    while any(alive):
        shoot(archers)
        move(enemies)
    if kill > answer:
        answer = kill
print(answer)
