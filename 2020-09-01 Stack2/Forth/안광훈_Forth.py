T = int(input())

for t in range(1, T+1):
    cal_formula = input().split()

    result = 0
    stack = []
    operators = ['+', '-', '*', '/']

    for char in cal_formula:
        # 연산자일 경우
        if char in operators:
            # Error: 숫자가 2개 이상 존재하지 않을 때
            if len(stack) < 2:
                result = 'error'
                break

            num2 = stack.pop()
            num1 = stack.pop()

            # 연산자에 따른 계산
            if char == '+':
                stack.append(num1+num2)
            elif char == '-':
                stack.append(num1-num2)
            elif char == '*':
                stack.append(num1*num2)
            else:
                stack.append(num1//num2)
        # 계산이 끝났을 때
        elif char == '.':
            # Error: 숫자가 2개 이상 남아있을 때
            if len(stack) > 1:
                result = 'error'
            else:
                result = stack[0]
            break
        # 숫자일 경우
        else:
            stack.append(int(char))

    print('#{} {}'.format(t, result))
