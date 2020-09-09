T = int(input())
for tc in range(1, T + 1):
    V, E, t1, t2 = map(int, input().split())
    # tree[i] = [left, right, parent]
    tree = [[None, None, None] for _ in range(V + 1)]
    info = list(map(int, input().split()))
    for i in range(E):
        p1, p2 = info[2 * i], info[2 * i + 1]
        if tree[p1][0] is None:
            tree[p1][0] = p2
        else:
            tree[p1][1] = p2
        tree[p2][2] = p1

    # cp : boolean list indicates that the each point is common parent of t1 and t2
    cp = [False] * (V + 1)
    near_cp = False
    pos = [t1, t2]
    while not near_cp:
        for i in range(2):
            parent = tree[pos[i]][2]
            if parent is None:  # doesn't have parent
                pass
            else:
                if cp[parent]:  # found common parent
                    near_cp = parent
                    break
                else:
                    cp[parent] = True
                    pos[i] = parent

    # find all sibling from near_cp
    ans = 0
    q = [near_cp]
    while q:
        pos = q.pop()
        ans += 1
        for i in range(2):
            if tree[pos][i] is not None:
                q.append(tree[pos][i])
    print(f'#{tc} {near_cp} {ans}')