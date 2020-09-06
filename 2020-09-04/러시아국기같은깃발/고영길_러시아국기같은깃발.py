T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    # flag : (list) store numbers of each color in horizontal
    flag = [[f.count('W'), f.count('B'), f.count('R')] for f in flag]
    ans = N * M
    # divide N rows into three sections, calculate the numbers of change in color
    for w in range(1, N - 1):
        for b in range(1, N - 1):
            if w + b >= N:
                continue
            # cnt : (int) maximum numbers of change in color
            cnt = N * M
            # In each section, subtract number you don't need to change
            for j in range(w):  # white section
                cnt -= flag[j][0]
            for j in range(w, w + b):  # blue section
                cnt -= flag[j][1]
            for j in range(w + b, N):  # red section
                cnt -= flag[j][2]
            ans = min(ans, cnt)
    print(f'#{tc} {ans}')
