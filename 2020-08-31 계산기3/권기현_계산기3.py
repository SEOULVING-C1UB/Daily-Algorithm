import sys

sys.stdin = open('input.txt')


def infix2postfix(n, infix):
    operator_stack=[]
    postfix = []
    for i in range(0, n):
        if not isnumber(infix[i]):
            if not operator_stack:
                operator_stack.append(infix[i])
            else:
                if infix[i] != ")":

                    while priority_isp(operator_stack[-1]) >= priority_icp(infix[i]):
                        postfix.append(operator_stack.pop())

                    operator_stack.append(infix[i])
                else:
                    while operator_stack[-1] != "(":
                        postfix.append(operator_stack.pop())
                    operator_stack.pop()

        else:
            postfix.append(infix[i])
    return postfix

def isnumber(oper):
    nums=['0', '1', '2', '3','4', '5', '6', '7', '8', '9']
    if oper in nums:
        return True


def priority_icp(oper):
    if oper == '*' or oper =="/":
        return 2
    elif oper == "+" or oper == "-":
        return 1
    elif oper =="(":
        return 3

def priority_isp(oper):
    if oper == '*' or oper =="/":
        return 2
    elif oper == "+" or oper == "-":
        return 1
    elif oper =="(":
        return 0


def postfix_calculator(postfix):
    operand_stack=[]
    for i in postfix:
        if isnumber(i):
            operand_stack.append(i)
        else:
            operand1 = operand_stack.pop()
            operand2 = operand_stack.pop()
            value = calculate(i, operand1, operand2)
            operand_stack.append(value)

    return operand_stack.pop()

def calculate(operator, operand1, operand2):
    operand1 = int(operand1)
    operand2 = int(operand2)
    if operator == '/':
        return operand1 / operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    else :
        print('error at calculate method')


for tc in range(1, 11):
    n = int(input())
    infix = input()
    postfix = infix2postfix(n, infix)
    result = postfix_calculator(postfix)
    print("#%d %d"%(tc, result))