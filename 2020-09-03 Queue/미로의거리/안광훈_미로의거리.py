import sys
from queue import Queue

sys.stdin = open('미로의_거리.txt')

# T: 테스트 케이스 개수
T = int(input())

# t: 테스트 케이스 번호
for t in range(1, T + 1):
    # N: 미로의 크기, maze: 미로 리스트
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    # 상하좌우 리스트
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # visited: 방문 체크 리스트, queue: bfs 기반 큐
    visited = [[0] * N for _ in range(N)]
    queue = Queue()

    # 시작점 찾는 함수
    def get_start_index():
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    return [i, j]

    # n: 미로 크기, k: 방문한 노드 개수, m: 이번 차례에 방문할 노드 개수
    def find_path(n, k, m):
        # 방문할 노드가 없을 경우 0 리턴
        if queue.empty():
            return 0

        # 다음 차례에 방문할 노드 개수
        new_m = 0

        for _ in range(m):
            node = queue.get()
            for i in range(4):
                new_y = node[0] + dy[i]
                new_x = node[1] + dx[i]
                # 인덱스 범위, 방문 여부 체크
                if 0 <= new_x < n and 0 <= new_y < n and not visited[new_y][new_x]:
                    # 도착했다면 k 리턴
                    if maze[new_y][new_x] == 3:
                        return k
                    # 통로일 때만 지나가기
                    if not maze[new_y][new_x]:
                        visited[new_y][new_x] = 1
                        queue.put([new_y, new_x])
                        new_m += 1

        return find_path(n, k + 1, new_m)

    start_y, start_x = get_start_index()
    visited[start_y][start_x] = 1
    queue.put([start_y, start_x])

    result = find_path(N, 0, 1)

    print('#{} {}'.format(t, result))
