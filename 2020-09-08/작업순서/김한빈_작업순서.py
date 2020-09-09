import sys

sys.stdin = open('작업순서.txt', 'r')
for t in range(1, 11):
    print(f'#{t}', end=" ")
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[0] * V for _ in range(V)] # 빈 행렬 생성
    for i in range(0, len(arr), 2): # 인접행렬 생성, r에서 c로 향하면 1
        r, c = arr[i] - 1, arr[i + 1] - 1
        graph[r][c] = 1

    temp = []
    for i in range(1, len(arr), 2): # 진입 차수 생성 위해 입력을 받는 노드만 리스트 삽입
        temp.append(arr[i])
    dic = {}
    for e in range(1, V + 1):
        dic[e] = temp.count(e) # 딕셔너리 자료형으로 진입 차수 생성
    stack = []
    while len(stack) != V: # 작업 순서가 전체 노드 수와 같아질때까지 반복
        for k, v in dic.items():
            if v == 0: # 진입 차수가 0일 때
                stack.append(k) # stack에 해당 노드(key) 추가
                dic[k] -= 1 # 진입 차수 딕셔너리에서 더 이상 영향을 끼치지 못하도록 -1로 만듦
                for c in range(V):
                    if graph[k - 1][c] == 1: # 0인 노드와 연결된 노드 찾기
                        dic[c + 1] -= 1 # 해당 노드의 진입차수 감소
    for s in stack:
        print(s, end=" ")
    print()

