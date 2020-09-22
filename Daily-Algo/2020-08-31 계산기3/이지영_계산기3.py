# 일반 식을 후위 표기법으로 변환 후 결과를 출력하자!
# 0 ~ 9 only
# +, * 두개만 + 괄호 가능
# TC 10개
'''
11
3+(4+5)*6+7
345+6*7+
'''
for tc in range(1, 11):

    N = int(input())  # TC 길이
    equation = input()  # 일반 식 받기
    # N = len(equation)

    #우선순위: * > + > (    => 이걸....ㅠ이렇게 풀어야하는지 몰랐다 개고생쩔었음!
    priority = {
        '*': 3,
        '+': 2,
        '(': 1
    }

    # 후위 표기법을 담을 changedEq, 연산자를 담을 operators
    changedEq = []
    operators = []

    for i in range(N):
        current = equation[i]

        #숫자는 결과에 바로 넣기
        if current.isdigit():
            changedEq.append(current)

        # (는 push
        elif current == '(':
            operators.append(current)

        # )는 (나올때까지 pop
        elif current == ')':
            while operators:
                # (는 최종 결과에 포함되면 안되니까 ( 아닌애들만 pop해서 후위표기법에 넣어줌
                if operators[-1] != '(':
                    changedEq.append(operators.pop())
                else:
                    operators.pop()
                    break

        # 나머지 연산자는 먼저 스택 비었는지부터 확인
        else:
            if not operators:
                operators.append(current)

            else:
                # 이제 우선순위를 비교해서 지금 들어오는 연산자의 우선순위가 top에 있는 것보다 크면 그냥 push
                if priority.get(operators[-1]) < priority.get(current):
                    operators.append(current)
                
                # 그게 아니라면 나보다 같거나 큰 놈들은 다 pop해버린다
                else:
                    while operators and priority.get(operators[-1]) >= priority.get(current):
                        # result += stack.pop()
                        changedEq.append(operators.pop())

                    operators.append(current)   #같거나 큰게 없으면 이제 push

    # 다 끝나고 남은 연산자는 후위표기법의 맨 뒤에 쭈루룩 붙여준다
    while operators:
        changedEq.append(operators.pop())

    # 계산용 리스트
    calculate = []

    for i in changedEq:
        if i == '+':
            calculate.append(calculate.pop() + calculate.pop())
        elif i == '*':
            calculate.append(calculate.pop() * calculate.pop())
        else:
            calculate.append(int(i))    #현재 표기식은 str이니까 계산하기 쉽게 계산리스트에 숫자로 바꿔서 넣어줌

    print('#{} {}'.format(tc, calculate[0]))