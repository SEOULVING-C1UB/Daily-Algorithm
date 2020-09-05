T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # MAP : (list) represent connected points
    MAP = [[] for _ in range(V + 1)]
    for _ in range(E):
        p1, p2 = map(int, input().split())
        MAP[p1].append(p2)
        MAP[p2].append(p1)

    # s,e : start,end point
    s, e = map(int, input().split())
    visited = [0] * (V + 1)
    # Start from 's', find next movable node and increase distance
    q = [s]
    dis = 0
    while q:
        # flag : (boolean) arrive in 'e'
        flag = 0
        next_q = []
        for pos in q:
            # end condition
            if pos == e:
                flag = 1
                break

            # find movable and not visited node
            visited[pos] = 1
            for next_pos in MAP[pos]:
                if not visited[next_pos]:
                    next_q.append(next_pos)

        # end condition
        if flag:
            break

        q = next_q
        dis += 1

    # flag and dis -> flag if not flag else dis
    print(f'#{tc} {flag and dis}')
