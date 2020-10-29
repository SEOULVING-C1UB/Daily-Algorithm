for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())))
    cap = sorted(list(map(int, input().split())))
    answer = 0
    for i in range(M - 1, -1, -1):
        try:
            while cap[i] < weights[-1]:
                weights.pop()
            answer += weights.pop()
        except IndexError:
            break
    print('#{} {}'.format(tc, answer))