import sys
sys.stdin = open('창용 마을 무리의 개수.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    ppl = [[p] for p in range(1, N + 1)]
    for line in arr:
        for i in range(len(ppl)):
            if line[0] in ppl[i]:
                a = ppl.pop(i)
                if len(ppl) == 0:
                    ppl = [a]
                    break
                else:
                    for j in range(len(ppl)):
                        if line[1] in ppl[j]:
                            b = ppl.pop(j)
                            ppl.append(a + b)
                            break
                        elif line[1] in a:
                            ppl.append(a)
                            break
                break
    print(len(ppl))

    # groups = []
    # for line in arr:
    #     if len(groups) > 0:
    #         for group in groups:
    #             if line[0] not in group and line[1] not in group:
    #                 if group == groups[-1]:
    #                     groups.append(line)
    #             else:
    #                 group.append(line[0])
    #                 group.append(line[1])
    #     else:
    #         groups.append(line)
    #
    # print(groups)
    # n = len(groups)
    # for i in range(len(groups)):
    #     for j in range(len(groups)):
    #         for a in set(groups[i]):
    #             if i < j and a in set(groups[j]):
    #                 n -= 1
    #                 break
    # print(n)


