import sys

sys.stdin = open("D4_1238_input.txt", "r")


def bfs_call(v):
    # 딕셔너리를 이용하여 해당 노드의 깊이 표시
    # 딕셔너리를 사용한 이유는 디버깅 편의성: 
    # 리스트의 경우 노드가 몇개인지 모르니 최대 길이(100개)를 설정해야 해서 보기 불편
    visit = {}
    stack = []
    stack.append(v)
    # 초기 노드 깊이를 1로 주어 while문 내 유효성 검사에 걸리지 않게끔
    visit[v] = 1
    while stack:
        t = stack.pop(0)        
        for w in G[t]:          
            # 방문한 적 없으면 딕셔너리이기 때문에 None이 리턴됨  
            if not visit.get(w):
                stack.append(w)                
                visit[w] = visit[t] + 1
    result = 0
    num = 0
    for i in range(101):
        temp = visit.get(i)
        if temp and temp >= num:
            num = visit.get(i)
            result = i
    return result


for test_case in range(10):
    lenth, start = map(int, input().split())
    # 딕셔너리를 이용하여 인접리스트 생성
    G = {i:[] for i in range(101)}
    edges = list(map(int, input().split()))
    i = 0
    while i < lenth:
        f, t = edges[i], edges[i+1]
        G[f].append(t)
        i += 2
    print('#' + str(test_case + 1), bfs_call(start))
