import sys

sys.stdin = open('배열 최소 합.txt', 'r')

def permutation(numbers):
    visited = [0] * len(numbers)
    i = 0
    min_result = 9 * N
    while i < len(numbers):
        if visited[i] < i:
            if i % 2 == 0:
                numbers[0], numbers[i] = numbers[i], numbers[0]
            else:
                numbers[visited[i]], numbers[i] = numbers[i], numbers[visited[i]]
            result = 0
            for r, c in enumerate(numbers[:]):
                result += arr[r][c]
            if result < min_result:
                min_result = result

            visited[i] += 1
            i = 0
        else:
            visited[i] = 0
            i += 1
    return min_result

T = int(input())
for t in range(1, T + 1):
    print(f"#{t}", end=" ")
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    column_numbers = [c for c in range(N)]
    results = []
    min_result = 9 * N

    print((permutation(column_numbers)))
