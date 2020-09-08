def bfs(start):
    global answer
    queue = [[start, 0]] # 현재 노드 위치부터 현재까지 거리
    # 이미 방문한 곳을 처리하기 위한 배열
    visit = [start]
    temp_queue = [[0 ,0]]
    while len(queue) != 0: # 큐가 빌 때까지 돌립니다.
        # temp_queue에 distance가 가장 높은 것들만 넣습니다.
        for find in queue:
            if find[1] > temp_queue[0][1]:
                temp_queue = []
                temp_queue.append(find)
            elif find[1] == temp_queue[0][1]:
                temp_queue.append(find)
        current_node, distance = queue.pop(0)
        for i in range(1,101):
            if node[current_node][i] == 1 and i not in visit: # 연결되어 있으며, i를 아직 방문 안한 경우
                visit.append(i)
                queue.append([i, distance + 1])
        # 만약 queue에 아무것도 들어있지 않다면, temp_queue에 남아 있는 것들이 마지막으로 연락된 노드일 것입니다.
    # 이제, temp_queue에 있는 값 중 node의 idx가 가장 큰 것들을 구해서 answer에 담습니다.
    for nd in temp_queue:
        if answer < nd[0]:
            answer = nd[0]

T = 10
for test_case in range(1, T + 1):
    answer = 0
    data_count, start_node = map(int, input().split())
    # 연락 인원은 최대 100명이며, 부여될 수 있는 번호는 1이상, 100이하
    # 연락을 위한 간선을 표현하기 위해 이차원 배열을 선언한다.
    node = [[0]*101 for _ in range(101)]

    input_data = list(map(int, input().split()))
    for i in range(0, data_count, 2):
        # 노드를 이어준다.
        from_node, to_node = input_data[i], input_data[i+1]
        node[from_node][to_node] = 1

    bfs(start_node)

    print('#{0} {1}' .format(test_case, answer))