def counting_color(white_end, blue_end, origin_flag):
    result = 0
    # 0 줄부터 white가 끝나는 지점까지
    for i in range(0, white_end+1):
        for j in range(m):
            if origin_flag[i][j] != 'W':
                result += 1

    # white_end 다음 줄부터 blue가 끝나는 지점까지
    for i in range(white_end+1, blue_end+1):
        for j in range(m):
            if origin_flag[i][j] != 'B':
                result += 1

    # blue_end 다음 줄부터 마지막 줄까지
    for i in range(blue_end+1, n):
        for j in range(m):
            if origin_flag[i][j] != 'R':
                result += 1

    return result

T = int(input())
for test_case in range(1, T + 1):
    # W 하양 R 빨강 B 파랑
    # W B R 순서로 칠해져야 한다.
    # 각 색상의 시작 행의 경우의 수는 W는 0~N-3까지, B는 1~N-2까지, R은 2~N-1이다.
    answer = 987654321
    n, m = map(int, input().split())
    origin_flag = [ list(input()) for _ in range(n) ]
    # 1. 하양색이 끝나는 지점, 파랑색이 끝나는 지점을 고른다.
    for cw in range(0, n-2):
        for cb in range(cw+1, n-1):
            temp = counting_color(cw, cb, origin_flag) # 구해 놓은 경우의 수를 기반으로 바꾸어야 할 색상이 몇개인지 리턴한다.
            answer = min(temp, answer)

    print('#{0} {1}' .format(test_case, answer))