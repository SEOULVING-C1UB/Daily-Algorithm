import sys
sys.stdin = open('노드의거리_input.txt','r')

def bfs(v):
    Q = [v]
    visited = [0] *(V+1)
    visited[v] = 1

    while Q:
        v = Q.pop(0)
        if v == end:                            # 도착 노드에 도착하면 해당 노드까지의 거리를 return 해준다
            return visited[v] - 1
        for w in range(1,V+1):
            if arr[v][w] == 1 and visited[w] == 0:      # 노드가 서로 연결되어있고 방문하지 않았으면 진행
                Q.append(w)                             # 큐에 해당 노드를 append하고
                visited[w] = visited[v] + 1             # 이전 노드의 visited 값을 현재 노드의 visited값에 +1과함께 저장한다
    return 0



for c in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        s,e = map(int, input().split())
        arr[s][e] = 1                           # 방향성이 존재하지 않는다
        arr[e][s] = 1
    start, end = map(int,input().split())

    print('#{} {}'.format(c,bfs(start)))


## 인접 딕셔너리를 이용    
# def bfs(v):
#     Q = []
#
#     Q.append(v)
#     visited[v] = 1
#
#     while Q:
#         v = Q.pop(0)
#         for w in arr[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = visited[v] +1
#                 if w == end:
#                     return visited[w]-1
#     return 0
#
#
# for c in range(1, int(input())+1):
#     V, E = map(int, input().split())
#     arr = {i:[] for i in range(1,V+1)}
#     visited = [0]*(V+1)
#     for i in range(E):
#         s,e = map(int, input().split())
#         arr[s].append(e)
#         arr[e].append(s)
#     start, end = map(int, input().split())
#
#
#     print('#{} {}'.format(c,bfs(start)))