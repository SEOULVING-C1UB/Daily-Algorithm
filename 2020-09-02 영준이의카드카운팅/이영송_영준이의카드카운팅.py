'''
기본 컨셉
1) 딕셔너리 구조를 두 개의 리스트로 구현했습니다
    1-1) 카드 무늬의 이름이 담긴 리스트를 만들고,
    1-2) 순서를 보존하여 각 카드 무늬의 숫자를 저장할 리스트를 다차원으로 선언했습니다.
2) 주어진 입력 값을 읽으며 리스트에 append합니다.
    2-1) append하기 전 containment 검사를 하여 중복된 값이 있는지 체크합니다.
    2-2) 있다면 중복 check 여부를 반영하고 바로 break를 걸어줍니다.
3) 모든 append를 마친 후 각 카드 별로 원소의 개수를 len를 통해 구합니다.
'''

T = int(input())

for t in range(1,T+1):
    cards = list(input())
    # 입력 cards 의 길이는 항상 3의 배수 이므로
    N = len(cards)//3
    # cards의 무늬와 그 순서를 보존한 check 리스트 생성
    name = ['S','D','H','C']
    check = [[],[],[],[]]
    # 중복 유무를 체크할 result
    result = 0
    # 3개의 연속된 원소를 1세트로, 총 N개의 세트 동안 반복
    for i in range(N):
        p = cards[3*i]
        n1 = cards[3*i+1]
        n2 = cards[3*i+2]
        # 앞에 0이 나오는 경우와 아닌 경우를 분리하기
        if n1 == '0':
            numbers = int(n2)
        else:
            numbers = int(n1 + n2)
        # 카드 무늬 정보 p가 어떤 것인지 확인하여
        # 해당 무늬의 index를 가지고
        # check 리스트를 불러와 거기에 숫자를 대입합니다.
        for j in range(4):
            if p == name[j]:
                # 만약, 중복된 숫자가 하나라도 있다면
                # 이에 대한 여부를 1로 표시하고 break합니다.
                if numbers in check[j]:
                    result = 1
                    break
                else:
                    check[j].append(numbers)
    if result != 1:
        print('#{} {} {} {} {}'.format(t,13-len(check[0]),13-len(check[1]),13-len(check[2]),13-len(check[3])))
    else:
        print('#{} ERROR'.format(t))