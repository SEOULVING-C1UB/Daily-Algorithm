import sys

sys.stdin = open("input.txt", "r")

T = int(input())

def color(b_start):
    for b_end in range(b_start, n-1):
        count = 0
        for b in range(b_start, b_end + 1):
            count += m - mat[b].count('B')
        for w in range(1, b_start):
            count += m - mat[w].count('W')
        for r in range(b_end + 1, n-1):
            count += m - mat[r].count('R')
        paint.append(count)
    return

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    mat = [list(input()) for _ in range(n)]
    # 각 케이스의 칠해야하는 수를 담는 배열
    paint = []
    # 결과의 초기값에 맨위, 맨아래 각각 흰,적 칠해야하는 수를 넣는다.
    res = 2*m - mat[0].count('W') - mat[-1].count('R')
    # 파랑의 시작점을 두번째에서 뒤에서 두번째까지 탐색
    for b_start in range(1, n-1):
        color(b_start)
    # 가장 적게 칠한 값을 결과에 추가
    res += min(paint)
    print('#{} {}'.format(test_case, res))