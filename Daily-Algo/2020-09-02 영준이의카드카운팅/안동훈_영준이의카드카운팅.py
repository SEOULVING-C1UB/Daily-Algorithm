T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    S, D, H, C = [0]*14, [0]*14, [0]*14, [0]*14
    cards= input()
    for i in range(0, len(cards), 3):
        if cards[i] == 'S':
            number = int(cards[i+1])*10 + int(cards[i+2])
            S[number] += 1
        elif cards[i] == 'D':
            number = int(cards[i+1])*10 + int(cards[i+2])
            D[number] += 1
        elif cards[i] == 'H':
            number = int(cards[i+1])*10 + int(cards[i+2])
            H[number] += 1
        elif cards[i] == 'C':
            number = int(cards[i+1])*10 + int(cards[i+2])
            C[number] += 1

    answer_S, answer_D, answer_H, answer_C, = 13, 13, 13, 13
    # 만약 배열의 요소가 2가 넘으면 바로 에러처리
    
    for i in range(1, 14):
        if S[i] >= 2 or D[i] >= 2 or H[i] >= 2 or C[i] >= 2:
            answer = 'ERROR'
            break

    # 배열에 요소가 1이면 각각의 answer 값 빼주기
    for i in range(1, 14):
        if S[i] == 1:
            answer_S -= 1
    for i in range(1, 14):
        if D[i] == 1:
            answer_D -= 1
    for i in range(1, 14):
        if H[i] == 1:
            answer_H -= 1
    for i in range(1, 14):
        if C[i] == 1:
            answer_C -= 1
    
    if answer == 0:
        print('#{0} {1} {2} {3} {4}'.format(test_case, answer_S, answer_D, answer_H, answer_C))
    else:
        print('#{0} {1}' .format(test_case, answer))
