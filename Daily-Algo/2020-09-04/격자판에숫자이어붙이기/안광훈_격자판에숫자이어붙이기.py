# T: 테스트 케이스 개수
T = int(input())

# t: 테스트 케이스 번호
for t in range(1, T + 1):
    # board: 격자판 리스트, numbers: 만든 숫자들 저장 셋
    board = [input().split() for _ in range(4)]
    numbers = set()

    # 상하좌우 이동
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # x: 현재 숫자 x 좌표, y: 현재 숫자 y 좌표, n: 현재 숫자 길이
    def get_number(x, y, n):
        # 숫자 길이가 7일 때
        if len(n) == 7:
            numbers.add(n)
            return

        for k in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                new_n = n + board[new_y][new_x]
                get_number(new_x, new_y, new_n)


    for i in range(4):
        for j in range(4):
            get_number(i, j, board[j][i])

    print('#{} {}'.format(t, len(numbers)))
