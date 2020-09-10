import sys
sys.stdin = open('test_input.txt', 'r')


def change():
    for i in range(N):
        if eqn[i] not in tokrank:               # 기호가 아닌 정수들은 정수스택에 append 해준다
            stackN.append(int(eqn[i]))
        elif eqn[i] == '(':                     # '('가 나오면 기호스택에 append 해준다
            stackO.append(eqn[i])
        elif eqn[i] == ')':                     # ')'가 나오면 다음 행동을 해준다
            while True:
                if stackO[-1] == '(':           # '('가 나올때까지 기호스택의 마지막 항목을 pop 해서
                    stackO.pop()                # 정수스택에 append 해준다
                    break                       # '('가 나오면 마지막으로 '('를 pop해주고 와일문이 끝난다
                else:
                    temp = stackO.pop()
                    stackN.append(temp)
        else:                                   # 연산자가 나오면 다음 행동을 해준다
            if stackO == []:                    # 만약 기호스택이 비어있으면
                stackO.append(eqn[i])           # 해당 연산자를 기호스택에 append 해준다
            else:
                if tokrank[eqn[i]] > tokrank[stackO[-1]]:   # 만약에 현재 연산자가 기호스택의 마지막항목에 있는 연산자보다 우선순위가 높으면
                    stackO.append(eqn[i])                   # 기호스택에 append 해준다
                else:
                    temp = stackO.pop()                     # 높지 않으면, 기호스택의 마지막 항목을 pop 해서 정수스택에 append 해주고
                    stackN.append(temp)                     # 현재 연산자를 기호스택에 append 해준다
                    stackO.append(eqn[i])

def cal(stack):
    temp = 0
    result = []
    for i in range(len(stack)):
        if type(stack[i]) is int:           # stack[i]가 정수면 새로 정의한 리스트에 append 한다
            result.append(stack[i])
        else:                               # 연산자가 나오면 다음 행동을 해준다
            n2 = result.pop()               # 처음 pop 하는 숫자를 n2로 다음 pop 하는 숫자를 n1에 저장한다
            n1 = result.pop()
            if stack[i] == '+':             # 해당 연산자에 따라 다음 연산을 해준다
                temp = n1 + n2
            elif stack[i] == '-':
                temp = n1 - n2
            elif stack[i] == '*':
                temp = n1 * n2
            elif stack[i] == '/':
                temp = n1 // n2
            result.append(temp)             # 연산 결과를 다시 새로 정의한 리스트에 append 한다
    return result[0]                        # result 리스트에 마지막으로 남은 인자를 return 한다



for c in range(1):
    N = int(input())
    inp = input().split()
    eqn = inp[0]
    tokrank = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}            # 연산자 우선순위
    stackO = []                     # 괄호, 연산자가 들어갈 기호스택
    stackN = []                     # 정수가 들어갈 정수스택
    change()                        # 스택에 저장을 해준다
    print('#{} {}'.format(c+1, cal(stackN)))    # 저장된 스택을 활용하여 계산을 해준다
