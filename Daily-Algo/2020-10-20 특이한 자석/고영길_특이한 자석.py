from collections import deque


def rotate(start_idx, idx, di):
    op_di = -1 if di == 1 else 1
    if idx < 3 and mgs[idx][2] != mgs[idx + 1][6] and start_idx < idx + 1:
        rotate(start_idx, idx + 1, op_di)
    if idx > 0 and mgs[idx][6] != mgs[idx - 1][2] and start_idx > idx - 1:
        rotate(start_idx, idx - 1, op_di)


    if di == 1:
        mgs[idx].appendleft(mgs[idx].pop())
    else:
        mgs[idx].append(mgs[idx].popleft())


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    mgs = [deque(map(int, input().split())) for _ in range(4)]

    for i in range(K):
        idx, di = map(int, input().split())
        rotate(idx - 1, idx - 1, di)

    answer = 0
    for i in range(4):
        if mgs[i][0]:
            answer += 2 ** i

    print(f'#{tc} {answer}')
