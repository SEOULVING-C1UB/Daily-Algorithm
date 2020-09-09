for tc in range(1, 11):

    N, start = map(int, input().split())
    tmp = list(map(int, input().split()))

    contact = [[0] * 101 for _ in range(101)]   # 1~100까지니까 101까지

    # 두칸씩 건너뛰기 => a b a b 이렇게 들어오니까
    for i in range(0, N, 2):
        # 모든 i번째는 a고 모든 i+1번째는 b다
        contact[tmp[i]][tmp[i+1]] = 1

    # 방문정보 저장용 배열
    visit = [0] * 101

    # 시작점을 미리 넣어두면서 Q를 시작
    Q = [start]

    # 시작점은 처음부터 방문처리
    visit[start] = 1

    # 큐에 뭔가 있을 동안
    while Q:

        # v에 큐에 있는 시작점을 받아서
        v = Q.pop(0)

        # 1~100까지 훑으면서 인접&방문안한 위치 찾기
        for w in range(1, 101):
            if contact[v][w] and not visit[w]:

                # 해당 위치가 있다면 그 전 위치에서 +1해줘야 점점 증가하도록 할 수 있음
                visit[w] = visit[v] + 1
                Q.append(w)

    ans = 1
    for i in range(2, 101):

        # 큰 값이 여러개 있을 때 위치가 뒤에 있는 걸 리턴해야함
        if visit[ans] <= visit[i]:
            ans = i

    print('#{} {}'.format(tc, ans))