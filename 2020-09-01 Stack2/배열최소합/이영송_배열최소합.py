T = int(input())

# 배열의 합을 계산하는 함수입니다.
# 전형적인 순열 알고리즘으로 swap을 사용하였습니다.
# min_val를 global로 설정하여 가지치기 및 정답 도출에 사용합니다.
def subsetsum(n,k,currsum):
    global min_val
    if min_val < currsum: return    # min_val보다 커진 합계는 더 계산해보지 않고 그만둡니다.
    if n == k:
        if currsum < min_val:       # 모든 경우의 수를 점검하고 sum이 작다면 min_val를 sum으로 업데이트 합니다.
            min_val = currsum
    else:
        for i in range(k,n):        # swap을 하게 되면 k번째 자리를 고정시켜야 하므로 ragne를 (k,n)으로 줍니다.
            A[k], A[i] = A[i], A[k]
            subsetsum(n,k+1,currsum+array[k][A[k]]) # A[k]번째는 다음 함수 호출 시 값의 변동이 없으므로 그 값을 더해줍니다.
            A[k], A[i] = A[i], A[k]             # 제자리로 돌려 i의 반복에 따라 경우의 수를 다양하게 하도록 만들어줍니다.

for t in range(1,T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    min_val = 0xfff         # 제가 아는 큰 수에 속합니다.
    subsetsum(N,0,0)        # 함수를 호출합니다.

    print('#{} {}'.format(t,min_val))