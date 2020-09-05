import sys

sys.stdin = open("D2_4874_input.txt", "r")


def forth():    
    stack = []
    operator = ['+', '-', '*', '/']
    for element in code:        
        if element == '.':
            if stack:
                result = stack.pop()
                # 종료 기호가 나온 후에 스택안에 숫자는 하나만 있어야 함
                if stack:
                    return 'error'
                else:
                    return result
            # 종료 기호가 나왔는데 스택이 비어있다면 리턴할 것이 없으므로 에러
            else:
                return 'error'
        if element not in operator:
            stack.append(int(element))
        else:
            # 연산자가 나왔음
            # 스택에서 숫자 2개를 꺼내야 하는데 스택이 비었으면 에러
            if not stack:
                return 'error'
            else:
                num2 = stack.pop()
                # 숫자가 1개만 있다면 2개를 꺼낼 수 없으니 에러
                if not stack:
                    return 'error'
                num1 = stack.pop()
                if element == '+':
                    stack.append(num1+num2)
                elif element == '-':
                    stack.append(num1-num2)
                elif element == '*':
                    stack.append(num1*num2)
                else:
                    stack.append(num1//num2)

t = int(input())
for test in range(t):
    code = list(input().split())    
    print('#'+str(test+1), forth())