import sys
sys.stdin = open('격자판.txt')


def dfs(i,j,k):
    if len(str(k)) == 7:
        save.append(k)
        return
    for q in range(4):
        if 0 <= i+x[q] < 4 and 0 <= j+y[q] < 4:
            ni = i+x[q]
            nj = j+y[q]
            dfs(ni,nj,str(k)+str(board[ni][nj]))


T = int(input())

x = [-1,1,0,0]
y = [0,0,-1,1]

for tc in range(1,1+T):
    board = [list(map(int,input().split())) for _ in range(4)]
    save = []


    for i in range(4):
        for j in range(4):
            dfs(i,j,board[i][j])

    print('#{} {}'.format(tc, len(set(save))))
