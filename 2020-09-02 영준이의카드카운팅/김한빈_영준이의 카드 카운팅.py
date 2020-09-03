import sys

sys.stdin = open('영준이의 카드 카운팅.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    arr = input()
    cards = [arr[i:i+3] for i in range(0, len(arr), 3)]
    spd, hrt, dia, clv = [], [], [], []
    for card in cards:
        if card[0] == 'S':
            if int(card[1:]) not in spd:
                spd.append(int(card[1:]))
        elif card[0] == 'D':
            if int(card[1:]) not in dia:
                dia.append(int(card[1:]))
        elif card[0] == 'H':
            if int(card[1:]) not in hrt:
                hrt.append(int(card[1:]))
        elif card[0] == 'C':
            if int(card[1:]) not in clv:
                clv.append(int(card[1:]))
    if len(cards) != len(spd + dia + hrt + clv):
        print('ERROR', end="")
    else:
        for deck in [spd, dia, hrt, clv]:
            print(13 - len(deck), end=" ")
    print()