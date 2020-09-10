import sys
sys.stdin = open('contact_input.txt', 'r')

def bfs(s):
    Q = [s]                                 # Q에 시작점 저장
    visit[s] = 1                            # 해당 시작점 visit 체크

    while Q:
        s = Q.pop(0)
        for w in G[s]:
            if not visit[w]:
                Q.append(w)
                visit[w] = visit[s] + 1


for c in range(1,11):
    N, S = map(int, input().split())
    info = list(map(int, input().split()))
    G = {i:[] for i in range(1, N+1)}               # 인접 딕셔너리로 값을 저장한다
    visit = [0]*(N+1)
    for i in range(0,len(info),2):
        s, e = info[i], info[i+1]
        G[s].append(e)                              # 방향성이 존재한다

    bfs(S)
    maxI = 0
    for i in range(1, N + 1):                       # 가장 나중에 연락받게 되는 사람 중 번호가 가장 큰사람을 찾아준다
        if visit[maxI] <= visit[i]:
            maxI = i

    print('#{} {}'.format(c,maxI))