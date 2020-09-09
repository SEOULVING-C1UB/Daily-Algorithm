import sys

sys.stdin = open("D5_1248_공통조상_input.txt", "r")


def mutual_ancestor(a, b):
    # 트리 작성: 0에 자기 자신, 1-2에 자식, 3에 부모 노드 번호 기입
    for i in range(1, v+1):
        Tree[i][0] = i

    for i in range(0, e*2, 2):
        parent, child = edges[i], edges[i+1]
        if Tree[parent][1]:
            Tree[parent][2] = child
        else:
            Tree[parent][1] = child
        Tree[child][3] = parent
    
    # 공통 조상 mutual_root 찾기
    parents_a = find_root(a)
    parents_b = find_root(b)
    mutual_root = 0
    for parent in parents_a:
        if parent in parents_b:
            mutual_root = parent
            break
    
    # 서브 트리의 크기 구하기
    subtree_size = tree_size(mutual_root)

    print(mutual_root, subtree_size)
    

# input으로부터 가까운 순서대로 부모들의 리스트를 작성하여 리턴
def find_root(x):   
    parents_x = []
    child = x
    while True:
        parent_x = Tree[child][3]
        if parent_x:
            parents_x.append(parent_x)
            child = parent_x
        else:
            break
    return parents_x
    

# 한 root로부터의 서브트리의 사이즈를 재귀적으로 계산하여 리턴
# 순회하면서 visit할 때마다 cnt += 1 하는 방법도 가능
# 더 빠른 방법은?
def tree_size(x):
    if Tree[x][1] == 0 and Tree[x][2] == 0:
        return 1
    # 주의: 리턴할 때 자기 자신도 카운트해야 하므로 1을 더해야
    elif Tree[x][1] != 0 and Tree[x][2] == 0:
        return tree_size(Tree[x][1]) + 1
    elif Tree[x][1] == 0 and Tree[x][2] != 0:
        return tree_size(Tree[x][2]) + 1
    else:
        left = Tree[x][1]
        right = Tree[x][2]
        return tree_size(left) + tree_size(right) + 1

t = int(input())
for test_case in range(t):    
    v, e, input1, input2 = map(int, input().split())
    edges = list(map(int, input().split()))
    Tree = [[0]*(4) for _ in range(v+1)]        
    print('#' + str(test_case + 1), end=" ")
    mutual_ancestor(input1, input2)