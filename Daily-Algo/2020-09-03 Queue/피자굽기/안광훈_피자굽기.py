import sys
sys.stdin = open('피자_굽기.txt')

# T: 테스트 케이스 개수
T = int(input())

# t: 테스트 케이스 번호
for t in range(1, T + 1):
    # N: 화덕의 크기, M: 피자 개수, Ci: 피자에 뿌려진 치즈의 양
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    # oven: 화덕 리스트, cur_pizza: 남은 피자 개수
    oven = []
    cur_pizza = M

    # 화덕에 피자 넣기
    for i in range(N):
        # 앞에는 피자 번호, 뒤에는 치즈 양
        oven.append([i + 1, Ci[i]])

    # i: 현재 화덕 인덱스, j: 화덕에 넣은 피자 개수
    i = 0
    j = N

    # 피자가 1개 남을 때까지
    while cur_pizza > 1:
        # 현재 화덕 인덱스에 피자가 없을 때
        if oven[i][1] == 0:
            i = (i + 1) % N
            continue

        # 피자 치즈 양 반으로 줄이기
        oven[i][1] //= 2

        # 반으로 줄였더니 없어졌을 때
        if oven[i][1] == 0:
            cur_pizza -= 1
            # 화덕에 넣을 피자가 남아있을 때
            if j < M:
                oven[i] = [j + 1, Ci[j]]
                j += 1

        i = (i + 1) % N

    result = 0
    for pizza in oven:
        # 치즈가 남아 있는 피자 찾기
        if pizza[1]:
            result = pizza[0]

    print('#{} {}'.format(t, result))
