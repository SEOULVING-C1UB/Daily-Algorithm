import sys
sys.stdin = open("(4880)토너먼트 카드게임_input.txt")


# 이긴 학생의 인덱스 반환하는 함수 
def who(a, b):
    if (cards[a], cards[b]) in [(1, 2), (3, 1), (2, 3)]:
        return b
    else:
        return a


# 학생 중 승자가 누구인지 확인하는 함수
def winner(start, end):
    # 만약 1명을 비교하면 자기 자신 return
    if start == end:
        return start
    # 만약 2명을 비교하면 둘 중 이긴 사람 return
    elif start + 1 == end:
        return who(start, end)
    # 그 외의 경우에는
    else:
        mid = (start + end) // 2
        # 문제에서 요구한대로, 그룹을 둘로 나눠 각 그룹의 승자 중 이긴 사람 return
        return who(winner(start, mid), winner(mid + 1, end))


T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    # 학생 번호가 1~N번으로 설정되어 있어 0번 인덱스에 무의미한 값 추가
    cards.insert(0, 0)
    win = winner(1, N)
    print('#{} {}'.format(t + 1, win))
