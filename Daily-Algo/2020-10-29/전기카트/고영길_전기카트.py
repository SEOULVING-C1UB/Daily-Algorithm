from itertools import permutations as pers

for tc in range(1, int(input()) + 1):
    N = int(input())
    bat = [list(map(int, input().split())) for _ in range(N)]
    answer = 1000
    for per in pers(range(1, N), N - 1):
        temp = bat[0][per[0]] + bat[per[-1]][0]
        for i in range(N - 2):
            temp += bat[per[i]][per[i + 1]]
        answer = min(answer, temp)
    print('#{} {}'.format(tc, answer))
