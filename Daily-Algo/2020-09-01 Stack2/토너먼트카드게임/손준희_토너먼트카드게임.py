# 조건에 따라 계속 그룹을 나눠서(merge) 각각의 승자를 구한 다음,
# 패자는 버리고 승자만 취하는 것을(combine) 우승자 단 1명이 남을 때까지 반복한다

def merge_combine(winners):
    if len(winners) == 1:   # 1명만 입력되는 경우가 발생하면 그냥 반환
        return winners
    if len(winners) == 2:   # 결승전 // 이 밑은 가위바위보를 위한 코드
        if card_numbers[winners[0]] == card_numbers[winners[1]]:
            return [winners[0]]
        elif card_numbers[winners[0]] + card_numbers[winners[1]] == 3:
            if card_numbers[winners[0]] < card_numbers[winners[1]]:
                return [winners[1]]
            else:
                return [winners[0]]
        elif card_numbers[winners[0]] + card_numbers[winners[1]] == 4:
            if card_numbers[winners[0]] > card_numbers[winners[1]]:
                return [winners[1]]
            else:
                return [winners[0]]
        elif card_numbers[winners[0]] + card_numbers[winners[1]] == 5:
            if card_numbers[winners[0]] < card_numbers[winners[1]]:
                return [winners[1]]
            else:
                return [winners[0]]
    elif len(winners)%2:    # 결승전 아니고 홀수인원이면 조건에 따라 merge해서 승부를 내고, combine
        return merge_combine(winners[:len(winners)//2+1]) + merge_combine(winners[len(winners)//2+1:])
    else:                   # 결승전 아니고 짝수인원이면 조건에 따라 merge해서 승부를 내고, combine
        return merge_combine(winners[:len(winners)//2]) + merge_combine(winners[len(winners)//2:])


testcase = int(input())
for i in range(testcase):
    N = int(input())
    card_numbers = list(map(int, input().split()))
    winners = [x for x in range(N)]         # 학생들을 0부터 N-1까지 배치(문제에서는 1부터 N까지)
    while len(winners) > 1:                 # 1명만 남을 때까지 승부를 반복한다
        winners = merge_combine(winners)
    print('#{} {}' .format(i+1, 1+winners[0]))  # 1명만 남으면 0부터 N-1까지 배치했으므로 +1해서 출력