def check_triplet(check_list):
    checked = []
    for card in check_list:                 # check할 list에 담긴 card들을 순서대로
        if card not in checked:             # 확인하지 않은 경우에만
            checked.append(card)            # 확인했다고 치고
            if check_list.count(card) > 2:  # 해당 card의 개수가 3개 이상이면
                return 1                    # triplet이므로 1을 리턴한다.
    return 0


def check_run(check_list):                  
    for card in check_list:                                     # check할 list에 담긴 카드들을 하나씩 꺼내서
        if card - 1 in check_list and card + 1 in check_list:   # 숫자가 연속되게 된다면
            return 1                                            # run이므로 1을 리턴한다.
    return 0


for TC in range(int(input())):
    cards = list(map(int, input().split()))
    first = []  # 첫 번째 사람
    second = [] # 두 번째 사람
    flag = 1    # 무승부인지 판별하는 flag
    for i in range(len(cards)):
        if i % 2:
            second.append(cards[i])
            if len(second) > 2:
                if check_triplet(second):               # second를 check_list로 해서
                    print('#{} {}'.format(TC + 1, 2))   # triplet이라면 2번의 승리!
                    flag = 0
                    break
                if check_run(second):                   # second를 check_list로 해서
                    print('#{} {}'.format(TC + 1, 2))   # run이라면 2번의 승리!
                    flag = 0
                    break
        else:
            first.append(cards[i])
            if len(first) > 2:
                if check_triplet(first):                # first를 check_list로 해서
                    print('#{} {}'.format(TC + 1, 1))   # triplet이라면 1번의 승리!
                    flag = 0
                    break
                if check_run(first):                    # first를 check_list로 해서
                    print('#{} {}'.format(TC + 1, 1))   # run이라면 1번의 승리!
                    flag = 0
                    break
    if flag:    # flag가 살아있으면 무승부다.
        print('#{} {}'.format(TC + 1, 0))
