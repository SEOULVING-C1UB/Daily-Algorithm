import sys

sys.stdin = open("연산_input.txt", "r")

from collections import deque


# deque을 이용한 BFS(거리가 모두 같기 때문에 다익스트라와 동일)
def calculate(start, goal):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        v = q.popleft()
        if v == goal:
            break
        
        # v와 연결된 4개 노드(+1, -1, *2, -10)를 deque에 추가
        if 1 <= v-1 <= 1000000 and not visited[v-1]:
            q.append(v-1)
            visited[v-1] = visited[v] + 1
        if 1 <= v+1 <= 1000000 and not visited[v+1]:
            q.append(v+1)
            visited[v+1] = visited[v] + 1
        if 1 <= v*2 <= 1000000 and not visited[v*2]:
            q.append(v*2)
            visited[v*2] = visited[v] + 1
        if 1 <= v-10 <= 1000000 and not visited[v-10]:
            q.append(v-10)
            visited[v-10] = visited[v] + 1

    return visited[goal]-1


t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    # n에서 몇 번 연산해야 도달할 수 있는지 담는 배열 생성
    visited = [0] * (1000001)
    print('#' + str(test_case + 1), calculate(n, m))