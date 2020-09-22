import sys
sys.stdin = open("(5102)노드의 거리_input.txt")

# bfs로 출발점에서부터의 거리 저장
def bfs(v):
    # queue를 만들어 시작점을 넣고
    Q = []
    Q.append(v)
    # 시작점에 방문 표시
    visited[v] = 1
    # 큐가 비어있지 않다면
    while Q :
        # 첫 원소를 pop해서 v에 담고
        v = Q.pop(0)
        # 만약 v가 목적지라면 종료
        if v == G:
            break
        # 아니라면 인접한 노드 중
        for w in li[v] :
            # 방문하지 않은 노드에 대해
            if visited[w] == 0:
                # 큐에 넣고
                Q.append(w)
                # (visited[직전 방문 노드] + 1)을 visited[w]에 넣어줌. 
                visited[w] = visited[v] + 1


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    # 입력은 인접 리스트로 받아온다
    li = [[]*(V+1) for _ in range(V+1)]
    for i in range(E):
        # undirected graph이니 s->e e->s 둘 다 추가
        s, e = map(int, input().split())
        li[s].append(e)
        li[e].append(s)
    S, G = map(int, input().split())
    # 출발점에서부터의 거리가 담길 list
    visited = [0] * (V+1)
    bfs(S)
    result = visited[G]
    # 만약 도착점에 도달했다면,
    if visited[G] > 0:
        # 출발점 = 1이니 1을 빼줌.
        result -= 1
    print('#{} {}' .format(t+1, result))
