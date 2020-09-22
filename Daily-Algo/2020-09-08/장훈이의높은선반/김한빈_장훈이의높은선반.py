import sys

def combination(arr, n): # 조합
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for a in arr:
            result.append([a])
    elif n > 1:
        for a in range(len(arr) - n + 1):
            for temp in combination(arr[a + 1:], n - 1):
                result.append([arr[a]] + temp)
    return result

sys.stdin = open('장훈이의 높은 선반.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    heights = list(reversed(sorted(heights))) # 정렬
    
    s = 0   # 가장 큰 수 몇개를 사용해야 B를 넘는 지 확인하고 s에 저장. 즉 s보다 작은 조합 개수는 고려할 필요 없음
    for i in range(N):
        if sum(heights[:i + 1]) >= B:
            s = i + 1
            break

    result = []
    for i in range(s, N + 1): # 최소 조합 개수 s부터 조합 확인
        for comb in combination(heights, i):
            a = sum(comb)
            if a >= B:
                result.append(a)
    print(min(result) - B) # 가장 작은 것과 B의 차이 출력


