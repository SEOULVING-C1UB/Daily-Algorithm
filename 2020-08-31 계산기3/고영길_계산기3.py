for tc in range(1, 11):
    N = int(input())
    data = input()
    stack = []
    num_lst = []

    push_prio = {'*': 2, '+': 1, '(': 3}
    pop_prio = {'*': 2, '+': 1, '(': 0}

    # Change to postfix
    for i in range(N):
        if data[i].isdigit():
            num_lst.append(data[i])

        else:
            if not stack:
                stack.append(data[i])
                continue

            else:
                if data[i] == ')':
                    while stack[-1] != '(':
                        num_lst.append(stack.pop())
                    stack.pop()

                elif push_prio[data[i]] > pop_prio[stack[-1]]:
                    stack.append(data[i])

                else:
                    while push_prio[data[i]] <= pop_prio[stack[-1]]:
                        num_lst.append(stack.pop())
                    stack.append(data[i])


    for i in range(len(num_lst)):
        if num_lst[i].isdigit():
            stack.append(num_lst[i])

        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if num_lst[i] == "+":
                tmp = num1 + num2
            elif num_lst[i] == "*":
                tmp = num1 * num2

            stack.append(str(tmp))

    print(f'#{tc} {stack[0]}')
