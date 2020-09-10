import sys
sys.stdin = open('input.txt', 'r')

import collections

T = int(input())

def move(i, j, count):
    # 전역변수 설정
    global best
    global s_point
    # 탐색 방향
    mode_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 방문 순서대로 쌓을 큐, 시작하는 방을 초기값으로
    v_list = collections.deque([room[i][j]])
    while True:
        # 더 이상 변화가 없을 때 while을 빠져나가기 위한 장치
        temp = count
        # 각 방향 탐색 중 1이 커지는 방이 있다면
        for mode in mode_list:
            if 0 <= i + mode[0] < n and 0 <= j + mode[1] < n and room[i + mode[0]][j + mode[1]] - room[i][j] == 1:
                # 가려는 방이 이미 방문한 방이라면
                if room[i + mode[0]][j + mode[1]] in visited:
                    # 그 방에 기록된 최대 이동거리에 현재 이동거리를 더한다
                    count += visited[room[i + mode[0]][j + mode[1]]]
                    # 현재 최고값과 같다면 시작점을 더 작은 것으로 교체
                    if best == count:
                        s_point = min(s_point, v_list[0])
                    # 현재 이동거리가 최고라면, 시작점과 최고값을 갱신
                    elif best < count:
                        best = count
                        s_point = v_list[0]
                    # 지금까지 이동해온 방들의 최대 이동거리를 갱신
                    while v_list:
                        if v_list[0] not in visited or visited[v_list[0]] < count:
                            visited[v_list.popleft()] = count
                        count -= 1
                    return
                # 방문하지 않은 방이라면 이동, 방문 리스트에 담기
                i, j = i + mode[0], j + mode[1]
                v_list.append(room[i][j])
                count += 1
        # 더이상 변화가 없다면 탈출
        if temp == count: break
    # 위에서 한 작업과 같은 작업
    if best == count:
        s_point = min(s_point, v_list[0])
    elif best < count:
        best = count
        s_point = v_list[0]
    while v_list:
        if v_list[0] not in visited or visited[v_list[0]] < count:
            visited[v_list.popleft()] = count
        count -= 1
    return

for test_case in range(1, T + 1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    visited = dict()
    best = 0                # 최대 이동 횟수
    s_point = float('inf')  # 최대 이동 횟수를 가진 시작점(min을 쓰기위해 초기값 무한대)
    # 방문하지 않은 방들부터 시작해서 탐색
    for i in range(n):
        for j in range(n):
            if room[i][j] in visited:
                continue
            move(i, j, 1)
    # 시작점과 최대 이동횟수
    print('#{} {} {}'.format(test_case, s_point, best))