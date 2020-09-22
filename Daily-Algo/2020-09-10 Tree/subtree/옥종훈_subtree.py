import sys

sys.stdin = open("D2_5174_subtree_input.txt", "r")


# pre-order 순회를 하며 visit할 때마다 subtree의 사이즈를 리턴
def subtree(node):
    if node:
        left = subtree(Tree[node][1])
        right = subtree(Tree[node][2])
        # 왼쪽과 오른쪽의 subtree의 사이즈를 더한 후 자기 자신을 count
        return left + right + 1
    # node == 0일 때, 즉 말단에 도달하면 0을 리턴
    else:
        return 0


t = int(input())
for test_case in range(t):    
    e, n = map(int, input().split())
    
    # 트리 작성
    Tree = [[0]*(e+2) for _ in range(e+2)]    
    edges = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        parent, child = edges[i], edges[i+1]
        if not Tree[parent][1]:
            Tree[parent][1] = child
        else:
            Tree[parent][2] = child
        Tree[child][3] = parent

    print('#' + str(test_case + 1), subtree(n))
