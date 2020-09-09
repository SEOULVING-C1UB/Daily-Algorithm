import sys
sys.stdin = open('격자판.txt')


def dfs(i,j,k):
    if len(str(k)) == 7: # str(k)의 값이 7일 때(=6번 움직였을 때)
        save.append(k) # save에 k의 값을 저장
        return
    for q in range(4):
        if 0 <= i+x[q] < 4 and 0 <= j+y[q] < 4: # 범위 제한
            ni = i+x[q]
            nj = j+y[q]
            dfs(ni,nj,str(k)+str(board[ni][nj])) # str을 안하면 int값이 더해짐(len으로 확인 불가능, 이동 횟수 확인 어려움)


T = int(input())

x = [-1,1,0,0]
y = [0,0,-1,1]

for tc in range(1,1+T):
    board = [list(map(int,input().split())) for _ in range(4)]
    save = [] # 저장 공간


    for i in range(4):
        for j in range(4):
            dfs(i,j,board[i][j]) # i,j 모든 값을 dfs로 보내기

    print('#{} {}'.format(tc, len(set(save))))