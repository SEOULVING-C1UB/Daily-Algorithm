for t in range(1, 11):
    N = int(input())
    chars = input()

    stack = []

    # 후위표기법 담을 변수
    new_chars = ''

    # 연산자 우선순위
    priority = dict([('*', 1), ('+', 0), ('(', -1)])

    # 중위표기법 => 후위표기법
    for char in chars:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # 오른쪽 괄호가 나왔으므로 왼쪽 괄호가 나올 때까지 모두 pop
            while stack[-1] != '(':
                new_chars += stack.pop()
            # 왼쪽 괄호 pop
            stack.pop()
        elif char == '*' or char == '+':
            # stack이 비어있는지 체크 & 자신과 같거나 높은 우선순위 연산자 모두 pop
            while len(stack) and priority[char] <= priority[stack[-1]]:
                new_chars += stack.pop()
            stack.append(char)
        # 숫자는 바로 후위표기법 변수에 추가
        else:
            new_chars += char

    # stack에 남아 있는 연산자들 추가
    while len(stack):
        new_chars += stack.pop()

    # 후위표기법 계산
    for char in new_chars:
        # 더하기 계산
        if char == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
        # 곱하기 계산
        elif char == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)
        # 숫자는 stack에 쌓음
        else:
            stack.append(int(char))

    print('#{} {}'.format(t, stack[0]))
