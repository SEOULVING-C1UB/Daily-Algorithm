'''
<문제해결>
 : 프림과 크루스칼 이용함
<추가사항>
1) 힙없이 구현하느라 힘들었다..
2) 마찬가지로 상호배타 집합 없이 구현하느라 힘들었다..
'''

import sys
sys.stdin = open("5249_최소신장트리.txt")

t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())

    # 프림
    field = [[0]*(v+1) for _ in range(v+1)]         # 가중치를 저장할 리스트
    dist = [0] + [1000000]*(v)                      # 거리를 저장할 리스트
    visited = [0]*(v+1)                             # 방문표시
    
    for _ in range(e):                              # 각 지점사이의 가중치 저장
        s, e, w = map(int, input().split())

        field[s][e] = field[e][s] = w
    s = 0                                           # 출발점 0으로 
    ans = 0                                         # 정답을 담을 변수
    while True:
        visited[s] = 1                              # 방문표시
        for i in range(v+1):                        # 모든 정점에 대하여
            if field[s][i]:                         # 출발점과 연결되어있는경우 현재 거리와 출발점으로부터의 거리 중 작은 값을 거리로 선정
                dist[i] = min(dist[i], field[s][i])
        m = 1000000                                 # 크기 비교 대상이 될 아주 큰 수
        for i in range(v+1):                        # 모든 정점에 대해
            if visited[i] == 0 and dist[i] < m:     # 아직 방문 전인 정점들 중 거리가 최소인 점을 찾아 출발점으로 설정
                m = dist[i]
                s = i
        if 0 not in visited:                        # 모든 점의 방문이 끝나면 break
            break
        ans += m                                    # 정답에 현재 최솟값 추가
    print(f'#{tc} {ans}')

    # 크루스칼
    field = [list(map(int, input().split())) for _ in range(e)]
    ans = 0
    p = [[i] for i in range(v+1)]                   # 부모들의 리스트
    field.sort(key=lambda x : x[2])                 # 간선들을 가중치가 작은 순으로 정렬
    i = 0                                           # 간선들을 방문할 인덱스
    c = 0                                           # depth를 확인할 변수
    while True:
        for par in p[field[i][0]]:                  # i번째 간선의 시작점의 부모들에 대해
            if par in p[field[i][1]]:               # i번째 간선의 도착점의 부모와 겹치는 부모가 있으면
                i += 1                              # 해당간선은 건너뛰고
                break
            else:                                   # 존재하지 않으면
                ans += field[i][2]                  # 해당 간선의 가중치를 정답에 추가하고
                c += 1                              # depth도 1증가
                new = list(set(p[field[i][0]] + p[field[i][1]]))
                for j in new:                       # 시작점과 도착점의 부모들을 합친 후 각 부모들의 부모집합도 갱신
                    p[j] = new
                break
            if c >= v:                              # depth가 마지막에 도달하면 break
                break
        if c >= v:
            break
                
    print(f'#{tc} {ans}')