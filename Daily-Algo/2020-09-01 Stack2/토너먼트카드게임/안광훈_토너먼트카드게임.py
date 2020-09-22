T = int(input())

for t in range(1, T+1):
    N = int(input())

    cards = [0]
    cards.extend(list(map(int, input().split())))

    # 가위바위보
    # a, b는 cards의 index
    def rock_scissors_paper(a, b):
        _result = (cards[a]-cards[b]) % 3
        # a를 기준으로 질 경우 나머지가 2임
        if _result == 2:
            return b
        # 비기거나 이기면 a 리턴
        return a

    def get_winner(start, end):
        # 1인 그룹일 경우
        if start == end:
            return start

        # 2인 그룹일 경우
        if end - start == 1:
            return rock_scissors_paper(start, end)

        # 가운데 인덱스
        middle = (start + end) // 2

        # 그룹을 둘로 쪼개서 그룹의 승자를 가림
        return rock_scissors_paper(get_winner(start, middle), get_winner(middle+1, end))

    result = get_winner(1, N)
    print('#{} {}'.format(t, result))