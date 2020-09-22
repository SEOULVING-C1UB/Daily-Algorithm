T = int(input())

def dfs(i, j, count, s):
    # 범위에서 벗어나면 가지치기
    if 0 > i or i >= 4 or 0 > j or j >= 4:
        return
    # 횟수 추가, 숫자 이어붙이기
    count += 1
    s += mat[i][j]
    # 7자리 되면 셋에 추가
    if count == 7:
        num_set.add(s)
        return
    # 4방향 탐색
    dfs(i, j + 1, count, s)
    dfs(i + 1, j, count, s)
    dfs(i, j - 1, count, s)
    dfs(i - 1, j, count, s)

for test_case in range(1, T + 1):
    mat = [input().split() for _ in range(4)]
    # 집합으로 생성
    num_set = set()
    # 모든 점에서 시작하기
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, '')
    print('#{} {}'.format(test_case, len(num_set)))