import sys
sys.stdin = open("장훈이의높은선반.txt")

T = int(input())

for t in range(1, T+1):
    # 데이터 입력
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    n = len(heights)  # n : 원소의 개수

    ans = []
    value = 9999999999
    # 부분집합
    for i in range(1 << n):
        tmp = 0
        for j in range(n + 1):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번째 비트가 1이면 j 번째 원소 출력
                tmp += heights[j]
        # 값이 B보다 크고 차이가 value보다 작을 때
        if tmp >= B and tmp - B < value:
            value = tmp - B
        # 값이 같으면 0 저장 후 break 
        elif tmp == B:
            value = 0
            break

    print("#{} {}".format(t, value))
