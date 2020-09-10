import sys
sys.stdin = open("5178_노드의합.txt")

'''
<풀이과정>
: 후위순회 이용
1) 각 노드에 대해 왼쪽 자식이 있고 그 값이 0이 아니면 현재노드에 값 더하기
2) 0인 경우 재귀호출
3) 오른쪽 자식에도 같은 방식으로 적용
'''

def nodesum(v):
    if 2*v <= n:                        # 왼쪽 자식이 있는 경우
        if nodes[2*v] == 0:             # 값이 0이면 합을 계산하지 않았으므로 재귀호출
            nodesum(2*v)
        nodes[v] += nodes[2*v]          # 재귀가 끝난 후 현재 노드에 왼쪽 자식 값 더하기
    if 2*v+1 <=n:                       # 오른쪽 자식이 있는 경우
        if nodes[2*v+1] == 0:           # 값이 0이면 합을 계산하지 않았으므로 재귀호출
            nodesum(2*v+1)
        nodes[v] += nodes[2*v+1]        # 재귀가 끝난 후 현재 노드에 오른쪽 자식 값 더하기


t = int(input())

for i in range(1,t+1):
    n, m, l = map(int, input().split())
    nodes = [0]*(n+1)
    for j in range(m):
        node, num = map(int,input().split())
        nodes[node] = num
    nodesum(1)
    print('#{} {}'.format(i,nodes[l]))