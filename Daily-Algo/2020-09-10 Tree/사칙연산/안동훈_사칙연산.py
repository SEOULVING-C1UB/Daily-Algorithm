import sys
sys.stdin = open('사칙연산_input.txt')

def calculate(node):
    if nodes[node][0] in '+-*/': # 노드의 값이 연산자면 stack에서 값을 꺼내 계산하고 다시 집어넣는다.
        if nodes[node][0] == '+':
            num2 = answer.pop()
            num1 = answer.pop()
            result = num1 + num2
            answer.append(result)
        elif nodes[node][0] == '-':
            num2 = answer.pop()
            num1 = answer.pop()
            result = num1 - num2
            answer.append(result)
        elif nodes[node][0] == '*':
            num2 = answer.pop()
            num1 = answer.pop()
            result = num1 * num2
            answer.append(result)
        elif nodes[node][0] == '/':
            num2 = answer.pop()
            num1 = answer.pop()
            result = num1 / num2
            answer.append(result)
    else: # 숫자면
        number = int(nodes[node][0])
        answer.append(number)

def post_order(node):
    if node <= n and nodes[node][0] != 'temp':
        try: # 자식 노드들도 돌려돌려
            post_order(int(nodes[node][1]))
            post_order(int(nodes[node][2]))
        except:
            pass
        calculate(node)

T = 10
for test_case in range(1, T + 1):
    answer = [] # 계산을 위한 stack
    n = int(input())
    nodes = [['temp', 0, 0] for _ in range(n+1)] # value, left, right
    for i in range(n): # 노드 만들기
        input_ = list(input().split())
        nodes[int(input_[0])][0] = input_[1]
        try:
            nodes[int(input_[0])][1] = input_[2]
            nodes[int(input_[0])][2] = input_[3]
        except:
            pass

    # 후위 순회를 돌며 모든 노드에 방문하면 될 것으로 생각됨.
    post_order(1) # 루트에서부터 시작한다.

    print("#{0} {1}" . format(test_case, int(answer.pop()))) # 정수로 변경하여 출력할 것
