N = int(input())
numbers = list(map(int, input().split()))
ans = 1
# longest increase, decrease sub
LIS = [1 for _ in range(9)]
LDS = [1 for _ in range(9)]

for i in range(1, N):
    if numbers[i - 1] <= numbers[i]:
        LIS[i] = LIS[i - 1] + 1
    if numbers[i - 1] >= numbers[i]:
        LDS[i] = LDS[i - 1] + 1
    ans = max(LDS[i], LIS[i], ans)

print(ans)