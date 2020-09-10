import sys
sys.stdin = open('Maze_input.txt')

T = int(input())

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

for t in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input()))for _ in range(N)]
    visit = [[0]*N for _ in range(N)]

    # 시작 지점을 설정합니다.
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr = r
                sc = c
                break

    # stack 자료형을 통해 풀었습니다.
    # row,col을 리스트로 넣지 않고 첫번째, 두번째로 구분하여 넣었습니다.
    stack = []
    stack.append(sc)
    stack.append(sr)
    # True/False를 점검하는 변수입니다.
    ans = 0
    # DFS 시작
    while len(stack) != 0:
        pr = stack.pop()
        pc = stack.pop()
        # pop이후 visit 처리 하는 것으로 알고리즘을 설계해서 visit 유무를 체크합니다.
        if visit[pr][pc] ==0:
            visit[pr][pc] = 1
            stack.append(pc)
            stack.append(pr)
            for i in range(4):
                nr = pr + dr[i]
                nc = pc + dc[i]
                if nr >= 0 and nr < N and nc >=0 and nc < N and visit[nr][nc] == 0 and maze[nr][nc] != 1:
                    stack.append(nc)
                    stack.append(nr)
        # 이제와서 보니 maze의 3이 있는지 유무를 체크하는 것이 가장 먼저 올라갔어야 했는데,
        # 이 코드는 매우 비효율적이고 안정적이지 않은 코드인 것 같습니다.
        # 답이 어떻게 나왔는지 의문입니다.
        elif maze[pr][pc] == 3:
            ans = 1
            break

    print('#{} {}'.format(t,ans))