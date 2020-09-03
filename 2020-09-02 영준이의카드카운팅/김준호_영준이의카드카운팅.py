def card_check(s):
    res = []
    # s[3*i]은 무늬, s[3*i+1:3*i+3]은 숫자 부분
    for i in range(len(s)//3):
        card[s[3*i]][int(s[3*i+1:3*i+3])] += 1
        if card[s[3*i]][int(s[3*i+1:3*i+3])] >= 2:  # 겹치는 것이 있다면 에러
            return 'ERROR'
    # 카드 딕셔너리 밸류 배열의 합들을 각각 13에서 빼서 res에 담는다.
    for v in card.values():
        res.append(str(13-sum(v)))
    # 공백을 두고 하나의 문자열로 합친다.
    return ' '.join(res)
            
T = int(input())

for test_case in range(1, T + 1):
    s = input()
    # 카드 딕셔너리 숫자 개수만큼 생성
    card = {
        'S' : [0]*14,
        'D' : [0]*14,
        'H' : [0]*14,
        'C' : [0]*14
    }
    
    print(f'#{test_case} {card_check(s)}')