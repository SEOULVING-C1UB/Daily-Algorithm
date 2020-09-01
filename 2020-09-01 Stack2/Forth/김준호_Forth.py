import sys

sys.stdin = open("Forth_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    stack = []
    res = 0     # 계산값
    err = []    # 에러 상황에 에러를 담음
    command = list(input().split())

    for com in command:
        if com == '.':
            if len(stack) > 1:  # 끝인데 숫자가 하나가 아니라면(계산이 안된 숫자가 남았다면)
                err.append('error')
                break
            else:
                res = stack.pop()   # 정상 종료라면 누적된 값을 담기
                break
        elif com in ['+','-','*','/']: # 연산자가 나오면
            if len(stack) < 2:  # 연산을 해야하는데 숫자가 없거나 하나만 있다면
                err.append('error')
                break
            else:   # 숫자 두개 뽑고 연산, 나눗셈을 위해 미리 뽑아놓음. ex) 3 4 / => a = 4, b = 3              
                a, b = stack.pop(), stack.pop()
                if com == '+':
                    stack.append(b + a)
                elif com == '-':
                    stack.append(b - a)
                elif com == '*':
                    stack.append(b * a)
                elif com == '/':
                    stack.append(b // a)
        else:   # 숫자라면
            stack.append(int(com))

    # 에러 있으면 에러 출력, 없다면 계산값 출력
    if err:
        print('#{} {}'.format(test_case, err[0]))
    else:
        print('#{} {}'.format(test_case, res))