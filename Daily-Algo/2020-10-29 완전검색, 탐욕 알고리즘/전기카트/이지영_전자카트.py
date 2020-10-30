import sys
sys.stdin = open('전자카트_input.txt')

# nPn 순열 구하기
def perm(n, k):

    if n == k:
        newTmp = tmp[:]
        totalPerm.append(newTmp)

    else:
        for i in range(n):
            if visited[i] : continue
            tmp[k] = num[i]
            visited[i] = True
            perm(n, k+1)
            visited[i] = False


def getSum(arr):

    total = 21476000000

    for i in range(len(arr)):
        currSum = batteries[0][arr[i][0]-1]
        for j in range(1, N-1):
            # print(batteries[arr[i][j-1]-1][arr[i][j]-1])
            x = arr[i][j-1]-1
            y = arr[i][j]-1
            now = batteries[x][y]
            currSum += batteries[x][y]

        # print(arr[i][len(arr)-1]-1)
        # print(batteries[arr[i][len(arr)-1]-1][0])
        currSum += batteries[arr[i][N-2]-1][0]

        if currSum < total:
            total = currSum

    return total


# T = 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    batteries = [list(map(int, input().split())) for _ in range(N)]
    # print(batteries)

    num = [i for i in range(2, N+1)]
    # print(order)

    tmp = [0]*(N-1)
    visited = [0]*(N-1)

    totalPerm = []
    perm(N-1, 0)

    # print(getSum(totalPerm))
    print('#{} {}'.format(tc, getSum(totalPerm)))

