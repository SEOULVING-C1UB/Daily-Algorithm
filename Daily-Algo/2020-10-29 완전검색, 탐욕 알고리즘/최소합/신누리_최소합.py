'''
[컨셉]
1) 0,0에서 시작해 마지막 칸에 다다를 때까지 가능한 모든 경우의 수를 센다.
2) 오른쪽 혹은 아래쪽으로 한 칸 움직인 뒤, 그 위치에서 다시 findmin함수를 호출하는 방식.
   - 처음에 문제를 제대로 읽지 않아 당연히 4방향이라고 생각하고 visited를 썼었는데, 오른쪽/아래로만 움직이니 사실 필요는 없다.
'''

def findmin(x, y, sumi):
    global mini
    if x == N-1 and y == N-1:
        if sumi < mini:
            mini = sumi
    else:
        if sumi < mini:
            for k in range(2):
                p, q = x + dir1[k], y + dir2[k]
                if 0 <= p < N and 0 <= q < N and not visited[p][q]:
                    visited[p][q] = 1
                    findmin(p, q, sumi+arr[p][q])
                    visited[p][q] = 0


dir1 = [1, 0]
dir2 = [0, 1]

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mini = 0xFFFFFFF
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    findmin(0, 0, arr[0][0])
    print('#{} {}' .format(t+1, mini))
