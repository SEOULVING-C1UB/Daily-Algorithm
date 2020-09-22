T = int(input())

for t in range(1, T + 1):
    # 입력값을 받습니다.
    row, col = map(int, input().split())
    flags = [list(input()) for _ in range(row)]

    # White, Black, Red의 값을 각각 계산하여 더했습니다.
    # 이는 메모리 낭비에 해당하지만, 코딩 할 때는 가독성과 이해에 도움이 되었습니다.
    min_val = row*col       # min_val는 비교를 위한 매개변수로, 최대값으로 나올 수 있는 행*열의 수로 할당했습니다.
    for i in range(0,row-2):
        for j in range(i+1, row-1):
            # 국기를 3가지 부분으로 나눕니다.
            # W로 칠하는 부분, B로 칠하는 부분, R로 칠하는 부분
            # 각 구간 마다 W와 B, R값을 계산한 후 최종적으로 더하여 min_val와 비교합니다.
            W = 0
            B = 0
            R = 0
            for o in range(0,i+1):
                for c in range(col):
                    if flags[o][c] != "W":
                        W += 1
            for m in range(i+1, j+1):
                for c in range(col):
                    if flags[m][c] != "B":
                        B += 1
            for l in range(j+1, row):
                for c in range(col):
                    if flags[l][c] != "R":
                        R += 1

            total = W + B + R
            # 최소값을 비교하며 검증합니다.
            if total > min_val:
                min_val = total

    print('#{}'.format(t), min_val)