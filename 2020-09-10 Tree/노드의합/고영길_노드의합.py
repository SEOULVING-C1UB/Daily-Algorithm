def sol(n):
    '''
    recursive function finding the leaf node,
    if meet leaf node, add the number.
    :param n: index of tree
    :return: if tree[n] is a number, return tree[n]
    '''
    if n <= N:
        if tree[n] is not None:
            return tree[n]
        else:
            if 2 * n + 1 <= N: # if node has only one sibling
                tree[n] = sol(2 * n) + sol(2 * n + 1)
            else:
                tree[n] = sol(2 * n)
            return tree[n]


for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    # use 'None' to avoid confusing between False and zero. Input number may be zero.
    tree = [None for _ in range(N + 1)]
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val
    sol(1)
    print('#{} {}'.format(tc, tree[L]))
