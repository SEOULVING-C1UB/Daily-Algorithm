'''
1부터 찾아서 2, 3, 4, 5 이렇게 순차적으로 증가하기

'''
import sys
sys.stdin = open('최소합_input.txt')
# 방향 오른쪽, 아래만 가능
dx = [0, 1]
dy = [1, 0]
def findMin(x, y):

    down = right = 2147000000

    if x==N-1 and y==N-1:
        return board[x][y]

    else:
        # if x can still go down
        if x < N-1:
            down = findMin(x+1, y)
        # if y can still go right
        if y < N-1:
            right = findMin(x, y+1)

    if down < right:
        return down + board[x][y]
    else:
        return right + board[x][y]


# T = 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(board)

    print('#{} {}'.format(tc, findMin(0,0)))



