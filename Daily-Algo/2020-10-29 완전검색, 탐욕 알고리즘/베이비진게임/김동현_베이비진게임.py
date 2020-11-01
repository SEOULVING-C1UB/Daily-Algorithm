import sys
sys.stdin = open('베이비진게임.txt')


T = int(input())

for tc in range(1, 1 + T):
    card_lst = list(map(int, input().split()))

    player_one = []
    player_two = []
    res = 0
    q = 0

    while q < 6:
        if res != 0: # 결과가 나왔으면 끝내기
            break

        player_one += [card_lst[2 * q]]
        player_two += [card_lst[2 * q + 1]]

        if q >= 2: # 3장 이상 모였을 때부터 확인하기
            player_one = sorted(player_one)
            for i in range(len(player_one) - 2):
                if (player_one[i]+1 in player_one and player_one[i]+2 in player_one) or player_one[i] == player_one[i+1] == player_one[i+2]:
                    if res == 0:
                        res = 1
            player_two = sorted(player_two)
            for j in range(len(player_two) - 2):
                if (player_two[j]+1 in player_two and player_two[j]+2 in player_two) or player_two[j] == player_two[j+1] == player_two[j+2]:
                    if res == 0:
                        res = 2
        q += 1

    print('#{} {}'.format(tc, res))