import sys

sys.stdin = open("미로_input.txt", "r")

def dfs(mat, start, n):
    need_visit = [start]    # 방문할 배열 만들고 시작점 넣기
    mode_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 탐색 방향 리스트
    while need_visit:   # 방문할 곳이 남았다면 반복
        cur = need_visit.pop()  # 스택에서 하나 뽑고 현재 위치로 지정
        mat[cur[0]][cur[1]] = 1     # 현재 위치값 다시 탐색 안하도록 벽(1)로 수정
        for mode in mode_list:      # 각 방향 탐색
            if 0 <= cur[0] + mode[0] < n and 0 <= cur[1] + mode[1] < n:     # 행렬 범위 안에 있다면
                if mat[cur[0] + mode[0]][cur[1] + mode[1]] == 0:    # 탐색 대상 값이 0이라면
                    need_visit.append([cur[0] + mode[0], cur[1] + mode[1]])     # 방문 예정 배열에 추가
                elif mat[cur[0] + mode[0]][cur[1] + mode[1]] == 3:  # 대상이 도착 지점이라면 성공이므로 1 반환
                    return 1
    return 0    # 탐색을 모두 마쳐도 도착 지점이 없었다면 실패이므로 0 반환

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    mat = []

    # 행렬 생성과 동시에 시작점 찾기
    for i in range(n):
        mat.append(list(map(int, input())))
        if 2 in mat[i]:
            start = [i, mat[i].index(2)]

    print('#{} {}'.format(test_case, dfs(mat, start, n)))