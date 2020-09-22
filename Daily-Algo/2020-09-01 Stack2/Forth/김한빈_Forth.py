import sys

sys.stdin = open('Forth.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    arr = list(input().split())

    stack = []
    try:
        for n in arr:
            if n.isnumeric():
                stack.append(int(n))
            else:
                if n == '+':
                    new = stack.pop() + stack.pop()
                    stack.append(new)
                elif n == '-':
                    new = stack.pop(-2) - stack.pop()
                    stack.append(new)
                elif n == '*':
                    new = stack.pop() * stack.pop()
                    stack.append(new)
                elif n == '/':
                    new = int(stack.pop(-2) / stack.pop())
                    stack.append(new)
                elif n == '.':
                    if len(stack) != 1:
                        print('error')
                    else:
                        print(stack.pop())
    except:
        print('error')