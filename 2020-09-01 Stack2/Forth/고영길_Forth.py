import sys

sys.stdin = open('Forth_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    opers = input().split()
    stack = []
    ans = 0
    for i in range(len(opers)):
        # In case letter is a number
        if opers[i].isdigit():
            stack.append(opers[i])
        else:
            # end condition
            if opers[i] == '.':
                # At the end of the loop, if stack has more than one or empty,
                # -> error
                if len(stack) == 1:
                    ans = stack.pop()
                else:
                    ans = 'error'
            else:
                if len(stack) >= 2:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    if opers[i] == '+':
                        stack.append(num1 + num2)
                    elif opers[i] == '-':
                        stack.append(num1 - num2)
                    elif opers[i] == '*':
                        stack.append(num1 * num2)
                    # you have to use '//' because result of '/' is float type
                    elif opers[i] == '/':
                        stack.append(num1 // num2)
                # If there are not enough numbers in the stack
                else:
                    ans = 'error'
                    break
    print(f'#{tc} {ans}')
