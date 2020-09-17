# 데이터 입력
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

# 방문표시
visit = [[0] * N for _ in range(N)]

# 한 단지에서 집의 개수
cnt = 0
# 답
ans = []


# 범위 체크
def check(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


# 단지 찾아가기
def find(x, y):
    global cnt
    # 좌우상하
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, -1, 1]
    # 1을 발견하면
    if arr[x][y] == 1:
        # 방문처리하고
        visit[x][y] = 1
        # 좌우상하 차례로 확인
        for d in range(4):
            # 범위체크, 값이 1이고 방문하지 않았을 경우
            if check(x+delta_x[d], y+delta_y[d]) and arr[x + delta_x[d]][y + delta_y[d]] == 1 and visit[x + delta_x[d]][y + delta_y[d]] == 0:
                # 하나의 단지에서 개수 증가
                cnt += 1
                # 방문처리
                visit[x + delta_x[d]][y + delta_y[d]] = 1
                # 다음 집의 인덱스 재귀 호출
                find(x+delta_x[d], y+delta_y[d])


# 모든 인덱스 반복
for i in range(N):
    for j in range(N):
        # 인덱스 값이 1이고 방문하지 않은경우
        if arr[i][j] == 1 and visit[i][j] == 0:
            # cnt를 1부터 시작
            cnt = 1
            find(i, j)
            # 0이 아닌 경우만 단지의 집의 개수 추가
            if cnt != 0:
                ans.append(cnt)
        # 초기화
        cnt = 0

# 오름차순 정렬
for i in range(len(ans)):
    for j in range(len(ans)-i-1):
        if ans[j] > ans[j+1]:
            ans[j+1], ans[j] = ans[j], ans[j+1]

# 출력
print(len(ans))
for i in ans:
    print(i)
