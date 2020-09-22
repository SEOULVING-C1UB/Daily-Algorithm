for t in range(1, 11):
    answer = 0

    width = int(input())
    table = [list(map(int, input().split())) for _ in range(width)]

    # 열 순회
    for c in range(width):
        # 1 또는 2가 나오면 저장
        flag = 0
        # 행 순회
        for r in range(width):
            # 2가 나왔을 때
            if table[r][c] == 2:
                # 1이 나온 상태라면
                if flag == 1:
                    # 답에 1 추가
                    answer += 1
                # 2가 나왔으니 flag 2로 변경
                flag = 2
            # 1이 나왔을 때
            elif table[r][c] == 1:
                # 1이 나왔으니 flag 1로 변경
                flag = 1

    print('#{} {}'.format(t, answer))