# bfs에 출발점으로부터 거리 추가.
def bfs(v) :
    # 큐에 시작점을 넣고
    Q = []
    Q.append(v)
    # 방문했음을 표시
    visited[v] = 1
    # 큐가 비어있지 않다면
    while Q :
        # 노드를 빼서
        v = Q.pop(0)
        # 주위에 있는 노드 중
        for w in G[v] :
            # 방문하지 않은 노드에 대해
            if visited[w] == 0 :
                # 큐에 넣고
                Q.append(w)
                # (직전 노드 + 1)로 방문 표시
                visited[w] = visited[v] + 1
    

for tc in range(1, 11) :
    E, start = map(int, input().split())
    temp = list(map(int, input().split()))
    # 가장 높은 번호를 가진 사람 기준으로 리스트 생성
    N = max(temp)
    # 인접 리스트로 입력을 받아오기
    G = [[] for _ in range(N+1)]
    for k in range(0, E, 2) :
        f = temp[k]
        t = temp[k+1]
        G[f].append(t)
    # 방문 표시할 list
    visited = [0]*(N+1)
    # start에서 시작해서 bfs
    bfs(start)
    # maxi에는 가장 멀리 있는 노드가 몇 번 걸쳐 간 것인지 담김
    maxi = 0
    # visited를 순회하며 최댓값 갱신
    for i in range(N+1) :
        # 가장 멀리 있는 노드 중 가장 큰 번호이기에 >= 으로 설정.
        if visited[i] >= maxi :
            maxi = visited[i]
            # 그리고 갱신된 최댓값에 맞춰, 그 번호가 몇 번인지 저장.
            idx = i
    print('#{} {}' .format(tc, idx))