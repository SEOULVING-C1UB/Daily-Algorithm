import sys
sys.stdin = open('1248.txt')

total_tc = int(input())

def anc(node, list_A):
    if node:
        list_A.append(node)
        anc(tree[node][0], list_A)

def traverse(node):
    global count
    if node:
        count += 1
        traverse(tree[node][1])
        traverse(tree[node][2])

for tc in range(1, total_tc + 1):
    V, E, A, B = list(map(int, input().split()))
    temp_list = list(map(int, input().split()))
    #tree 만들기. parent, leftchild, rightchild
    tree = [[0, 0, 0] for _ in range (V+1)]
    for i in range(E):
        parent, child = temp_list[2*i], temp_list[2*i+1]
        if tree[parent][1]==0:
            tree[parent][1]=child
        else:
            tree[parent][2]=child
        tree[child][0] = parent


    #조상의 리스트 뽑기
    list_A = []
    list_B = []
    anc(A, list_A)
    anc(B, list_B)

    #공통리스트중 최소값 구하기
    common_anc = []
    for i in list_A:
        if i in list_B:
            common_anc.append(i)

    for j in common_anc:
        if tree[j][2] not in common_anc and tree[j][1] not in common_anc:
            closest_common_ancestor = j



    #공통조상 트리 크기
    count = 0
    traverse(closest_common_ancestor)

    #정답출력
    print("#%d %d %d"%(tc, closest_common_ancestor, count))