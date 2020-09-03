# 수업시간에 다룬 예제와 거의 똑같기 때문에 굳이 주석은 달지않았습니다
def bfs(start, goal):
    visit = [0]*(v+1)
    stack = []
    stack.append(start)
    visit[start] = 0
    while stack:
        t = stack.pop(0)
        if t == goal:
            return visit[t]
        for i in range(v+1):
            if G[t][i]:
                if not visit[i]:
                    stack.append(i)
                    visit[i] = visit[t] + 1
    return 0

T = int(input())
for test_case in range(T):
    v, e = map(int, input().split())
    # 인접행렬을 이용
    G = [[0]*(v+1) for _ in range(v+1)]
    for i in range(e):
        s, e = map(int, input().split())
        G[s][e] = 1
        G[e][s] = 1
    s, g = map(int, input().split())
    print('#' + str(test_case + 1), bfs(s, g))
