import sys
sys.stdin = open('(5105)_input.txt')

T = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# BFS 탐색을 통해 경로를 방문할 떄 마다 횟수를 누적시킵니다
def BFS(s1,s2):     # 입력값으로 Row, Col을 받아 첫 번째 원소를 r, 두 번째 원소를 c로 읽어옵니다.
    result = 0
    Q = []
    Q.append(s1)
    Q.append(s2)
    visit[s1][s2] = 1
    while len(Q) != 0:  # Q가 0이 될 때까지 반복합니다.
        pr = Q.pop(0)   # 행, 열 좌표를 한 번에 받지 않고 하나씩 나눠서 받았습니다.
        pc = Q.pop(0)
        for i in range(4):  # 상하좌우, 4방위를 탐색합니다.
            nr = pr + dr[i]
            nc = pc + dc[i]
                            ## 벽에 부딪히는 지, 방문한지 여부와 함께 maze가 1이 아닌지 탐색합니다.
            if nr >= 0 and nr < N and nc >= 0 and nc < N and maze[nr][nc]!=1 and visit[nr][nc] ==0:
               if maze[nr][nc] == 3:    # maze 가 1이 아닌 경우 중 3인 경우의 수에 break를 걸어줍니다.
                   visit[nr][nc] = visit[pr][pc] - 1    # 방문 경로의 누적 회수를 계산할 때 처음을 빼주어야 하므로 -1을 했습니다.
                   result = visit[nr][nc]
                   break
               else:
                   Q.append(nr)
                   Q.append(nc)
                   visit[nr][nc] = visit[pr][pc] + 1
    return result


for t in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]

    # 출발 지점을 찾습니다.
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr = r
                sc = c
                break

    # def로 return을 받게 만들었습니다.
    print('#{} {}'.format(t,BFS(sr,sc)))
