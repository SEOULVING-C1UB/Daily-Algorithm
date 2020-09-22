import sys

sys.stdin = open("피자굽기_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    res = 0
    n, m = map(int, input().split())
    # 각 피자의 치즈양과 번호를 결합
    cheese = list(map(list, zip(map(int, input().split()), range(1, m+1))))
    oven = []
    # 오븐 크기만큼 피자 넣기
    for _ in range(n):
        oven.append(cheese.pop(0))
    count = 0
    # 오븐에 남은 치즈가 녹이고, 다 녹았았고 남은 치즈가 있다면 그 자리에 치즈 추가
    # 다 녹은 치즈의 개수가 전체 치즈 개수-1 이라면 끝
    while count < m-1:
        for i in range(n):
            if oven[i][0]:
                oven[i][0] //= 2
                if oven[i][0] == 0:
                    count += 1
                    if cheese:
                        oven[i] = cheese.pop(0)
                    if count == m-1:
                        break
    # 남은 치즈의 번호를 결과 값에 추가
    for j in range(n):
        if oven[j][0]:
            res = oven[j][1]
    print('#{} {}'.format(test_case, res))