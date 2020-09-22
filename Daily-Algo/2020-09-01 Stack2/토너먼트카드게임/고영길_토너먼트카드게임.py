import sys

sys.stdin = open('토너먼트 카드게임_input.txt', 'r')


def who_win(a, b):
    """
    Because in case of draw winner is a,
    consider the case winner is b.
    :return: winner of a,b
    """
    if [a[0], b[0]] in [[1, 2], [2, 3], [3, 1]]:
        return b
    else:
        return a


def solve(students):
    """
    Recursive function to divide students into group
    or return the winning student
    :param students: (list) store what each student choice RSP
    :return:
    """
    if len(students) == 1:
        return students[0]
    elif len(students) == 2:
        return who_win(students[0], students[1])
    else:
        l = (1 + len(students)) // 2
        return who_win(solve(students[:l]), solve(students[l:]))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tmp = list(map(int, input().split()))
    # cards : (list) store [card, index]
    cards = [[tmp[i], i] for i in range(N)]
    ans = solve(cards)[1] + 1
    print(f'#{tc} {ans}')
