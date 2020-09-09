import sys
sys.stdin = open('공통조상.txt', 'r')
# sys.stdin = open('sample_input.txt', 'r')

def pre_order(node):
    global count
    if node == 0 : return
    count += 1
    pre_order(tree[node][0])
    pre_order(tree[node][1])

#기본적인 bfs 틀을 사용했다
def bfs(F,S):
    Qf = [F]
    Qs = [S]
    parentsF = []
    parentsS = []
    visitedF = [0]*(V+1)
    visitedS = [0]*(V+1)
    visitedF[F] = 1
    visitedS[S] = 1
    # 우선 첫번째 대상 F (First)를 돌려서 부모노드가 뭐가 있는지 확인
    while Qf:
        s = Qf.pop(0)
        w = tree[s][2]
        if visitedF[w] == 0 and w != 0:
            Qf.append(w)
            visitedF[w] = 1
            parentsF.append(w)
    # 두번째 대상 S (Second)를 돌리고 만약 첫번째 대상의 부모노드와 중복되는 부모노드가 나오면 멈춘다
    while Qs:
        s = Qs.pop(0)
        w = tree[s][2]
        if visitedS[w] == 0 and w != 0:
            Qs.append(w)
            visitedS[w] = 1
            parentsS.append(w)
        if w in parentsF:
            break
    # 두번째 대상 S의 parentsS에 들어간 마지막 항목은 두 비교대상(F & S)의 부모노드 중 제일 처음 겹치는 부모노드이다
    # 이를 pop() 해서 return 해준다.
    return parentsS.pop()


for c in range(1, int(input())+1):
    V,E,F,S = map(int,input().split())
    data = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(V+1)]
    count = 0

    for i in range(V-1):
        if tree[data[2*i]][0] == 0:
            tree[data[2*i]][0] = data[2*i+1]
        else:
            tree[data[2*i]][1] = data[2*i+1]

        tree[data[2*i+1]][2] = data[2*i]

    x = bfs(F,S)
    # bfs()를 돌려서 얻은 x값을 pre_order(x)을 통해 해당 노드의 자식(?)들의 개수를 counting 한다.
    pre_order(x)
    print('#{} {} {}'.format(c, x, count))