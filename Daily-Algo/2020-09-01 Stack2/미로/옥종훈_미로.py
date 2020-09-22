import sys

sys.stdin = open("D2_4875_input.txt", "r")


# 지도를 하나씩 순회하면서 2가(출발점) 나타나면 DFS 시작
def maze_path():    
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                result = DFS([j, i])
    return 1 if result else 0


# 모든 점에 대해 DFS를 다 돌면 시간 초과가 뜸
# 따라서 3을 만나는 순간 리턴하여 종료되도록 함
# DFS를 다 돌 때까지 3을 만나지 못하면 False를 리턴
def DFS(v):
    visit = []
    stack = []
    stack.append(v)
    while stack:
        w = stack.pop()
        if maze[w[1]][w[0]] == 3:
            return True
        if w not in visit:
            visit.append(w)            
            stack.extend(adjacency(w))
    return False


# 인접행렬을 리턴해주는 함수
def adjacency(v):
    result = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    new_x = v[0]
    new_y = v[1]
    for i in range(4):
        new_x += dx[i]
        new_y += dy[i]
        if 0 <= new_x < n and 0 <= new_y < n and maze[new_y][new_x] != 1:
            result.append([new_x, new_y])
        new_x = v[0]
        new_y = v[1]
    return result


t = int(input())
for test in range(t):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    print('#'+str(test+1), maze_path())