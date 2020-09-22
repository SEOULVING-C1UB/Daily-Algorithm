import sys
sys.stdin = open("정사각형방.txt")

def check(x, y):    # 범위체크 
    if 0 <= x < N and 0 <= y < N: return True
    else: return False

def find(x, y):     # 길찾기
    global cnt
    for d in range(4):  # 상하좌우
        if check(x + delta_x[d], y + delta_y[d]) and arr[x][y] + 1 == arr[x + delta_x[d]][y + delta_y[d]]:
            cnt += 1    # 길 찾을 때마다 cnt += 1
            find(x+delta_x[d], y+delta_y[d])    # 다음 방향으로 재귀호출

T = int(input())

for t in range(1, T+1):
    cnt = 1
    max_cnt = 0
    min_value = 9999999999
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, -1, 1]

    result = []
    # 순서대로 재귀함수 실행
    for x in range(N):
        for y in range(N):
            find(x, y)
            # 함수 호출 후 최대값찾기
            if cnt >= max_cnt:
                result.append([arr[x][y], cnt])
                max_cnt = cnt
            # cnt 초기화
            cnt = 1

    # 경로 최대값이 같을 때 숫자의 최소값 구하기
    for r in result:
        if r[1] == max_cnt and r[0] <= min_value:
            min_value = r[0]

    print("#{} {} {}".format(t, min_value, max_cnt))
