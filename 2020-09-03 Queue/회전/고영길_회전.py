# Using ignition equation is more efficient

T = int(input())
for tc in range(1, T + 1):
    N, R = map(int, input().split())
    numbers = input().split()
    print(f'#{tc} {numbers[R % len(numbers)]}')
