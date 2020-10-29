for tc in range(1, int(input()) + 1):
    N = int(input())
    cargos = [list(map(int, input().split())) for _ in range(N)]
    cargos.sort(key=lambda x: x[1] - x[0])
    cap_time = [False] * 24
    answer = 0
    for s, e in cargos:
        if any(cap_time[s:e]):
            continue
        for i in range(s, e):
            cap_time[i] = True
        answer += 1
    print('#{} {}'.format(tc, answer))
