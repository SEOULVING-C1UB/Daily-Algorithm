import sys

sys.stdin = open("D2_4880_input.txt", "r")


# 재귀를 이용하여 구현
# players는 리스트로, 가위바위보 값과 인덱스 값 두 가지를 가지는 원소 player들로 구성됨
def tournament(players):
    if len(players) == 1:
        return players[0]
    elif len(players) == 2:
        return win(players[0], players[1])
    else:        
        # 아래 수식이 핵심
        # 짝수일 경우 정확히 반씩 쪼개고, 홀수일 경우 앞 그룹이 뒷 그룹보다 한 명 많게끔 함
        len1 = (len(players)+1)//2
        return win(tournament(players[:len1]), tournament(players[len1:]))


def win(player1, player2):
    # 비겼을 경우 인덱스 값이 적은 플레이어를 리턴(승자)
    if player1[0] == player2[0]:
        if player1[1] < player2[1]:
            return player1
        else:
            return player2
    # 플레이어 1이 이겼을 경우
    elif (player1[0], player2[0]) in [(1, 3), (2, 1), (3, 2)]:
        return player1
    # 플레이어 2가 이겼을 경우
    else:
        return player2

t = int(input())
for test in range(t):
    n = int(input())
    card = list(map(int, input().split()))
    # 카드의 값(가위,바위보)만으로는 게임 진행이 되지 않으므로 인덱스 값을 함께 저장하는 리스트 player 생성
    players = [[card[i], i+1] for i in range(n)]
    print('#'+str(test+1), tournament(players)[1])