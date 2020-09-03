import sys
sys.stdin = open("(4881)배열 최소 합_input.txt")


def findmin(k, n, cursum):
    # mini를 변경하기 위해 global로 가져오고
    global mini
    # 모든 열에 대해 다 고르면
    if k == n:
        # 최소값 갱신
        if cursum < mini:
            mini = cursum
    # 아직 다 고르지 않았다면
    else:
        # 현재까지의 합이 현재 최소값보다 작을 경우에만 (가지치기)
        if cursum < mini:
            # 조합 생성
            for i in range(k, n):
                idx[k], idx[i] = idx[i], idx[k]
                findmin(k + 1, n, cursum + mat[k][idx[k]])
                idx[i], idx[k] = idx[k], idx[i]


T = int(input())
for t in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    # 각 행에서 최대값을 골라 더한 것을 댭을 담을 mini에 넣어준다
    mini = 0
    for i in range(N):
        mini += max(mat[i])
    # 각 행에서 몇번째 idx를 고를지 저장하는 배열
    idx = list(range(N))
    findmin(0, N, 0)
    print('#{} {}'.format(t + 1, mini))
