import sys
sys.stdin = open("Forth_input.txt")

def calculate(A, operator, B):
    a = int(A)
    b = int(B)
    
    if operator == '+':
        return a + b
    elif operator == '-':   #빼는 거랑 나누는건 스택 순서 상 앞에 숫자에서 뒤에숫자를 연산해야하니까 순서 바꾸기
        return b - a
    elif operator == '/':   #나누기 / <- 얘는 float결과가 나오니 정수가 나오는 //으로
        return b // a
    elif operator == '*':
        return a * b

T = int(input())

for tc in range(1, T + 1):

    equation = list(map(str, input().split()))  # input 연산코드

    stack = []  # 숫자를 담을 스택
    error = 0   # error 탐지용 변수

    for i in range(len(equation)):

        current = equation[i]   # 현재값 담는 변수(equation[i] 일일이 치기 귀찮아서..)

        # 만약 현재 값이 숫자라면 스택에 추가
        if current.isdigit():
            stack.append(current)

        # 일반 연산자일때는 계산 후 스택에 추가
        elif current in '+-/*':

            # 계산 불가한 경우(list out of range 등)는 에러 변수 증가시키기
            if len(stack)<2:
                error += 1
                break

            else:
                A = stack.pop()
                B = stack.pop()
                stack.append(calculate(A, current, B))

        #마침표
        else:
            if len(stack) > 1:  #마침표 나왔는데도 뭐가 있다? = 뭔가 잘못됐다
                error += 1
                break

    if error > 0:
        print('#{} error'.format(tc))
    else:
        print('#{} {}'.format(tc, stack[0]))


