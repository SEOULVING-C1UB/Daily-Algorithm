import sys

sys.stdin = open('1231.txt')

total_tc = 10

def inorder(node):
    global N
    if node<=N and tree[node]:
        inorder(node*2)
        print(tree[node][1], end='')
        inorder(node*2 +1)



for tc in range(1, total_tc +1):
    N = int(input())
    tree = [[0, 0, 0, 0] for _ in range (N+1)]
    for j in range(1, N+1):
        temp = list(input().split())
        len_temp = len(temp)
        for i in range (len_temp):
            tree[j][i] = temp[i]
    print('#%d'%(tc), end=' ')
    inorder(1)
    print()





