import sys
sys.stdin = open('배열_최소_합.txt')

# T: 테스트 케이스 개수
T = int(input())

# t: 테스트 케이스 번호
for t in range(1, T + 1):
    # N: 고르는 숫자 개수, array: 주어진 배열
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    # result: 답, 최대 합은 10 * N이므로 이걸로 초기화
    # visited: 방문 체크 리스트
    result = 10 * N
    visited = [0 for _ in range(N)]

    # k: 총 방문한 노드의 개수, cur_sum: 현재 노드의 합
    def get_sum(k, cur_sum):
        global result, N

        # N개를 선택했을 때
        if k == N:
            # 더 작은 값으로 result에 넣기
            result = min(result, cur_sum)
            return

        # 이미 합이 result 이상일 경우 중단
        if cur_sum >= result:
            return

        for i in range(N):
            # 방문한 적이 없을 때
            if not visited[i]:
                # 방문 처리하고
                visited[i] = 1
                # 방문한 상태로 다음 노드로 감
                get_sum(k + 1, cur_sum + array[k][i])
                # 방문 처리 해제
                visited[i] = 0


    get_sum(0, 0)
    print('#{} {}'.format(t, result))
