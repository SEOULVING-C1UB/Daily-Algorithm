def maze_path():
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                result = bfs(i, j)
    return result
   

def bfs(x,y):
    # visit을 딕셔너리로 생성: 방분한 좌표가 key, 원점으로부터 거리가 value
    visit = {}
    stack = []
    stack.append((x,y))
    visit[(x,y)] = -1
    
    while stack:        
        t = stack.pop(0)        
        # 3을 만나게 되면 원점으로부터의 거리를 리턴
        if maze[t[0]][t[1]] == 3:
            return visit[t]
        # t에 인접한 좌표들을 모두 받아옴
        adjacency_t = adjacency(t)
        for w in adjacency_t:
            # w가 visit딕셔너리에 없다면 stack과 visit에 추가
            if not visit.get(w):
                stack.append(w)
                visit[w] = visit[t] + 1
    # while문을 빠져나오면 경로가 없다는 의미이므로 0을 리턴
    return 0
        

def adjacency(v):
    result = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1:
            result.append((nx, ny))
    
    return result


T = int(input())
for test_case in range(T):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    print('#' + str(test_case + 1), maze_path())
