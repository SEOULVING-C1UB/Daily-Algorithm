for tc in range(1, 11):
    V, E = map(int, input().split())
    # MAP[j][i] means that 'i' must precede 'j'.
    MAP = [[0 for i in range(V + 1)] for i in range(V + 1)]
    # check[j] indicate the number of points that must precede 'j'
    check = [0 for _ in range(V + 1)]
    info = list(map(int, input().split()))
    for i in range(E):
        MAP[info[2 * i + 1]][info[2 * i]] = 1
        check[info[2 * i + 1]] += 1

    stack = []
    cnt = 0  # length of stack
    while cnt < V:
        # find the point whose preceding points have been completed
        q = [i for i in range(1, V + 1) if check[i] == 0]
        for point in q:
            stack.append(point)
            check[point] = -1 # visited
            cnt += 1
            # preceding check
            for j in range(1, V + 1):
                if MAP[j][point]:
                    MAP[j][point] = 0
                    check[j] -= 1

    print(f'#{tc} {" ".join(map(str, stack))}')
