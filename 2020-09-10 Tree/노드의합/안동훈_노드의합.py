import sys
sys.stdin = open('노드의합_input.txt')


T = int(input())
for test_case in range(1, T + 1):
    # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    n, m, l = map(int,input().split())
    tree = [0]*(n+1) # 트리 선언
    for i in range(m):
        idx, value = map(int,input().split()) # 노드 번호, 노드의 값
        tree[idx] = value
    # left 노드의 값을 부모 노드에 더해준다.
    for i in range(n, 0, -1):
        tree[i//2] += tree[i]

    answer = tree[l]
    print("#{0} {1}" . format(test_case, answer))
