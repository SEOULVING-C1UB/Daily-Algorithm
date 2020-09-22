import sys
sys.stdin = open("subtree.txt")

def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())
    tmp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E + 2)]
    cnt = 0

    for i in range(len(tmp)//2):
        p, c = tmp[2 * i], tmp[2 * i + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        elif tree[p][0] != 0:
            tree[p][1] = c
        tree[c][2] = p
    print(tree)
    preorder(N)
    print("#{} {}".format(t, cnt))

