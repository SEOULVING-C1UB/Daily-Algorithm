import sys
sys.stdin = open('1232.txt')

total_tc = 10



operators =['+', '-', '*', '/']
def calculator(node):
    #트리의 값이 숫자라면 그대로 리턴
    if tree[node][0] not in operators:
        return tree[node][0]
    #트리의 값이 연산자라면 하위의 값들 계산해서 그 값을 트리에 삽입
    else:
        operator, operand1, operand2, = tree[node][0], tree[node][1], tree[node][2]
        if operator == '+':
            tree[node][0] = calculator(tree[node][1]) + calculator(tree[node][2])
        elif operator == '-':
            tree[node][0] = calculator(tree[node][1]) - calculator(tree[node][2])
        elif operator == '*':
            tree[node][0] = calculator(tree[node][1]) * calculator(tree[node][2])
        elif operator == '/':
            tree[node][0] = calculator(tree[node][1]) / calculator(tree[node][2])
        else:
            print('error2')
        return tree[node][0]



for tc in range ( 1, total_tc+1 ):
    N = int(input())
    tree = [[0, 0, 0, 0] for _ in range (N+1)]



    # 입력받은 값으로 우선 트리를 만들어보자
    for i in range(1, N+1):
        #일시적으로 입력을 받고
        temp = list(input().split())
        #입력 받은 리스트의 길이로 나누어서 생각한다
        len_temp = len(temp)
        #네개인 경우
        if len_temp ==4:
            node, operator, lc, rc = int(temp[0]), temp[1], int(temp[2]), int(temp[3])
            tree[node][0] = operator
            tree[node][1] = lc
            tree[node][2] = rc
            tree[lc][3] = node
            tree[rc][3] = node
        #두개인 경우
        elif len_temp ==2:
            node, value = int(temp[0]), int(temp[1])
            tree[node][0] = value

        else:
            print('error 1')
    #트리에 있는 값으로 계산을 해보자
    result = calculator(1)
    print("#%d %d"%(tc, int(result)))









