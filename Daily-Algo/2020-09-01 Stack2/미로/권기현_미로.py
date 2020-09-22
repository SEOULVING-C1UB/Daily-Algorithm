import sys
sys.stdin = open("5105.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def maze_runner(x, y):

    queue.append([x,y])
    while queue:
        maze_TF[y][x] = True
        x, y = queue.pop(0)
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if new_x>=0 and new_x < N and new_y >=0 and new_y <N and not maze_TF[new_y][new_x]:
                if maze[new_y][new_x] == 3:
                    return distance[y][x]

                elif maze[new_y][new_x] == 0:
                    queue.append([new_x, new_y])
                    distance[new_y][new_x] = distance[y][x]+1
    return 0





total_tc = int(input())

for tc in range(1, total_tc+1):
    queue = []
    N = int(input())
    maze = [[int(x) for x in str(input())] for _ in range (N)]
    maze_TF = [[False for _ in range (N)] for _ in range (N)]
    distance = [[0 for _ in range (N)] for _ in range (N)]
    for i in range(N):
        for j in range(N):
            if maze[j][i]==2:
                starting_x, starting_y = i, j

    result = maze_runner(starting_x, starting_y)
    print("#%d %d"%(tc,result))