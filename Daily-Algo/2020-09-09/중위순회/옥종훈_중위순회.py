import sys

sys.stdin = open("D4_중위순회_1231_input.txt", "r")

def in_order(node):
    left = Tree[node][1]
    right = Tree[node][2]
    if node:        
        result = in_order(left) + Tree[node][0] + in_order(right) 
        return result
    else:
        return ''


for test_case in range(10):    
    n = int(input())
    # 트리 작성
    # 0에 해당 노드의 알파벳, 1~2에 자식 노드, 3에 부모
    Tree = [[0]*4 for _ in range(n+1)]
    for i in range(1, n+1):
        chars = list(input().split())
        Tree[i][0] = chars[1]
               
        j = 2
        while j < len(chars):
            Tree[i][j-1] = int(chars[j])
            Tree[int(chars[j])][3] = i
            j += 1

    print('#' + str(test_case + 1), in_order(1))
    