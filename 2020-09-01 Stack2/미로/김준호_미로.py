import sys

sys.stdin = open("미로_input.txt", "r")

def dfs(mat, start, n):
    need_visit = [start]
    mode_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while need_visit:
        cur = need_visit.pop()
        mat[cur[0]][cur[1]] = 1
        for mode in mode_list:
            if 0 <= cur[0] + mode[0] < n and 0 <= cur[1] + mode[1] < n:
                if mat[cur[0] + mode[0]][cur[1] + mode[1]] == 0:    # 탐색할 인덱스가 범위안에 존재하고, 그 값이 1이라면
                    need_visit.append([cur[0] + mode[0], cur[1] + mode[1]])
                elif mat[cur[0] + mode[0]][cur[1] + mode[1]] == 3:
                    return 1
    return 0

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    mat = []

    for i in range(n):
        mat.append(list(map(int, input())))
        if 2 in mat[i]:
            start = [i, mat[i].index(2)]

    print('#{} {}'.format(test_case, dfs(mat, start, n)))