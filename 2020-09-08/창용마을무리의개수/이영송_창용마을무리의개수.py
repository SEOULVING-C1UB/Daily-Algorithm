T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    tmp = [list(map(int,input().split())) for _ in range(M)]
    # 인접 리스트 표현
    connect = [[] for _ in range(N+1)]
    for m in range(M):
        t1 = tmp[m][0]; t2 = tmp[m][1]
        connect[t1].append(t2)
        connect[t2].append(t1)
    # 방문 정보를 통해 GROUP 정보 계산
    visit = [0] * (N+1)
    # 그룹 정보로 업데이트 해 줄 flag 변수
    flag = 0
    # stack 자료 구조를 통한 업데이트
    for i in range(1,N+1):
        # 리스트의 최대 크기는 N, 인덱스는 1부터 시작
        # 각 사람을 모두 점검하여 visit(group)여부 체크
        start = i
        S = []
        # group 여부가 체크되면 flag의 값을 업데이트 하여 다른 그룹으로 분류 시작
        if not visit[start]:
            flag += 1
            S.append(start)
            # while 문을 통해 stack자료구조를 이용하여 DFS 순회
            while len(S):
                v = S.pop()
                if not visit[v]:
                    visit[v] = flag
                    for w in connect[v]:
                        S.append(w)
    # visit의 최대 값 = group의 개수
    print('#{} {}'.format(t,max(visit)))