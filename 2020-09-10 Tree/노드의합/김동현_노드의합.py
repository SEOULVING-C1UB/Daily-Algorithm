import sys
sys.stdin = open('노드의합.txt')


def binary(node):
    if node != 0:
        binary(board[node][0]) # 왼쪽
        box_sum[node//2] += box_sum[node] # box_sum[node//2](부모노드)에 자식 노드 더하기
        binary(board[node][1]) # 오른쪽

T = int(input())

for tc in range(1,1+T):
    n,m,l = map(int,input().split())
    box_sum = [0] * (n+1) # 노드의 값을 입력하기 위한 0*(n+1) 리스트
    tree = [list(map(int,input().split())) for _ in range(m)]
    for q in range(m):
        box_sum[tree[q][0]] = tree[q][1] # 리프 노드 채워넣기

    board = [[0]*2 for _ in range(n+1)] # 좌우 확인용

    for i in range(2,n+1): # 좌우 채워넣기
        if board[i//2][0] == 0:
            board[i//2][0] = i
            if i//2+1 <= n:
                board[i // 2][1] = i+1
    binary(1)
    print(box_sum[2])