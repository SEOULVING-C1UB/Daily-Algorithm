import sys
sys.stdin = open('이진탐색_input.txt', 'r')

for TC in range(int(input())):
    N = int(input())
    n = 0   # 현재 트리의 높이 변수 n
    while 2**n <= N:
        n += 1
    end_nodes = N - 2**(n-1) + 1    # 마지막 줄 노드 개수
    left_nodes = 2**(n-2) - 1       # 마지막 줄을 제외한 왼쪽 부분 노드의 개수
    if end_nodes <= 2**(n-2):       # 마지막 줄이 반보다 덜 채운 경우의 if문
        root_node = left_nodes + end_nodes + 1  # root node는 왼쪽 노드의 총 개수 + 1의 값
    else:
        root_node = left_nodes + 2**(n-2) + 1   # root node는 왼쪽 노드의 총 개수 + 1의 값
    middle_node = 2 * end_nodes - 1             # 마지막 노드의 부모 노드의 값을 구하기 위한 변수
    if end_nodes % 2:                           # 마지막 줄의 노드 개수가 홀수개면
        middle_node += 1                        # 마지막 노드는 왼쪽 자식이므로 부모는 그보다 1 많다
    else:
        middle_node -= 1                        # 아니면 오른쪽 자식이므로 부모는 그보다 1 적다
    print('#{} {} {}' .format(TC+1, root_node, middle_node))