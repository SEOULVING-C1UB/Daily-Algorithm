def solve(idx, currentSum):
    global mini

    if currentSum >= mini:
        return

    # 현재 인덱스가 끝일때 (N-1)까지 돌았음
    if idx >= N:

        # 만약 현재까지의 합이 B보다 크면 합을 mini로 바꿔줌
        if currentSum >= B:
            mini = currentSum
        return

    # 현재 인덱스는 당연히 방문처리를 해줌
    visited[idx] = 1

    # 그리고 그 다음 인덱스, 현재합+현재인덱스값 = 뉴 합
    solve(idx+1, currentSum+heights[idx])

    # idx >= N에서 리턴한 후 인덱스 안 방문처리
    visited[idx] = 0

    # 그 전에 값에서 현재 가진 합으로 또 돌려보기
    solve(idx+1, currentSum)

T = int(input())

for tc in range(1, T+1):

    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort()

    mini = 2147000000

    visited = [0]*N
    solve(0, 0)

    print('#{} {}'.format(tc, mini - B))