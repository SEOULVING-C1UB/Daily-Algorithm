'''
[컨셉]
1) 입력을 받아온다.
2) 땅인 모든 지점에서 bfs를 응용한 find_treasure을 시행한다.
  - 그 지점에서부터 가장 먼 거리의 땅인 지점을 찾아 반환하고, 결과값인 maxi를 update한다.
'''

def find_treasure(x,y):                                             # bfs 응용
    visited = [[0]*M for _ in range(N)]                             # 방문 체크할 배열
    Q = [(x,y)]                                                     # Queue에 시작점을 넣고
    visited[x][y] = 1                                               # 방문 체크 의미에서 1을 넣음
    while Q:                                                        # 큐가 비어있지 않은 동안
        a, b = Q.pop(0)                                             # pop
        if treasure[a][b] == 'L':                                   # 해당 지점이 땅이면
            for k in range(4):                                      # 4방향으로 움직이며
                p, q = a+dir1[k], b+dir2[k]
                if 0<=p<N and 0<=q<M:                               # 움직인 지점이 배열의 범위 내에 있고
                    if not visited[p][q] and treasure[p][q] == 'L': # 아직 방문되지 않았으며, 땅이라면
                        visited[p][q] = visited[a][b]+1             # 직전 지점 +1을 visited에 넣고
                        Q.append((p,q))                             # 큐에 추가한다
    ans = 0                                                         # 가장 먼 거리를 찾기 위한 변수
    for n in range(N):                                              # 2차원 배열을 순회하며 
        for m in range(M):
            if visited[a][b] > ans :                                # 최댓값 찾기
                ans = visited[a][b]
    return ans-1                                                    # 시작점에 1을 넣었으니, 거리를 알기 위해 1을 빼서 반환

# 컨셉 1
N, M = map(int, input().split())
treasure = [list(input()) for _ in range(N)]

# 4방향으로 움직이기 위한 dir
dir1 = [1, 0, -1, 0]
dir2 = [0, 1, 0, -1]

# 컨셉 2
maxi = 0                                    # 결과값을 저장할 변수
for n in range(N):                          # 모든 땅인 지점에 대해 find_treasure
    for m in range(M):
        if treasure[x][y] == 'L':
            result = find_treasure(n, m)    # find_treasure을 시행해, 가장 먼 지점까지의 거리 반환
            if result > maxi:               # maxi와 비교해서 갱신
                maxi = result
print(maxi)                                 # 결과값 print