import sys

def inorder(node):
    if node != 0:
        inorder(tree[node][2])
        print(tree[node][1], end="")
        inorder(tree[node][3])

sys.stdin = open('중위순회.txt', 'r')

for t in range(1, 11):
    print(f'#{t}', end=" ")
    V = int(input())  # 정점
    E = V - 1  # 간선
    tree = [[0] * 4 for _ in range(V)]
    arr = [list(input().split(' ')) for _ in range(V)]
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            try:
                tree[r][c] = int(arr[r][c])
            except:
                tree[r][c] = arr[r][c]
    tree = [[0, 0, 0, 0]] + tree

    inorder(1)
    print()
