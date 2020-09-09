for t in range(1,11):
    N = int(input())
    magnetic = [list(map(int,input().split()))for _ in range(N)]

    # 사실 예외 처리를 저렇게 까지 할 필요가 없습니다.
    # 그냥 모든 경우의 수인 것 같습니다.

    # 정답을 위해 블록이 마주칠 때 마다 cnt를 샙니다.
    cnt = 0
    for r in range(N):
        # 어떤 자석의 성질인 지 첫 출발을 통해 구분해주기 위해 0,1을 사용합니다.
        first = 0
        # status를 통해 연속적으로 만난 것인지, 최초로 만난 것인지 구분해줍니다.
        status = 0
        for c in range(N):
            if first == 0 and magnetic[c][r] == 2:
                first = 0
            elif first == 0 and magnetic[c][r] == 1:
                first = 1
                status = 1
            elif status == 0 and magnetic[c][r] == 1:
                status = 1
            elif status == 1 and magnetic[c][r] == 1:
                status = 1
            elif status == 1 and magnetic[c][r] == 2:
                status = 0
                cnt += 1

    print('#{} {}'.format(t,cnt))