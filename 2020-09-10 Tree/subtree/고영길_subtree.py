T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    info = list(map(int, input().split()))

    # MAP : graph indicate the mainline
    MAP = [[] for _ in range(E + 2)]
    for i in range(E):
        MAP[info[2 * i]].append(info[2 * i + 1])

    # bfs : search all points downward from 'N'
    q = [N]
    ans = 0
    while q:
        pos = q.pop()
        ans += 1
        q.extend(MAP[pos])

    print(f'#{tc} {ans}')
