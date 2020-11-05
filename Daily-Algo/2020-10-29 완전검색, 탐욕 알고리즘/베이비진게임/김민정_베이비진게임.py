import sys
sys.stdin = open("베이비진게임_input.txt")

def play(cards) :
    global winner, a, b

    while cards:        # card가 빌 때 까지 돌린다.

        #===========  a 차례 ===========
        a[(cards.pop(0))] += 1  # 무조건 a 순서가 먼저니까 a부터 뽑은 카드 배열에 넣음
        if 3 in a:              # 만약에 카드 3장 쌓인게 있으면 게임 끝
            winner = 1
            return

        for i in range(0, 8):   # 연속된 값이 있는지 체크
            if a[i] != 0 and a[i + 1] != 0 and a[i + 2] != 0:
                winner = 1
                return

        #===========  b 차례 ===========
        b[(cards.pop(0))] += 1 # a 와 마찬가지로 진행한다.
        if 3 in b:
            winner = 2
            return

        for i in range(0, 8):
            if b[i] != 0 and b[i + 1] != 0 and b[i + 2] != 0:
                winner = 2
                return


for tc in range(1, int(input())+1) :

    cards = list(map(int, input().split()))
    a = [0] * 10        # 0부터 9까지니까 그만큼 배열 선언
    b = [0] * 10
    a[cards.pop(0)] += 1    # 차례대로 카드를 가져가는데, 3장부터 의미있으니까
    b[cards.pop(0)] += 1    # 2장씩 나눠가진다.
    a[cards.pop(0)] += 1
    b[cards.pop(0)] += 1
    winner = 0              # 승자 결과
    play(cards)

    print("#{} {}".format(tc, winner))