T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    groups = []
    # check : check the people who don't belong to a group
    check = [False] * N
    for _ in range(M):
        p1, p2 = map(int, input().split())
        # If idx == -1 : not belong to any group
        idx1, idx2 = -1, -1
        check[p1 - 1], check[p2 - 1] = True, True

        # Find which group has p1, p2
        for i in range(len(groups)):
            if p1 in groups[i]:
                idx1 = i
            if p2 in groups[i]:
                idx2 = i


        if idx1 > -1 and idx2 > -1 and idx1 != idx2: # p1, p2 in differnt group
            groups[idx1].update(groups[idx2])
            groups.pop(idx2)
        elif idx1 == -1 and idx2 == -1:              # don't belong any group neither
            groups.append(set([p1, p2]))
        elif idx2 == -1:
            groups[idx1].add(p2)                     # p1 belongs to groups[idx1], add p2
        elif idx1 == -1:
            groups[idx2].add(p1)                     # p2 belongs to groups[idx2], add p1

    # print (number of groups) + number of people who don't belong to any groups
    print(f'#{tc} {len(groups) + check.count(False)}')
