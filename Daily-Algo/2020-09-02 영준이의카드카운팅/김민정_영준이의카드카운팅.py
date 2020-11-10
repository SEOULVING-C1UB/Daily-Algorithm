tc = int(input())

for t in range(tc) :
    cards_dict = {'S':0, 'D':0, 'H':0, 'C':0}
    result = []
    deq = input()
    already = []

    for i in range(0, len(deq), 3) :
        card = deq[i]
        cardy = deq[i:i+3]
        if cardy in already :
            already.append(-1)
            break;
        else :
            cards_dict[card] += 1
            already.append(cardy)

    if already[-1] == -1 :
        print("#{} ERROR".format(t+1))
    else :
        for j in cards_dict.values() :
            result.append(13-j)
        print("#{} {}".format(t+1, " ".join(map(str,result))))