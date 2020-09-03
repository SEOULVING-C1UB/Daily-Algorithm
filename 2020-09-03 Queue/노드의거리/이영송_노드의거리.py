'''
기본컨셉
- enQ를 이용한 BFS에서 방문 시 정점 노드(v)에 대해
- 간선 노드(w)의 방문 정보 visit[w]를 visit[v] + 1로 저장
* 주의사항: 두 지점 사이의 거리는 탐색하면서 방문한 회수와 다름
'''

import sys
sys.stdin = open('(5102)_input.txt')

T = int(input())

# enQ visit 체크를 통해 방문 정보를 저장합니다.
def bfs(s,g):
    global result
    visit = [0] * (V+1)
    Q = []

    Q.append(s)
    visit[s] = 1
    while len(Q) != 0:
        v = Q.pop(0)
        for w in node[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = visit[v] + 1 # 방문 정보에 대해 v를 기준으로 w를 업데이트 합니다.
                if w == g:
                    result = visit[w] - 1 #거리 정보는 방문한 횟수와 다릅니다.
                    break

for t in range(1,T+1):
    V, E = map(int,input().split())
    node = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int,input().split())
        node[a].append(b)
        node[b].append(a)
    S, G = map(int,input().split())
    result = 0                          # result 정보를 0으로 세팅하고 global로 변화시킵니다.
    bfs(S,G)
    print('#{} {}'.format(t,result))