'''
<문제해결>
 : 운반할수있는 최대 무게의 화물을 순서대로 이동하는것으로 해결
1) 화물은 무거운순으로 트럭은 적재량이 적은 순으로 정렬
2) 적재량이 적은 차부터 화물을 방문하여 적재 가능하면 운반
3) 운반한 화물은 방문 표시
'''

import sys
sys.stdin = open("5201_컨테이너운반.txt")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())),reverse=True)    # 화물 무거운순 정렬
    t = sorted(list(map(int, input().split())))                 # 트럭 적재량 적은 순 정렬
    visited = [0 for _ in range(n)]                             # 방문표시할 리스트
    s = 0
    for j in range(m):                                          # 각각의 트럭에 대해
        for i in range(n):                                      # 화물을 순회하며
            if visited[i] == 0 and w[i] <= t[j]:                # 운반하지 않은 화물중 적재가능한 화물을 찾아 운반(무거운순으로 정렬되어있기 때문에 옮길수있는 최대무게임)
                s += w[i]                                       # 정답에 해당 화물 무게 더해주고
                visited[i] = 1                                  # 방문표시
                break
    print('#{} {}'.format(tc, s))