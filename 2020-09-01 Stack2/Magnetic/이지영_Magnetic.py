for tc in range(1, 11):
    side = int(input())

    # 100까지 받을꺼니까 +1
    board = [[0]*(side+1) for _ in range(side+1)]

    for i in range(side):
        board[i] = (list(map(int, input().split())))

    # board = [list(map(int, input().split())) for _ in range(side)]

    cnt = 0

    for col in range(side):
        for row in range(side):

            # 위에서 시작
            if board[col][row] == 1:
                
                if board[col + 1][row] == 2:  # 다음줄에 2가 있으면 cnt 증가
                    cnt += 1

                elif board[col + 1][row] == 0:  # 0이면 그 위치로 이동
                    board[col + 1][row] = board[col][row]

    print('#{} {}'.format(tc, cnt))
