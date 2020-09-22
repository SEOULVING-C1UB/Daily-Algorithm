import sys
sys.stdin = open('subtree.txt')


def order(node):
    global cnt # cnt가 값이기 때문에 global 사용?
    if node != 0:
        cnt += 1
        order(board[node][0])
        order(board[node][1])

T = int(input())

for tc in range(1,1+T):
    e,n = map(int,input().split())
    tree = list(map(int,input().split())) # 연결고리 받아오기
    board = [[0]*2 for _ in range(e+2)] # tree 값을 입력해서 node의 좌,우 값이 존재하는지 확인하기 위한 board(0을 찾기 위함)
    cnt = 0 # 노드가 몇 개인지 확인하기 위한 cnt

    for i in range(e):
        if board[tree[2*i]][0] == 0: # board 값이 0 이면
            board[tree[2*i]][0] = tree[2*i+1] # 해당 위치에 값 입력(왼쪽 값)
        else:
            board[tree[2 * i]][1] = tree[2 * i + 1] # 이미 차 있으면 값 입력(오른쪽 값)

    order(n) # 루트가 n인 트리의 노드 갯수를 확인하기 위해 n 값 에서 출발
    print('#{} {}'.format(tc,cnt))
    