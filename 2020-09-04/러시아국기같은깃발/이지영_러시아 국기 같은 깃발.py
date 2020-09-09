T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # flag = [list(input()) for _ in range(N)]
    flag = [input() for _ in range(N)]
    result = []

    for i in range(0, N-2):

        white = 0
        # 0 ~ i 까지 W찾기
        row1 = flag[:i+1]
        for x in row1:
            for w in x:
                if w != 'W':
                    white += 1

        for j in range(i+1, N-1):

            blue = 0
            row2 = flag[i+1: j+1]
            for y in row2:
                for b in y:
                    if b != 'B':
                        blue += 1

            red = 0
            row3 = flag[j+1:]
            for z in row3:
                for r in z:
                    if r != 'R':
                        red += 1

            result.append(white + blue + red)

    print('#{} {}'.format(tc, min(result)))


