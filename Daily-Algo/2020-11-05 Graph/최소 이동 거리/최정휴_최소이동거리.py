'''
<문제해결>
 : 다익스트라 알고리즘 사용
'''


import sys
sys.stdin = open("5251_최소이동거리.txt")


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    field = [[0]*(n+1) for _ in range(n+1)]         # 가중치를 저장 할 리스트
    dist = [0] + [1000000]*n                        # 거리를 저장 할 리스트
    visited = [0]*(n+1)                             # 방문 표시
    for _ in range(m):
        s, e, w = map(int, input().split())
        field[s][e] = w                             # 단방향으로 저장
    s = 0                                           # 시작점 0으로 설정
    while True:
        visited[s] = 1                              # 출발점 방문 표시
        for i in range(n+1):                        # 모든 정점을 순회하며 출발점과 연결되어있으면 거리 갱신
            if field[s][i]:
                dist[i] = min(dist[i], dist[s]+field[s][i])
        m = 1000000
        for i in range(n+1):                        # 모든 정점을 순회하며 방문하지 않은 점 중에 거리가 가장 작은 점을 찾아 출발점 갱신
            if visited[i] == 0 and dist[i] < m:
                m = dist[i]
                s = i
        if 0 not in visited:                        # 모든 점을 방문하면 breaks
            break
    print(f'#{tc} {dist[-1]}')