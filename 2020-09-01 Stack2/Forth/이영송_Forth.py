import sys; sys.stdin = open('Forth_input.txt')
T = int(input())

# 계산 기능을 함수로 구현헀습니다.
# 문자열로 취급된 연산자를 연산하는 방법을 찾지 못해 조건을 할당하였습니다.
def operate(char, forward, back):
    if char == '+':
        value = forward + back
    elif char == '-':
        value = forward - back
    elif char == '*':
        value = forward * back
    elif char == '/':
        value = forward / back
    return value


for t in range(1,T+1):
    data = list(input().split())

    stack = []
    operator = ['+','/','*','-']
    # 연산자 리스트를 만들어 입력값을 숫자/연산자로 구분했습니다.
    for datum in data:
        # '.'은 리스트의 마지막에 해당하므로 stack에 어떤 값이 남아있느냐에 따라 결과 처리를 해주었습니다.
        if datum == '.':
            # 만약, 모든 입력을 처리한 후 stack에 값이 남아있는데 그것이 연산자라면 error이고
            if len(stack) == 1:
                result = stack.pop()
                if result in operator:
                    result = 'error'
            # 만약, 모든 입력을 처리하고 남아있는 값이 없다면 그것도 error입니다.
            else:
                result = 'error'
                break
        # 숫자는 모두 int로 바꾸어 stack에 append했습니다.
        elif datum not in operator:
            stack.append(int(datum))
        # 연산자를 꺼낼 때도 두 가지 case를 나누었습니다.
        elif datum in operator:
            # 연산자를 만났을 때 stack에 숫자가 두 개 이상 있는 경우에만 앞서 정의한 함수를 실행합니다.
            if len(stack) >=2:
                back = stack.pop()
                forward = stack.pop()
                total = operate(datum, forward, back)
                stack.append(int(total))
            # 연산자를 만났는데 stack에 숫자가 두 개 이상 없는 경우면 error입니다.
            else:
                result = 'error'
                break
    print('#{} {}'.format(t,result))
