import sys

sys.stdin = open("미로의거리_input.txt", "r")

T = int(input())

def dfs(i, j, count):
    global res
    # 범위를 벗어나거나 벽을 만나면 해당 탐색 끝
    if i < 0 or i >= n or j < 0 or j >= n or maze[i][j] == '1':
        return
    # 목표를 만나면 결과값을 추가하고 끝('3'인 칸은 세지 않으므로 -1 해줌)
    if maze[i][j] =='3':
        res = count - 1
        return 
    # 가지치기: '1'로 값을 업데이트해 다음에 다시 탐색하지 않게함
    maze[i][j] = '1'
    # 4방향 탐색
    dfs(i+1, j, count+1)
    dfs(i-1, j, count+1)
    dfs(i, j+1, count+1)
    dfs(i, j-1, count+1)



for test_case in range(1, T + 1):
    res = 0
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    # '2'인 곳에서 탐색 시작
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                dfs(i, j, 0)
    print('#{} {}'.format(test_case, res))