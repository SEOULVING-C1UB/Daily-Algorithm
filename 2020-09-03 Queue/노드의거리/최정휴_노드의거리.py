'''
기본컨셉
1) bfs 사용
2) depth를 계산하면 그게 거리.
3) depth계산을 위해 기존 bfs에서 pop을 이용하지않고 인덱스를 움직여가며 연산
4) 현재 깊이의 for이 끝나면 depth증가

주의사항
1) dfs에 dist만 추가하면 될줄 알고 돌렸는데 7개까지인가 맞더라
2) 이유는 s에서 e로 가는 경로가 여러가지일 수 있기 때문
'''

import sys
sys.stdin = open("5102_노드의거리.txt")

def bfs(v):
    queue=[]                                                # 큐생성
    queue.append(v)                                         # 큐에 현재 노드 저장
    visited[v] = 1                                          # 방문 표시
    now = 0                                                 # 시작 인덱스 초기화
    depth = 0                                               # 깊이 초기화
    while len(queue) != now:                                # 시작 인덱스가 큐길이와 같아지면 끝
        depth += 1                                          # 반복문 돌릴때 마다 깊이 1증가
        for i in range(now,len(queue)):                     # 시작 인덱스 부터 끝까지 현재 깊이 탐색
            now += 1                                        # 탐색 할때 마다 인덱스 증가
            t = queue[i]                                    # 현재 노드
            for w in range(1, V+1):
                if edges[t][w] == 1 and visited[w] == 0:    # 연결되어 있고 방문하지 않았으면
                    if w == e:                              # 종착지이면
                        ans.append(depth)                   # 현재 깊이 ans에 추가후 리턴
                        return
                    else:
                        queue.append(w)                     # 종착지가 아니면 노드 큐에 저장
                        visited[w] = 1                      # 방문 표시

t = int(input())

for i in range(1,t+1):
    V, E = map(int,input().split())
    visited = [0]*(V+1)
    edges = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int,input().split())
        edges[s][e] = 1
        edges[e][s] = 1
    s, e = map(int, input().split())
    ans = [0]                                               # ans에 미리 0을 넣어놔 연결되지않으면 0 출력
    bfs(s)
   
    print("#{} {}".format(i, ans[-1]))
