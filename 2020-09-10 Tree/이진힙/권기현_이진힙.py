import sys

sys.stdin = open('5177.txt')
total_tc = int(input())



def minheap(node):
    if tree[node][3]:
        if tree[node][0] < tree[tree[node][3]][0]:
            tree[node][0], tree[tree[node][3]][0] = tree[tree[node][3]][0], tree[node][0]
            minheap(tree[node][3])

#조상들의 합을 구한다
def sum_ancestor(node):
    global result
    if node:
        result += tree[node][0]
        sum_ancestor(tree[node][3])



for tc in range(1, total_tc + 1):
    N = int(input())
    # tree는 value, leftchild, rightchild, parent 로 설정
    tree = [[0, 0, 0, 0] for _ in range (N+1)]
    input_list = list(map(int, input().split()))
    # traverse 함수를 이용해 lefchild, rightchild, parent를 먼저 만ㄷ르어준다

    for k in range(1, N+1):
        if 2*k < N+1:
            tree[k][1] = 2 * k
            tree[2*k][3] = k
        if 2*k +1 < N+1:
            tree[k][2] = 2 * k + 1
            tree[2*k+1][3] = k


    # value 값을 차례대로 입력해주면서 minheap함수를 이용해 sort해준다
    for i in range(N+1):
        tree[i][0] = input_list[i-1]
        minheap(i)

    #조상노드의 합을 구하는 함수
    result = 0
    #자신을 제외한 조상이므로 한단계위의 조상을 값에 넣어준다.
    ancestor = tree[N][3]
    sum_ancestor(ancestor)
    print("#%d %d"%(tc, result))


