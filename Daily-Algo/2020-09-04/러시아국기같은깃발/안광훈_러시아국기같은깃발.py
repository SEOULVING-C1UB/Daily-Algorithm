"""
맨 윗줄, 맨 아랫줄은 고정
파란색 줄 위치만 결정되면 나머지는 자동으로 결정되는 성질을 이용
"""

# T: 테스트 케이스 개수
T = int(input())

# t: 테스트 케이스 번호
for t in range(1, T + 1):
    # N: 행, M: 열
    N, M = map(int, input().split())
    colors = [input() for _ in range(N)]

    result = N * M

    # 모든 줄마다 해당 색깔로 바꿨을 경우 바꿔야 하는 개수로 초기화
    for i in range(N):
        W = B = R = 0
        for color in colors[i]:
            if color != 'W':
                W += 1
            if color != 'B':
                B += 1
            if color != 'R':
                R += 1
        colors[i] = [W, B, R]

    # s: 시작 줄, e: 끝나는 줄, c: 색깔 인덱스
    def change_color(s, e, c):
        total = 0
        for i in range(s, e + 1):
            total += colors[i][c]
        return total

    # s: 시작 줄, e: 끝나는 줄
    def get_min(s, e):
        total = 0
        # 흰색 줄
        total += change_color(0, s - 1, 0)
        # 파란색 줄
        total += change_color(s, e, 1)
        # 빨간색 줄
        total += change_color(e + 1, N - 1, 2)
        return total

    for i in range(1, N - 1):
        for j in range(i, N - 1):
            result = min(result, get_min(i, j))

    print('#{} {}'.format(t, result))
