import sys
sys.stdin = open('창용 마을 무리의 개수_input.txt')

#1 2
#2 1

def bfs(node, arr, visit):
    global answer
    queue = [node] # 큐에 넣는다.
    visit[node] = 1 # 방문 처리
    while True: # 큐가 빌 때까지 돌립니다.
        if len(queue) == 0:
            answer += 1
            return
        current_node = queue.pop(0)
        for find_node in range(len(arr[current_node])):
            if visit[arr[current_node][find_node]] == 0: # 아직 방문한 곳이 아니면 큐에 넣고 방문 처리하자.
                queue.append(arr[current_node][find_node])
                visit[arr[current_node][find_node]] = 1


T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    n, m = map(int, input().split())
    # 아는 사이인 지 판단하기 위한 배열 선언
    arr = [ [] for _ in range(n+1) ]
    # 방문 여부 판단을 위한 배열 선언
    visit = [0] * (n+1)
    # 아는 사이이면 배열에 추가
    for i in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    # 방문하지 않은 모든 노드에 bfs 실행
    for i in range(1, n+1):
        if visit[i] == 0:
            bfs(i, arr, visit)

    print("#{0} {1}".format(test_case, answer))
