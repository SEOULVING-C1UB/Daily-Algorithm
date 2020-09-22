import sys
sys.stdin = open('토너먼트 카드게임_input.txt')

def win(x, y):
    # 1 가위 2 바위 3 보
    if (students[x-1] == 1 and students[y-1] == 3) or (students[x-1] == 1 and students[y-1] == 1):
        return x
    elif (students[x-1] == 2 and students[y-1] == 1) or (students[x-1] == 2 and students[y-1] == 2):
        return x
    elif (students[x-1] == 3 and students[y-1] == 2) or (students[x-1] == 3 and students[y-1] == 3):
        return x
    return y

def divide(left, right):
    if left == right:
        return left
    left_winner = divide(left, (left+right)//2)
    right_winner = divide((left+right)//2+1, right)
    winner = win(left_winner, right_winner)
    return winner

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    students = list(map(int, input().split()))
    left = 1
    right = n

    # 학생들을 먼저 나눈다
    answer = divide(left, right)

    print("#{0} {1}".format(test_case, answer))