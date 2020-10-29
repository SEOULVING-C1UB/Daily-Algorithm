from itertools import combinations as coms


def is_section(group):
    check = [True for _ in range(N + 1)]
    for i in range(1, len(group)):
        check[group[i]] = False

    q = [group[0]]
    while q:
        cur_edge = q.pop()
        for next_edge in MAP[cur_edge]:
            if not check[next_edge]:
                q.append(next_edge)
                check[next_edge] = True
    return all(check)


MAX = 0xFFFFFFF
N = int(input())
ppls = list(map(int, input().split()))
MAP = {i: [] for i in range(1, N + 1)}
for i in range(1, N + 1):
    MAP[i] = list(map(int, input()[2:].split()))

answer = MAX
for i in range(1, N // 2 + 1):
    for group1 in coms(range(1, N + 1), i):
        group2 = [k for k in range(1, N + 1) if k not in group1]
        if is_section(group1) and is_section(group2):
            answer = min(answer, abs(sum([ppls[x - 1] for x in group1]) - sum([ppls[x - 1] for x in group2])))
if answer == MAX:
    answer = -1
print(answer)
