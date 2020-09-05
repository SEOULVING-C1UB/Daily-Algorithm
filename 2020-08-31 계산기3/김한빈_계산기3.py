import sys

sys.stdin = open('계산기3.txt', 'r')

def change(arr):
    result = []
    stack = []
    for s in arr:
        if s.isnumeric():
            result.append(s)
        elif s == '*':
            if len(stack) != 0:
                if stack[-1] == '*':
                    result.append(stack.pop())
            stack.append(s)
        elif s == '+':
            if len(stack) != 0:
                if stack[-1] != '(':
                    result.append(stack.pop())
            stack.append(s)
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            if stack[-1] == '(':
                stack.pop()
    return result

def calculate(arr):
    stack = []
    try:
        for n in arr:
            if n.isnumeric():
                stack.append(int(n))
            else:
                if n == '+':
                    new = stack.pop() + stack.pop()
                    stack.append(new)
                elif n == '*':
                    new = stack.pop() * stack.pop()
                    stack.append(new)
        return stack
    except:
        print('error')



for t in range(1, 11):
    print(f'#{t}', end=' ')
    length = int(input())
    arr = input()
    stack = []
    arr = change(arr)
    print(calculate(arr)[0])

