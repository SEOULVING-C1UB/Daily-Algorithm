def finder(s) :  # 트리에서 부모의 부모를 물고 올라가는 형식. 조상들을 parents에 append
    if tree[s][2] == 0 :     # 다음 부모 값이 0일 경우, 최상위 노드기 때문에 
        parents.append(s)    # 조상리스트에 넣고, 함수 종료
        return
    else :                  # 다음 부모 값이 존재 할 경우
        parents.append(s)   # 조상 리스트에 넣고
        finder(tree[s][2])  # 해당 부모 값으로 재귀함수 실행


def matcher() :     # a노드 조상리스트와 b노드 조상리스트에서 공통된 조상을 찾는 함수
    for a in ap :
        for b in bp :
            if a == b : return a


def counter(node) : # 서브트리의 수를 세는 함수
    global counti
    if node :
        counter(tree[node][0])
        counti += 1
        counter(tree[node][1])


for tc in range(1, int(input())+1) :
    V, line, a, b = map(int, input().split())   # 노드, 간선 수, a, b 
    lines = list(map(int, input().split()))     # 간선 정보 입력
    tree = [ [0]*3 for _ in range(V+1)]         # [왼쪽,오른쪽,부모] 정보 저장할 2차원배열 선언

    for i in range(0, len(lines), 2) :          # 간선 정보를 통해 2차원 배열에 정보 입력
        p, c = lines[i], lines[i+1]
        if tree[p][0] == 0 :                    # 왼쪽 노드에 적힌 값이 없으면 
            tree[p][0] = c                      # 왼쪽 노드에 정보 저장
        else :                                  # 왼쪽 노드에 적힌 값이 있으면
            tree[p][1] = c                      # 오른쪽 노드에 정보 저장
        tree[c][2] = p                          # 부모 정보를 저장

    parents = []                                # 조상리스트 선언
    finder(a)                                   # a의 조상리스트 조사 함수 실행
    ap = parents[:]                             # parents정보를 ap에 카피
    parents = []                                # b 조상리스트 저장을 위해 다시 초기화
    finder(b)                                   # b의 조상리스트 조사 함수 실행
    bp = parents[:]                             # parents정보를 bp에 카피

    counti = 0                                  # 서브트리 수를 저장할 변수 선언

    result = matcher()                          # a와 b의 공통 조상 찾는 함수 실행 후 result에 저장
    counter(result)                             # 공통조상의 서브트리 수 세는 함수 실행

    print("#{} {} {}".format(tc, result, counti))








