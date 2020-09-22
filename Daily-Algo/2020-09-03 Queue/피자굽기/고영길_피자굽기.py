from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = deque(zip(map(int, input().split()), range(1, M + 1)))
    oven = [[0]] * N

    # idx : (int) index of oven indicate entrance
    idx = 0
    # cnt : (int) numbers of finished pizza
    cnt = 0
    while cnt < M - 1:
        # oven[idx] is not empty
        if oven[idx][0]:
            oven[idx][0] //= 2
            # finished
            if oven[idx][0] == 0:
                cnt += 1

        # If oven[idx] is empty.
        if oven[idx][0] == 0 and pizza:
            oven[idx] = list(pizza.popleft())
        idx = (idx + 1) % N

    # Find last pizza left in oven
    for i in range(N):
        if oven[i][0]:
            ans = oven[i][1]
            break

    print(f'#{tc} {ans}')
