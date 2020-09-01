import sys


def split(arr):
    N = len(arr)
    if N == 1:
        return arr[0]
    else:
        arr1, arr2 = arr[:(N + 1) // 2], arr[(N + 1) // 2:]

        return checkMax(split(arr1), split(arr2))

def checkMax(a, b):
    if a[1] == 1:
        if b[1] == 1:
            return a
        elif b[1] == 2:
            return b
        elif b[1] == 3:
            return a
    elif a[1] == 2:
        if b[1] == 1:
            return a
        elif b[1] == 2:
            return a
        elif b[1] == 3:
            return b
    elif a[1] == 3:
        if b[1] == 1:
            return b
        elif b[1] == 2:
            return a
        elif b[1] == 3:
            return a

sys.stdin = open('토너먼트 카드게임.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    N = int(input())
    arr = list(map(int, input().split()))
    arr = list(enumerate(arr))

    arr = split(arr)
    print(arr[0] + 1)