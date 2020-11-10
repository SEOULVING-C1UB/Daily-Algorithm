
def nodefinder(start, end) :
    queue = []
    queue.append(start)
    visited = {}            # visited 라는 딕셔너리를 만든다.
    visited[start] = 1      # 딕셔너리에 start 키값을 추가하고 초기값을 1로 설정

    while queue :
        now = queue.pop(0)

        for w in node_dict[now] :
            if visited.get(w, 0) == 0 :
                queue.append(w)
                visited[w] = visited[now] + 1       # 이전 방문 값 + 1을 새로운 키값으로 딕셔너리에 저장
                node_dict[w].remove(now)            # 이전 정보 제거
                print(node_dict)
                if w == end :                       # 만약에 도착했으면 함수 종료 (1 빼줘야됨)
                    return visited[w] - 1

    return visited[w]-1


tc = int(input())

for t in range(tc) :
    node, line = map(int, input().split())
    lines = []
    node_dict = { i:[] for i in range(1, node+1) }
    for i in range(line) :      # 연결 정보를 받아서
        lines.append(list(map(int, input().split())))

    start, end = map(int, input().split())

    for i in range(line):       # 만들어놓은 딕셔너리에 연결정보 추가
        s = lines[i][0]
        e = lines[i][1]
        node_dict[s].append(e)
        node_dict[e].append(s)

    result = nodefinder(start, end)
    print("#{} {}".format(t+1, result))