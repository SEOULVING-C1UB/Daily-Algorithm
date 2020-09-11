import sys
sys.stdin = open('이진힙.txt')


def asd(node):
    if node != 0:
        if node//2 >= 1:
            if index[node] < index[node//2]: # 부모 노드 > 자식 노드일 경우
                index[node] , index[node//2] = index[node//2] , index[node] # swap
        asd(board[node][0])
        asd(board[node][1])

T = int(input())

for tc in range(1,1+T):
    n = int(input())
    index = [0] + list(map(int,input().split()))
    board = [[0]*2 for _ in range(len(index)+1)] # 좌우 확인용 board(0찾기 위함)
    for i in range(2,len(index)+1): # board에 좌우 인식할 수 있도록 만들기
        if board[i//2][0] == 0:
            board[i//2][0] = i
            if i+1 <= n:
                board[i//2][1] = i+1

    asd(1)
    cnt = 0
    while n != 1: # a라는 노드의 부모 노드는 a//2임, 1이면 그만 둬야 함 최상위 루트의 node의 인덱스?? 값을 1로 줬기 때문에
        cnt += index[n//2]
        n = n//2

    print('#{} {}'.format(tc,cnt)) # 런타임 오류... ㅠㅠ