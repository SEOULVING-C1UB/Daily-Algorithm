def find_set(n):
    if set_id[n] == n:
        return n
    else:
        # use recursion to make people's group number correct.
        set_id[n] = find_set(set_id[n])
        return set_id[n]


for tc in range(int(input())):
    N, M = map(int, input().split())
    app = list(map(lambda x: int(x) - 1, input().split()))
    # set_id: group number
    set_id = [i for i in range(N)]
    cnt = N
    for i in range(M):
        p1, p2 = find_set(app[2 * i]), find_set(app[2 * i + 1])
        if p1 != p2: # make their group number same
            set_id[p2] = set_id[p1]
            cnt -= 1
    print('#{} {}'.format(tc + 1, cnt))
