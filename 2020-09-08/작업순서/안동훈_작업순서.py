import sys
sys.stdin = open('작업순서_input.txt')

def dfs(node, require, visit):
    visit[node] = 1
    answer.append(node)
    for i in range(1,len(require)):
        try:
            require[i].remove(node) # 필요 작업 목록들을 삭제합니다.
        except ValueError:
            pass
    while True:
        if len(answer) == v: # 모든 정점이 작업을 마치면 종료
            return
        for k in range(1, len(require)):
            if len(require[k]) == 0 and visit[k] == 0: # 필요 작업이 없고 방문하지 않았다면
                visit[k] = 1
                answer.append(k)
                for j in range(1, len(require)):
                    try:
                        require[j].remove(k)  # 필요 작업 목록들을 삭제합니다.
                    except ValueError:
                        pass


T = 10
for test_case in range(1, T + 1):
    answer = [] # 정답을 담을 리스트
    v, e = map(int, input().split()) # 정점의 총 수 v, 간선의 총 수 e
    require = [[] for _ in range(v+1)] # 각 정점(idx)마다 먼저 작업을 마쳐야 하는 정점(v)를 담는다.
    visit = [0]*(v+1) # 방문 체크를 위한 배열
    works = list(map(int ,input().split())) # 작업 순서 리스트에 담는다.
    for i in range(0, len(works), 2):
        require[works[i+1]].append(works[i]) # i 출발 정점(먼저 작업을 해야함) i+1은 도착 정점

    # 필요 요구 작업이 없는 정점에서부터 dfs를 시작한다.
    for i in range(1, len(require)):
        if len(require[i]) == 0 and visit[i] == 0:
            dfs(i, require, visit)


    # 출력 부분
    print("#{0}".format(test_case), end = " ")
    for ans in answer:
        print(ans, end = ' ')
    print()