import sys

sys.stdin = open("D2_5176_이진탐색_input.txt", "r")


def in_order(node, start):
    if node <= n:
        left = in_order(node*2, start)
        # 부모노드는 왼쪽 자식보다 1이 커야 함
        mid = Tree[node][0] = left + 1
        # 오른쪽 자식은 부모보다 큰 수에서 시작해야하기 때문에 start값을 부모 값으로 함
        right = in_order(node*2+1, mid)
        return right
    else:
        # 노드가 없으면 start를 리턴하여 최하단 노드에 start+1이 기록되게끔 함
        return start


t = int(input())
for test_case in range(t):    
    n = int(input())
    
    # 트리를 다 채운 후 in-order를 이용해 루트의 값과 n//2번 노드의 값 찾기
    # 0번에는 노드의 값, 1~2번에는 자식 노드의 번호, 3번에는 부모 노드 번호
    Tree = [[0]*(4) for _ in range(n+1)]
    for i in range(1, n+1):
        Tree[i][1] = i*2
        Tree[i][2] = i*2 + 1
        Tree[i][3] = i//2
    
    # start를 0으로 해야 좌측 최하단 노드에 1이 기록됨
    in_order(1, 0)
    print('#' + str(test_case + 1), Tree[1][0], Tree[n//2][0])    
