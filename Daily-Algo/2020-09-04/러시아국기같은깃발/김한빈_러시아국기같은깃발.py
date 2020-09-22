import sys

sys.stdin = open('러시아 국기 같은 깃발.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 위부터 차례로 W, B, R 색으로 칠해지는 경우의 수 구하기
    patterns = []
    for i in range(1, N + 1): # W로 색칠
        for j in range(N + 1 - i): # B로 색칠
            for k in range(N + 1 - i - j): # R로 색칠
                if (i != 0 and j != 0 and k != 0) and (i + j + k == N): # 최소 한 줄 씩은 칠애햐 하기 때문에 0 제거. 모든 행이 칠해져야 하므로 합이 N과 동일
                    patterns.append([i, j, k])

    counts = []
    # 각 경우의 수 별 새로 칠하는 칸 수 세기
    for p in patterns:
        count = 0 # ex) p = [2, 1, 3]
        for r in range(0, p[0]): # range(0, 2) -> r = 0, 1
            for c in range(len(arr[0])):
                if arr[r][c] != 'W': # W로 새로 칠해야 하는 칸 count
                    count += 1
        for r in range(p[0], p[0] + p[1]): # range(2, 3) -> r = 2
            for c in range(len(arr[0])):
                if arr[r][c] != 'B': # B로 새로 칠해야 하는 칸 count
                    count += 1
        for r in range(p[0] + p[1], p[0] + p[1] + p[2]): # range(3, 6) -> r = 3, 4, 5, 6
            for c in range(len(arr[0])):
                if arr[r][c] != 'R': # R로 새로 칠해야 하는 칸 count
                    count += 1
        counts.append(count) # counts에 저장
    print(min(counts)) # 최솟값 프린트

