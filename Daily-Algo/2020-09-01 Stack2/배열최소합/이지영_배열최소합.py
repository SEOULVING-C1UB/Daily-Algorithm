
# T = int(input())
'''
3
2 1 2
5 8 5
7 2 2
'''
def minSum(idx, currentSum):
    global mini

    # 만약 배열 최대 idx면 그때의 합을 리턴
    if idx == N:
        if currentSum < mini:
            mini = currentSum
        return

    # 만약 지금 있는 합이 그 전에 있던 최소값보다 크다? 그럼 그 그룹은 볼 필요도 없음
    if currentSum > mini:
        return

    # 탐색을 시작하자
    for i in range(N):
        if not visited[i]:  #이 칸을 방문한적이 없으면
            visited[i] = True   #방문했다고 바꿔주고

            # 재귀로 다시 호출
            # 그 다음줄로 넘어감, 합에는 지금 위치에 있는 값 가져감
            minSum(idx+1, currentSum+arr[idx][i])
            visited[i] = False

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mini = 2147000000

    visited = [False for _ in range(N)]

    minSum(0, 0)    #0, 0에서 시작

    print('#{} {}'.format(tc, mini))