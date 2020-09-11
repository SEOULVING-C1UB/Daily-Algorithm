import sys
sys.stdin = open('노드의 합_input.txt', 'r')

for TC in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    n = 0   # 현재 트리의 높이를 담을 변수 n
    while 2**n <= N:
        n += 1
    for i in range(n, 1, -1):   # 밑바닥에서부터 위로 올라가면서 더하자
        if i == n:
            for j in range(N - 2**(n-1) + 1):   # 밑바닥이면 밑바닥의 노드 개수만큼만
                tree[(2**(i-1)+j)//2] += tree[2**(i-1)+j]
        else:
            for j in range(0, 2**(i-1), 2):     # 밑바닥이 아니면 현재 층의 노드 개수만큼만
                tree[(2**(i-1)+j)//2] = tree[2**(i-1)+j] + tree[2**(i-1)+j+1]
    print('#{} {}' .format(TC+1, tree[L]))      # 다 돌리고 L번 노드에 있는 값 출력