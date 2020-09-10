import sys

sys.stdin = open("D3_5178_노드의합_input.txt", "r")

def node_sum(target):
    last = n
    # 2개씩 더하면서 반복하기 위해 n이 홀수인 경우 부모 노드에 값을 적어주고 n-1부터 시작
    if last % 2 == 0:
        Tree[last//2] = Tree[last]
        last -= 1

    for i in range(last, target, -2):        
        Tree[i//2] = Tree[i]+Tree[i-1]
    
    return Tree[target]


t = int(input())
for test_case in range(t):    
    n, m, l = map(int, input().split())
    
    Tree = [0]*(n+1)    
    for _ in range(m):
        num, value = map(int, input().split())
        Tree[num] = value
    
    print('#' + str(test_case + 1), node_sum(l))    
