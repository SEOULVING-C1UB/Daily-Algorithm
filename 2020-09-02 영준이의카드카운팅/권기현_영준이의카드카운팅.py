import sys
sys.stdin = open('input.txt')

shape = ["S", "D", "H", "C"]
number = [x for x in range(1, 14)]

def card_counter(my_card, my_card_cnt):
    for i in range(0, my_card_cnt, 3):

        card_shape = my_card[i]
        card_number = str(int(my_card[i+1:i+3]))
        try :
            total_card.remove(card_shape+card_number)
        except:
            print("#%d ERROR"%(tc))
            return 1
    S = D = H = C = 0
    for card in total_card:
        if card[0]=="S":
            S += 1
        elif card[0]=="D":
            D += 1
        elif card[0]=="H":
            H += 1
        elif card[0]=="C":
            C += 1
    print("#%d %d %d %d %d"%(tc, S, D, H, C))
    return 0



total_tc = int(input())
for tc in range(1, total_tc+1):
    my_card = input()
    my_card_cnt = len(my_card)
    total_card = [s + str(n) for s in shape for n in number]
    card_counter(my_card, my_card_cnt)
