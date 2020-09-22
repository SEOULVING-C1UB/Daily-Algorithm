for t in range(1,11):
    # 입력값 받기
    V,E = map(int,input().split())          # 노드 수, 간선 수
    tmp = list(map(int,input().split()))    # 간선 정보
    # Graph 생성
    G = [[] for _ in range(V+1)]            # 그래프 행렬, V+1로 인덱스 1로 시작하도록 맞춰줌
    # 입력값 받는 노드 리스트
    to_list = []                            # 입력 없이 출력만 하는 노드를 찾기 위해
    for i in range(E):                      # 입력을 받는 to 노드 리스트를 생성
        f = tmp[2*i]; to = tmp[2*i+1]
        G[f].append(to)
        to_list.append(to)
    # 입력값을 받지 않느 노드 리스트
    start = []                              # to list에 없는 내용을 출발 지점으로 선정
    for g in range(1,V+1):
        if g not in to_list:
            start.append(g)

    S = len(start)                          # S는 출발 지점의 개수
    visit = [[0] * (V+1) for _ in range(S)] # 각 출발지점마다 Visit을 새로 만들어 BFS를 통해 누적 경로 계산
    # BFS
    for s in range(S):                      # 시작 지점을 매번 업데이트 해주며 BFS 시작
        Q = []
        v = start[s]
        Q.append(v)
        visit[s][v] = 1
        while len(Q):                       # BFS 시작
            p = Q.pop(0)
            for w in G[p]:
                Q.append(w)
                visit[s][w] = visit[s][p] + 1   # 초기 출발지점을 1로 계산하여 떨어진 깊이 만큼 +1
    # 순서 통합
    total = [0] * (V+1)                     # 각 visit에는 출발지점에서 도착지점으로 가는 데 필요한 거리의 수가 계산되어 있음
    for s in range(S):                      # 같은 node라고 하더라도 어디서 출발했느냐에 따라 깊이가 달라짐
        for k in range(V+1):                # 따라서 먼저는 초기화 배열을 만들어 낸 후 (total)
            if total[k] <= visit[s][k]:     # visit 정보를 비교하여 가장 나중에 도착할 노드의 순번을 저장함
                total[k] = visit[s][k]      # visit이 서로 겹치지 않는 경우에는 그 값이 그대로 입력됨

    # 정렬하며 인덱스 리턴
    ans = list(range(V+1))                  # 인덱스 정보를 반환해야 하므로
    for i in range(1,V+1):                  # 정렬 시 인덱스를 기억해 줄 평행한 배열 하나를 선언함
        for j in range(i+1,V+1):
            if total[i] > total[j]:
                total[i], total[j] = total[j],total[i]
                ans[i],ans[j] = ans[j], ans[i]  # 버블 정렬을 사용하면서 인덱스 정보도 동일하게 변경해줌

    print('#{}'.format(t),end=" ")          # 정답의 출력 결과를 맞추기 위해 for 반복문 이용
    for i in range(1,V+1):
        print(ans[i],end=" ")
    print("")
