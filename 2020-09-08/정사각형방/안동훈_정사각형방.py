import sys
sys.stdin = open('정사각형 방_input.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j, arr, visit):
    global room_number, count
    stack = [[i, j]] # 시작점 stack에 담기
    visit[i][j] = 1 # 방문 처리
    sum = 1
    my_room_number = arr[i][j]
    while True:
        if len(stack) == 0: # stack이 빌 때까지 돌린다.
            if sum > count:
                room_number = [my_room_number]
                count = sum
            elif sum == count:
                room_number.append(my_room_number)
            break
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # nx, ny가 범위 이내이며, 방문하지 않았으며, 기존 숫자보다 1 크다면
            if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0 and arr[nx][ny] == arr[cx][cy] + 1:
                visit[nx][ny] = 1
                stack.append([nx, ny])
                sum += 1


T = int(input())
for test_case in range(1, T + 1):
    room_number = [] # 정답 후보군은 여러가지이므로..
    count = 0
    # 입력 파트
    n = int(input())
    arr = [ list(map(int ,input().split())) for _ in range(n) ]

    # 완전 탐색+dfs로 해결하자. 모든 방에서부터 출발한다.
    # 이 때, 방을 한 번 탐색할 때마다 visit 배열을 초기화해주어야 하겠다.
    for i in range(n):
        for j in range(n):
            visit = [ [0]*n for i in range(n) ]
            dfs(i, j, arr, visit)

    room_number = sorted(room_number)

    print("#{0} {1} {2}".format(test_case, room_number[0], count))
