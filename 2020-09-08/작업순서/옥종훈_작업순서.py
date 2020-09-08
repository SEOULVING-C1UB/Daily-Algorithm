import sys
from collections import deque

sys.stdin = open("D6_1267_input.txt", "r")


def task_order():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for subnode in graph[now]:
            indegree[subnode] -= 1
            if indegree[subnode] == 0:
                q.append(subnode)
    
    for node in result:
        print(node, end=" ")
    print()

    
for test_case in range(10):    
    v,e = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = {i:[] for i in range(1, v+1)}    
    indegree = [0]*(v+1)
    for i in range(0, e*2, 2):
        graph[edges[i]].append(edges[i+1])       
        indegree[edges[i+1]] += 1
    print('#' + str(test_case + 1), end=" ")
    task_order()