# 중위표기식을 후위표기식으로 만드는 함수
def trans(cmd):
    # 연산자를 넣을 스택
    stack = []
    # 후위표기식을 넣을 스택
    who = []
    # 연산자는 스택에 들어가기 전에는 yeon의 순서로, 스택에 들어간 후에는 yeon2와 같은 순서오 우선순위를 가짐
    yeon = ["(", "*", "+", ")"]
    yeon2 = ["*", "+", ")", "("]
    for c in cmd:
        # cmd의 원소가 연산자가 아닌경우 후위표기식에 push
        if c not in yeon:
            who.append(c)
        # cmd의 원소가 연산자인 경우
        # 스택에 아무것도 없거나 스택의 top의 우선순위보다 높으면 push
        elif len(stack) == 0 or yeon.index(stack[-1])>yeon.index(c):
            stack.append(c)
        # 스택의 탑보다 우선순위가 낮은경우
        else:
            # 스택에 아무것도 없거나 스택의 top의 우선순위보다 높아 질때 까지 후위표기식에 push하며 스택에서는 pop
            while len(stack)>0 and yeon2.index(stack[-1])<yeon2.index(c):
                who.append(stack[-1])
                stack.pop()
            # while문이 끝나면 현재 원소가 닫는 괄호인지 확인
            # 닫는 괄호이면 stack의 top은 여는괄호이므로 pop하여 삭제
            # 아닌경우 현재 원소를 push
            else:
                if c == ")":
                    stack.pop()
                else:
                    stack.append(c)
    # 만들어진 후위 표기식과 스택에 남은 연산자를 합침
    return who+stack

# 후위표기식으로 만든 수식을 연산하기 위한 함수
def yeon(cmd):
    yeon = "+*-/"
    # 피연산자를 넣을 스택
    stack = []
    for c in cmd:
        # 연산자가 아닌경우 스택에 push
        if c not in yeon:
            stack.append(int(c))
        else:
            # 연산자인 경우 스택의 맨위 두원소를 연산한후 스택에 푸시
            if c == "+":
                ans = stack[-2] + stack[-1]
            elif c == "*":
                ans = stack[-2] * stack[-1]
            elif c == "-":
                ans = stack[-2] - stack[-1]
            elif c == "/":
                ans = stack[-2] // stack[-1]
            stack.pop()
            stack.pop()
            stack.append(ans)
    return stack[-1]

for i in range(10):
    n = int(input())
    cmd = list(input())
    print('#{} {}'.format(i+1, yeon(trans(cmd))))