from _collections import deque
from copy import deepcopy

for tc in range(1, 11):
    N, start = map(int, input().split())
    infos = list(map(int, input().split()))
    # cont : (dict) store every path from point to point
    cont = dict()
    for i in range(N // 2):
        if infos[i * 2] in cont:
            if infos[i * 2 + 1] not in cont[infos[i * 2]]:
                cont[infos[i * 2]].append(infos[i * 2 + 1])
        else:
            cont[infos[i * 2]] = [infos[i * 2 + 1]]
    # Start from 'start', find every movable point
    q = [start]
    visited = []
    while q:
        # Use 'deepcopy' for nested list
        tmp_q = deque(deepcopy(sorted(q)))
        q = []
        while tmp_q:
            pos = tmp_q.popleft()
            visited.append(pos)
            if pos in cont:
                for next in cont[pos]:
                    if next not in visited:
                        q.append(next)
    print(f'#{tc} {pos}')
