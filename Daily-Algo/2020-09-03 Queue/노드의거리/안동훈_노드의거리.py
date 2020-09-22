import sys
sys.stdin = open('노드의거리_input.txt')

def bfs(node):
    queue = [[node, 0]] # 현재 노드 위치와 지금까지의 거리
    visit = [node] # 방문처리
    while len(queue) != 0: # 큐가 빌 때까지 돌립니다.
        current_node, distance = queue.pop(0)
        if current_node == g:
            return distance
        for i in range(v+1):
            if nodes[current_node][i] == 1 and i not in visit: # 연결되어 있으며, i를 아직 방문 안한 경우
                visit.append(i) # 방문 처리
                queue.append([i, distance + 1]) # 거리 1개 늘리고 큐에 추가
    return 0 # 도착 못할 경우 0을 리턴
T = int(input())
for test_case in range(1, T + 1):
    # input이 띄워쓰기 단위로 구분되어 있으므로, split()을 사용하여 list로 받아냅니다.
    v, e = map(int, input().split())
    # v 크기의 이차원 배열 선언
    nodes = [[0]*(v+1) for _ in range(v+1)] # 연결 되어 있으면 1 아니면 0

    for i in range(e):
        st, ed = map(int, input().split())
        nodes[st][ed] = 1
        nodes[ed][st] = 1
    s, g = map(int, input().split())
    # s 위치로부터 bfs를 돌린다.
    answer = bfs(s)

    print("#{0} {1}".format(test_case, answer))
