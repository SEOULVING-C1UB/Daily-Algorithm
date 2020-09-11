import sys
sys.stdin = open('이진탐색.txt')


def binary(node):
    if node != 0:
        binary(board[node][0]) # 왼쪽
        tree_num[node] = number.pop(0) # tree_num의 node의 위치에 있는 값을 number의 가장 앞에서 뽑아옴(1부터) /// 왼 < 현재 노드 < 오 순서로 값이 커야하기 때문에 왼쪽부터 채워줌 
        binary(board[node][1]) # 오른쪽

T = int(input())

for tc in range(1,1+T):
    n = int(input())
    board = [[0]*2 for _ in range(n+1)] # node의 좌,우 값이 존재하는지 확인하기 위한 board(0을 찾기 위함)
    number = []
    for j in range(1,n+1): # tree_num에 집어 넣을 list(1~n) 만들기
        number += [j]

    tree_num = [0]*(n+1) # node에 입력된 값을 넣기 위한 list

    for i in range(2,n+1): # board에 좌 우 값 입력
        if board[i//2][0] == 0:
            board[i//2][0] = i
            if i+1 <= n:
                board[i // 2][1] = i+1
    binary(1) # 루트에서 시작
    print('#{} {} {}'.format(tc,tree_num[1],tree_num[n//2]))