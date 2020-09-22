import sys
sys.stdin = open("토너먼트_input.txt")

def group(players):
    j = len(players)

    if j == 1:
        # print(players[0])
        return players[0]

    elif j==2:
        return rockPaperScissors(players[0], players[1])

    else:
        # 모든 경우에서 첫번째 그룹이 적게 떨어지기 위해서 필요
        j = (len(players)-1)//2 + 1
        group1 = players[:j]
        group2 = players[j:]

        # print(group1, group2)

        return rockPaperScissors(group(group1), group(group2))



def rockPaperScissors(player1, player2):
    p1 = player1[1]
    p2 = player2[1]

    # player1이 이기는 경우
    if (p1, p2) in [(1,3), (2,1), (3,2)]:
        return player1

    # player 2
    elif (p2, p1) in [(1,3), (2,1), (3,2)]:
        return player2

    # 비길때
    else:
        if player1[0] < player2[0]:
            return player1
        else:
            return player2

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    cards = list(map(int, input().split()))
    players = [(i,cards[i-1]) for i in range(1, N+1)]

    winner = group(players)

    print('#{} {}'.format(tc, winner[0]))