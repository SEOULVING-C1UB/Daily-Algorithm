class micro:
    def __init__(self, nom, di, pos):
        self.nom = nom
        self.di = di
        self.pos = pos

    def hour_pass(self):
        self.pos[0] += dr[self.di]
        self.pos[1] += dc[self.di]
        if self.pos[0] in [0, N - 1] or self.pos[1] in [0, N - 1]:
            self.nom //= 2
            self.di += -1 if self.di % 2 else 1


def union(micros):
    t_nom = sum([m.nom for m in micros])
    t_di = max(micros, key=lambda x: x.nom).di
    t_pos = micros[0].pos
    return micro(t_nom, t_di, t_pos)


def check_unionable(micros):
    res = [i for i in range(len(micros))]
    for i in range(len(micros)):
        for j in range(i + 1, len(micros)):
            if micros[i].pos == micros[j].pos:
                res[j] = res[i]
    return res


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(int(input())):
    N, M, K = map(int, input().split())
    MICROS = []
    for _ in range(K):
        r, c, nom, di = map(int, input().split())
        MICROS.append(micro(nom, di - 1, [r, c]))
    cur_time = 0
    while cur_time < M:
        cur_time += 1
        for m in MICROS:
            m.hour_pass()
        check = check_unionable(MICROS)
        done = [True if check.count(check[i]) == 1 else False for i in range(len(check))]
        New_MICROS = [MICROS[i] for i in range(len(MICROS)) if done[i]]
        for i in range(len(check)):
            if done[i]:
                continue

            group = [i]
            for j in range(len(check)):
                if i != j and check[i] == check[j]:
                    group.append(j)
                    done[j] = True

            New_MICROS.append(union([MICROS[x] for x in group]))
        MICROS = New_MICROS
    print(f'#{tc + 1} {sum([x.nom for x in MICROS])}')
