import sys
sys.stdin = open('forthinput.txt')


def postfix_calculator(postfix):
    operand_stack=[]
    try :
        for i in postfix:
            if i == '.':
                result = operand_stack.pop()
                if operand_stack:
                    return 'error'
                else:
                    return result

            elif i == '+':
                operand_stack.append(operand_stack.pop(-2) + operand_stack.pop())
            elif i == '-':
                operand_stack.append(operand_stack.pop(-2) - operand_stack.pop())
            elif i == '*':
                operand_stack.append(operand_stack.pop(-2) * operand_stack.pop())
            elif i == '/':
                operand_stack.append(int(operand_stack.pop(-2) / operand_stack.pop()))
            else:
                operand_stack.append(int(i))
    except:
        return 'error'





total_tc = int(input())

for tc in range(1, total_tc+1):
    postfix = list(input().split())
    result = postfix_calculator(postfix)
    print('#%d '%(tc)+ str(result))