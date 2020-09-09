def dfs(i, j, number, cnt):
    if cnt == 7: # 길이가 7이 되면 set에 넣는다.
        numbers.add(number)
        return

    number += grid[i][j]

    # 상하좌우를 돌며 number를 추가한다.
    if i - 1 >= 0:
        dfs(i - 1, j, number, cnt + 1)
    if i + 1 < 4:
        dfs(i + 1, j, number, cnt + 1)
    if j - 1 >= 0:
        dfs(i, j - 1, number, cnt + 1)
    if j + 1 < 4:
        dfs(i, j + 1, number, cnt + 1)

T = int(input())
for test_case in range(1, T + 1):
    # 중복을 제거하기 위해서 number들을 담을 numbers를 선언
    numbers = set()
    answer = 0
    grid = [ list(input().split()) for _ in range(4) ]
    # 시작 지점 구하기
    for i in range(4):
        for j in range(4):
            dfs(i, j, '', 0)

    answer = len(numbers)
    print('#{0} {1}' .format(test_case, answer))
