import sys

sys.stdin = open("Forth_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    stack = []
    res = 0
    err = []
    command = list(input().split())

    for com in command:
        if com == '.':
            if len(stack) > 1:
                err.append('error')
                break
            else:
                res = stack.pop()
                break
        elif com in ['+','-','*','/']:
            if len(stack) < 2:
                err.append('error')
                break
            else:
                a, b = stack.pop(), stack.pop()
                if com == '+':
                    stack.append(b + a)
                elif com == '-':
                    stack.append(b - a)
                elif com == '*':
                    stack.append(b * a)
                elif com == '/':
                    stack.append(b // a)
        else:
            stack.append(int(com))

    if err:
        print('#{} {}'.format(test_case, err[0]))
    else:
        print('#{} {}'.format(test_case, res))