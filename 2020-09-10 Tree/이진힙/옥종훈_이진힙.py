import sys

sys.stdin = open("D2_5177_이진힙_input.txt", "r")

# 트리 작성
def writing_tree():
    for i in range(1, len(nodes)+1):
        # 일단 추가
        Tree[i] = nodes[i-1]
        # 부모 노드의 값이 자식 노드보다 크면 교체
        parent = i // 2
        child = i
        while Tree[parent] > Tree[child]:
            Tree[parent], Tree[child] = Tree[child], Tree[parent]
            child = parent
            parent = child // 2


def tree_sum(n):
    result = 0
    # n번 노드는 더할 필요 없으니 그 부모부터 반복적으로 더하기 시작
    parent = n//2
    while parent:
        result += Tree[parent]
        parent //= 2
    # parent == 0이 되면 루트까지 모두 더한 것이니 while문 나와서 리턴
    return result

t = int(input())
for test_case in range(t):    
    n = int(input())
    nodes = list(map(int, input().split()))
    
    Tree = [0]*(n+1)
    writing_tree()
    
    print('#' + str(test_case + 1), tree_sum(n))    
