from itertools import permutations as pers

for tc in range(1, int(input()) + 1):
    N = int(input())
    bat = [list(map(int, input().split())) for _ in range(N)]
    answer = 1000
    # By using permutation, make the route like 1231, 1321.
    # Because always start from 1, end from 1, exclude 1 from permutation.
    for per in pers(range(1, N), N - 1):
        temp = bat[0][per[0]] + bat[per[-1]][0]  # 1-> second, second last -> 1
        for i in range(N - 2):
            temp += bat[per[i]][per[i + 1]]
            if temp >= answer:  # back tracking
                break
        answer = min(answer, temp)
    print('#{} {}'.format(tc, answer))
