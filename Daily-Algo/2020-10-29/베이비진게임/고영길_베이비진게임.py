# make sure that card with the number greater than 3 is in deck
def is_run(deck):
    return bool(list(filter(lambda x: x >= 3, deck)))


# make sure consecutive three numbers cards in deck
def is_triplet(deck):
    for i in range(8):
        if all(deck[i:i + 3]):
            return True
    return False


for tc in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    # c1, c2 : ck[i] means the number of cards 'i' that 'k' has received so far
    c1 = [0 for _ in range(10)]
    c2 = [0 for _ in range(10)]
    answer = 0
    for i in range(6):
        c1[cards[2 * i]] += 1
        c2[cards[2 * i + 1]] += 1
        if i < 2:   # check when the number of cards in deck is bigger than 3
            continue

        if is_run(c1) or is_triplet(c1):
            answer = 1
            break
        if is_run(c2) or is_triplet(c2):
            answer = 2
            break
    print('#{} {}'.format(tc, answer))
