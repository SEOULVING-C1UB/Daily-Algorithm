
'''
24 2
1 17 3 22 1 8 1 7 7 1 2 7 2 15 15 4 6 2 11 6 4 10 4 2
'''

import sys
sys.stdin = open('contact_input.txt', 'r')

def connector(start) :
    queue = []
    queue.append(start)
    visited[start] = 1

    while queue :
        start = queue.pop(0)
        for w in node_dict[start] :
            if visited[w] == 0  :       # 방문하지 않은 곳에 대해
                queue.append(w)         # 큐에 넣어주고
                visited[w] = visited[start] + 1     # 이전 연결 방문값에 1씩 더해주면서 카운트한다.

for t in range(10) :
    num, startnode = map(int, input().split())
    templi = list(map(int, input().split()))

    visited = [0] * (num+1)
    node_dict = { i:[] for i in range(1, num+1)}    # 1부터 num크기의 딕셔너리를 만들어준다.
    arr = []

    for i in range(0, len(templi), 2) :
        start = templi[i]
        end = templi[i+1]
        node_dict[start].append(end)        # 연결 정보를 딕셔너리에 넣는다.

    connector(startnode)
    print(node_dict)

    maxi = 0

    for i in range(1, num+1) :
        if visited[maxi] <= visited[i] :
            maxi = i

    print("#{} {}".format(t+1, maxi))