# T: 테스트 케이스 개수
T = int(input())

# t: 테스트 케이스 번호
for t in range(1, T + 1):
    # S: 영준이가 가지고 있는 카드 정보
    S = input()
    # cards: 무늬 별로 가지고 있는 카드 개수
    cards = dict([('S', [0] * 14), ('D', [0] * 14), ('H', [0] * 14), ('C', [0] * 14)])

    # 카드 정보 분석해서 카드 개수에 반영
    for i in range(0, len(S), 3):
        cards[S[i]][int(S[i + 1:i + 3])] += 1


    def count_card():
        # 무늬 별 총 카드 개수
        card_count = [0, 0, 0, 0]
        # index: 검사하는 무늬 인덱스
        index = 0
        for card in cards.values():
            for j in range(1, 14):
                # 겹치는 카드가 있을 경우
                if card[j] > 1:
                    return 'ERROR'
                card_count[index] += (1 - card[j])
            index += 1
        return ' '.join(list(map(str, card_count)))


    result = count_card()

    print('#{} {}'.format(t, result))
