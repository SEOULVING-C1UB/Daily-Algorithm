class micro:
    def __init__(self, nom, di, pos):
        self.nom = nom
        self.di = di
        self.pos = pos

    def hour_pass(self):
        self.r += dr[self.di]
        self.c += dc[self.di]
        if N in [self.r, self.c]:
            self.nom //= 2
            self.di += -1 if self.di % 2 else 1


def union(micros):
    nom = sum([m.nom for m in micros])
    di = max(micros, key=lambda x: x.nom).di
    return micro(nom, di, micros[0].pos)


def check_unionable(micros):
    res = [i for i in range(len(micros))]
    for i in range(len(micros)):
        for j in range(i + 1, len(micros)):
            if micros[i].pos == micros[j].pos:
                res[j] = res[i]
    return res


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(int(input())):
    N, M, K = map(int, input().split())
    MICROS = [micro(nom, di - 1, [r, c]) for _ in range(K) for r, c, nom, di in map(int, input().split())]
    cur_time = 0
    while cur_time < M:
        cur_time += 1
        MICROS = list(map(micro.hour_pass, MICROS))
        check = check_unionable(MICROS)
        group = []
        for i in range(len(check)):

        New_MICROS = [MICROS[i] for i in range(len(MICROS)) if check.count(check[i]) == 1]
