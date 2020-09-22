import sys

sys.stdin = open('Magnetic.txt', 'r')

for t in range(1, 11):
    print(f'#{t}', end="\n")
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    check = 1
    while check == 1:
        check = 0

        for r in reversed(range(len(arr))):
            for c in range(len(arr[0])):
                if arr[r][c] == 1:
                    if r + 1 == N:
                        arr[r][c] = 0
                        check = 1
                    elif arr[r + 1][c] == 0:
                        arr[r + 1][c] = 1
                        arr[r][c] = 0
                        check = 1
        for r in range(len(arr)):
            for c in range(len(arr[0])):
                if arr[r][c] == 2:
                    if r - 1 == -1:
                        arr[r][c] = 0
                        check = 1
                    elif arr[r - 1][c] == 0:
                        arr[r - 1][c] = 2
                        arr[r][c] = 0
                        check = 1
    results = []
    for c in range(len(arr[0])):
        col = []
        count = 0
        for r in range(len(arr)):
            col.append(arr[r][c])
        for i in range(len(col) - 1):
            if col[i] == 1 and col[i + 1] == 2:
                col[i], col[i + 1] = 0, 0
                count += 1
        results.append(count)
    print(sum(results))


'''
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''