import sys
sys.stdin = open('러시아국기.txt')

T = int(input())

for tc in range(1,1+T):
    n,m = map(int,input().split())
    select = [] # 각자 몇 개 필요한지 확인하기 위한 틀
    min_cnt = m*n # 결과값
    board = [list(str(input())) for _ in range(n)] # 자료 받아오기
    for q in range(1, n - 1): # 필요한 갯수 저장
        a = m - board[q].count('W')
        b = m - board[q].count('B')
        c = m - board[q].count('R')
        select += [[a, b, c]]
    # select는 n-2개임

# 가장 윗줄은 무조건 하얀색, 마지막 줄은 빨강으로 칠해야 함, 그래서 그 두 줄 제외함
    for i in range(n-2): # white
        for j in range(1,n-1): # blue # 반드시 한 줄이상 들어가야 함
            cnt = 0
            if i+j >= n-1: # n-2 넘기지 않기 위해
                continue
            for z in range(i):
                cnt += select[z][0]
            for x in range(i,i+j):
                cnt += select[x][1]
            for c in range(i+j,n-2):
                cnt += select[c][2]
            if min_cnt >= cnt:
                min_cnt = cnt

    min_cnt += m - board[0].count('W')
    min_cnt += m - board[len(board)-1].count('R') # 첫 줄과 마지막 줄에서 필요한 갯수 더해주기
    print('#{} {}'.format(tc, min_cnt))