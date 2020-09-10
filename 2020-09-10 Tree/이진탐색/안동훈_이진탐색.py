import sys
sys.stdin = open('이진탐색_input.txt')

def make_tree(node):
    global idx
    if node <= n: # 1부터 n까지만 value에 추가하도록 하자.
        make_tree(node*2)
        tree[node] = idx
        idx += 1
        make_tree(node*2+1)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    tree = [i for i in range(n+1)] # 트리 만들기 전 배열
    idx = 1
    # 트리를 만들어야만 한다.
    make_tree(1)
    print("#{0} {1} {2}" . format(test_case, tree[1], tree[n//2]))
