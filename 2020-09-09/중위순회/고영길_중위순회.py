# If you make tree by class Node is more powerful, smart way
# but you can make tree also by binary list. This is easier way.

def in_order_traversal(idx):
    '''
    To print out left -> root -> right order, use recursion.
    :param idx: index of binary tree
    :return:
    '''
    global ans
    if idx >= N:
        pass
    else:
        # recursion order : left -> root -> right
        in_order_traversal(idx * 2 + 1)
        ans += s[idx]
        in_order_traversal(idx * 2 + 2)


for tc in range(1, 11):
    N = int(input())
    s = ''
    for i in range(N):
        s += input().split()[1]
    ans = ''
    in_order_traversal(0)
    print(f'#{tc} {ans}')
