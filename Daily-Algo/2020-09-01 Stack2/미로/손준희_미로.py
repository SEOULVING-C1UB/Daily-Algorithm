import sys
sys.stdin = open('미로_input.txt', 'r')

def find_start_pos(N):      # 도착점 찾는 함수
    for y in range(N):
        if 3 in maze[y]:
            return [maze[y].index(3), y]
    return 'error'

def maze_runner(maze):      # 출발점으로 갈 수 있는지 확인하는 함수
    stack = [find_start_pos(N)]
    check_list = []
    while len(stack):
        x, y = stack.pop()
        for move in movement:                           # 좌 우 상 하 움직임에 대해서
            nextX, nextY = x + move[0], y + move[1]     # 다음 위치 nextX, nextY가
            if -1 < nextX < N and -1 < nextY < N:       # 미로 내부이고
                if maze[nextY][nextX] == 2:             # 출발점 2면 도착이므로 1
                    return 1
                                                        # 다음 위치가 미로의 벽이 아니고(길이고) 체크한 곳이 아니라면 스택
                if not maze[nextY][nextX] and not [nextX, nextY] in check_list:
                    stack.append([nextX, nextY])
        if not [x, y] in check_list:                    # 체크한 곳이 아니라면 체크
            check_list.append([x, y])
    return 0        # 다 도는 동안 1 안 나오면 도착 못 한 거

movement = [[-1, 0], [1, 0], [0, -1], [0, 1]]
testcase = int(input())
for i in range(testcase):
    N = int(input())
    maze = [list(map(int, input()))[:N] for j in range(N)]
    print('#{} {}' .format(i+1, maze_runner(maze)))