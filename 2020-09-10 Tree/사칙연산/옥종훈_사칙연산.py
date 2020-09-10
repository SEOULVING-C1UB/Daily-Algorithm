import sys

sys.stdin = open("D4_1232_사칙연산_input.txt", "r")


# in-order 방식으로 계산
def calculation(node):
    # 0번에 연산자가 있으면 왼쪽 (연산) 오른쪽을 수행하여 리턴
    if Tree[node][0] in operator:
        if Tree[node][0] == '+':
            return calculation(Tree[node][1]) + calculation(Tree[node][2])
        elif Tree[node][0] == '-':
            return calculation(Tree[node][1]) - calculation(Tree[node][2])
        elif Tree[node][0] == '*':
            return calculation(Tree[node][1]) * calculation(Tree[node][2])
        else:
            return calculation(Tree[node][1]) / calculation(Tree[node][2])
    # 0번에 연산자가 없으면 말단이라는 뜻이므로 자신의 값을 리턴
    else:
        return Tree[node][0]


for test_case in range(10):    
    n = int(input())    
    operator = ['+', '-','*', '/']
    Tree = [[0]*3 for _ in range(n+1)]
    # 트리 작성: 0번에 연산자 혹은 숫자, 1~2번에 자식노드
    for i in range(1, n+1):
        info = input().split()
        if info[1] in operator:
            Tree[i][0] = info[1]
            Tree[i][1] = int(info[2])            
            Tree[i][2] = int(info[3])            
        else:
            Tree[i][0] = int(info[1])
    
    print('#' + str(test_case + 1), int(calculation(1)))    
