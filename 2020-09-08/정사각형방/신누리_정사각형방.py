'''
[컨셉]
1) dfs를 통해 갈 수 있는 방을 탐색.
   - 정확히 1만큼 방번호가 커야 해서 stack에는 최대 1개씩 추가되므로, visited에 +1씩 하며 몇개의 방을 옮겼는지 저장.
2) 그렇게 반환된 값을 기존 최댓값과 비교해서 더 크면 최댓값과 방번호 모두 갱신, 같으면 방번호만 비교해 갱신.
'''

def path(x, y) :
    visited = [[0]*N for _ in range(N)]     # 각 점을 순회할 때마다 체크해야해서 함수 내에 위치
    s = []
    s.append((x, y))
    visited[x][y] = 1
    while s :
        a, b = s.pop()
        for d in range(4):
            p, q = a+dir1[d], b+dir2[d]     
            if 0 <= p < N and 0 <= q < N :                              # 배열 범위 내에 있고,
                if arr[a][b] + 1 == arr[p][q] and not visited[p][q]:    # 전 방보다 1 크고 미방문이라면,
                    visited[p][q] = visited[a][b] + 1                   # 전 방보다 1 큰 수를 넣어 몇개 갔는지 확인
                    s.append((p,q))
    return visited[a][b]    # 마지막에 갔던 방번호 return


T = int(input())
for t in range(T) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxi = 1                            # 최댓값을 담을 변수. 적어도 자신의 방은 방문하니 1로 초기화
    idx = arr[0][0]                     # 최댓값이 나온 시작 방번호를 담을 변수.
    dir1 = [1, 0, -1, 0]                # 상하좌우 이동을 위해
    dir2 = [0, 1, 0, -1]
    for i in range(N) :                 # 2차원 배열을 순회하며
        for j in range(N) :
            result = path(i, j)         # 각 방에서 path를 구해봄.
            if result > maxi :          # 최댓값 갱신
                maxi = result
                idx = arr[i][j]
            elif result == maxi :       # 기존 최댓값과 결과값이 같을 때는
                if idx > arr[i][j] :    # 방번호가 작은 쪽으로 저장.
                    idx = arr[i][j]
    print('#{} {} {}' .format(t+1, idx, maxi))
