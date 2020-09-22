T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()

    result = sum(H)

    # height: 현재 높이, k: 현재 점원 인덱스
    def min_height(height, k):
        global result

        # 현재 높이가 이미 B보다 클 경우 가지치기
        if height >= B:
            result = min(result, height)
            return

        if k >= N:
            return

        # 현재 점원 포함하고 다음 인덱스로
        min_height(height + H[k], k + 1)
        # 현재 점원 포함하지 않고 다음 인덱스로
        min_height(height, k + 1)

    min_height(0, 0)

    print('#{} {}'.format(t, result - B))
