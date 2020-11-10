'''
<문제해결>
 : 다익스트라를 이용. 시간초과 해결이 문제.
<추가사항>
1) 처음엔 재귀로 풀었으나 시간이..
2) min, max함수 생각보다 시간 겁나 잡아먹어서 또 실패..
3) 힙 안쓰고 할라고 별짓 다해서 결국 성공
'''

import sys
sys.stdin = open("5250_최소비용.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]         # 각 지점의 높이 저장
    
    dist = [[1000000]*(n) for _ in range(n)]                            # 원점으로 부터의 거리 저장할 리스트. 초깃값은 1000000정도로 크게 설정
    dist[0][0] = 0                                                      # 원점의 거리 0
    visited = [[0]*(n) for _ in range(n)]                               # 방문표시
    cand = []                                                           # 뻗어나갈 후보 정점의 리스트
    sx = sy = 0                                                         # 출발 x, y 좌표
    dx = [0, 0, 1, -1]                                                  # 델타 검색용
    dy = [1, -1, 0, 0]

    while True:
        visited[sy][sx] = 1                                             # 출발점 방문표시
        
        for i in range(4):                                              # 네방향 검색
            tx = sx + dx[i]
            ty = sy + dy[i]
            if 0 <= tx < n and 0 <= ty < n and visited[ty][tx] == 0:    # 검색지점의 인덱스가 범위 안에 들어오고 방문한적이 없으면
                if field[ty][tx]-field[sy][sx] > 0:                     # 검색지점의 높이가 출발지보다 높을 때 거리 비교하여 갱신
                    if dist[ty][tx] > dist[sy][sx] + 1 + field[ty][tx]-field[sy][sx]:
                        dist[ty][tx] = dist[sy][sx] + 1 + field[ty][tx]-field[sy][sx]
                        for j in range(len(cand)):                      # 후보 정점에 집어넣어야하는데 sort를 사용하면 느려지므로 이미 있는 후보들과 비교해 삽입
                            if dist[ty][tx] <= cand[j][2]:
                                cand.insert(j, [tx, ty, dist[ty][tx]])
                                break
                        else:
                            cand.append([tx, ty, dist[ty][tx]])
                        
                else:                                                   # 검색지점의 높이가 출발지보다 낮을때 거리 비교하여 갱신
                    if dist[ty][tx] > dist[sy][sx] + 1:
                        dist[ty][tx] = dist[sy][sx] + 1
                        for j in range(len(cand)):
                            if dist[ty][tx] <= cand[j][2]:
                                cand.insert(j, [tx, ty, dist[ty][tx]])
                                break
                        else:
                            cand.append([tx, ty, dist[ty][tx]])
            ''' min, max써서 망하고, append하고 sort써서 망한 코드
            if 0 <= tx < n and 0 <= ty < n and visited[ty][tx] == 0:
                dist[ty][tx] = min(dist[ty][tx], dist[sy][sx] + 1 + max(0, field[ty][tx]-field[sy][sx]))
                cand.append([tx, ty, dist[ty][tx]])
            '''
        sx, sy = cand[0][0], cand[0][1]                                 # 후보중 맨 앞의것이 가장 작으므로 출발지 갱신
        del cand[0]                                                     # 첫번째 후보 제거.(작은걸 맨뒤로 하면 더 빨라지겠구나..)
        
        if sx == n-1 and sy == n-1:                                     # 마지막 정점에 도달하면 breaks
            break
    print(f'#{tc} {dist[-1][-1]}')

