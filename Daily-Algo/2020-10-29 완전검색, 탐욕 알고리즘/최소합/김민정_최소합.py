import sys
sys.stdin = open("최소합_input.txt")

dx = [1, 0]
dy = [0, 1]

def path(x, y) :
    global N, result, mini

    if mini < result : return       # 가지치기

    if x == N-1 and y == N-1 :
        mini = result
        return

    for i in range(2) :     # 방향이 오른쪽과 아래 뿐이므로 2번 돌린다.
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < N and ny < N and (nx, ny) not in visited :  # 범위체크, 방문체크
            visited.append((nx, ny))        # 해당되면 방문목록에 넣는다.
            result += arr[nx][ny]           # 결과값에 값을 더해준다.
            path(nx, ny)                    # 재귀 돌린다.
            visited.remove((nx, ny))        # 원래 위치로 방문안함으로 돌려놓기
            result -= arr[nx][ny]           # 결과값에서도 원래로 되돌려놓기

for tc in range(1, int(input())+1) :
    mini = 999999999
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    result = arr[0][0]

    path(0, 0)

    print("#{} {}".format(tc, mini))