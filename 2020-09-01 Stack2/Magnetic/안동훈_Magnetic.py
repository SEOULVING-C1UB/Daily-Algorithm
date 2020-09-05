T = 10
for test_case in range(1, T + 1):
    n = int(input())
    # 테이블을 입력받습니다.
    table = [list(map(int, input().split())) for _ in range(n)]
    # check 변수는 N극과 S극이 번갈아가면서 나올 때마다 answer를 증가시키는 용도로 사용됩니다.
    # 이때, 1이 먼저 나오고 2가 나와야 의미 있습니다.
    answer = 0
    for i in range(n):
        check = 0
        for j in range(n):
            if table[j][i] == 1:
                check = 1
            elif table[j][i] == 2:
                if check == 1:
                    check = 2
                    answer += 1

    print(f'#{test_case} {answer}')