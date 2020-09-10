# You can notice that if you traverse-inorder range(1,N+1),
# you can make the bst:binary search tree through indexing.


# restore 'cnt' on bst through inorder-traversal index
def inorder(idx):
    global cnt
    if idx <= N:
        inorder(2 * idx)
        bst[idx] = cnt
        cnt += 1
        inorder(2 * idx + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bst = [0 for _ in range(N + 1)]
    cnt = 1
    inorder(1)
    print('#{} {} {}'.format(tc, bst[1], bst[N // 2]))
