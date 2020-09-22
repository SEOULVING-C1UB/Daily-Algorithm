import sys

sys.stdin = open('5178.txt')

total_tc = int(input())


for tc in range(1, total_tc + 1):
    N, M, L = map(int, input().split())
    #value leftchild rightchild parent
    tree = [[0, 0, 0, 0 ] for _ in range (N+1)]
    node_with_value=[]

    for k in range(1, N+1):
        if 2*k < N+1:
            tree[k][1] = 2 * k
            tree[2*k][3] = k
        if 2*k +1 < N+1:
            tree[k][2] = 2 * k + 1
            tree[2*k+1][3] = k

    for i in range (M):
        node, value = map(int, input().split())
        tree[node][0] = value
        node_with_value.append(node)


    for j in range(N, 0, -1):
        if j not in node_with_value:
            tree[j][0] = tree[tree[j][1]][0] + tree[tree[j][2]][0]

    print("#%d %d"%(tc, tree[L][0]))





