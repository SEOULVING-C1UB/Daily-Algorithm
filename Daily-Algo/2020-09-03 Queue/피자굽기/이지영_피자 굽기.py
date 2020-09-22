
T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    # 우선 치즈 양이 들어옴
    inputCheese = list(map(int, input().split()))
    pizza = []

    # 인덱스랑 치즈양이 같이 pizza라는 배열에 저장되도록 함
    for idx, cheese in enumerate(inputCheese):
        pizza.append((idx+1, cheese))
    # print(pizza)

    # 오븐에 들어갈 피자와 남는 피자는 N을 기준으로 분배한다
    oven = pizza[:N]
    leftPizza = pizza[N:]

    # 오븐에 한개만 남을 때까지
    while len(oven) > 1:

        # 오븐의 첫번째 피자를 꺼내서 치즈를 반토막을 낸다
        idx, cheese = oven.pop(0)
        cheese = cheese//2

        # 만약 치즈가 아직 남아있으면 다시 오븐에 피자를 집어넣고
        if cheese:
            oven.append((idx, cheese))

        # 치즈가 없어지면? 오븐에 안 넣은 피자를 넣는다
        else:
            if leftPizza:
                oven.append(leftPizza.pop(0))

    print('#{} {}'.format(tc, oven.pop(0)[0]))

