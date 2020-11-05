def bfs(s) :
    if visit[s] == 1 : return
    global counti
    global N

    Q = [s]
    visit[s] = 1

    while Q :
        now = Q.pop(0)
        for w in range(1, N+1) :
            if G[now][w] == 1 and visit[w] == 0 :
                visit[w] = 1
                Q.append(w)
    counti += 1                         # 한 텀 끝나면 마을 수 올린다.

for tc in range(1, int(input())+ 1) :
    counti = 0
    N, M = map(int, input().split())

    visit = [0] * (N+1)

    G = [ [0]*(N+1) for _ in range(N+1) ]       # 2차원 배열을 만든다.

    for i in range(M) :                         # 연결된 부분 모두 1로 처리
        u, v = map(int, input().split())
        G[u][v] = G[v][u] = 1

    for b in range(1, N+1) :                    # 노드 수 만큼 돌린다.
        bfs(b)

    print("#{} {}".format(tc, counti))