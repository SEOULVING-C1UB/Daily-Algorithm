T = int(input())

for tc in range(1, T + 1):
    # deck : (dict) store which cards having pattern are given
    deck = {'S': [], 'D': [], 'H': [], 'C': []}
    info = input()
    ans = ''
    # Consider which cards were given and check duplicated cards
    for i in range(0, len(info), 3):
        tmp = [info[i], info[i + 1:i + 3]]
        if tmp[1] in deck[tmp[0]]:
            ans = 'ERROR'
            break
        else:
            deck[tmp[0]].append(tmp[1])
    # If ans is not 'error', count number of cards that need to make complete cards set
    if ans:
        print(f'#{tc} {ans}')
    else:
        for mark in deck:
            ans += f'{13-len(deck[mark])} '
        print(f'#{tc} {ans}')
