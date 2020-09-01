import sys
sys.stdin = open('Forth_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    # input이 띄워쓰기 단위로 구분되어 있으므로, split()을 사용하여 list로 받아냅니다.
    formula = list(input().split())
    # 계산을 위한 스택 선언
    stack = []
    answer = 0
    for token in formula:
        if token == '.':
            # stack에 다른 찌꺼기가 남았으면 에러처리
            if len(stack) > 1:
                answer = 'error'
            else:
                answer = stack.pop()
        elif token in '+-/*':
            # stack에 2개 이상의 number가 존재하지 않으면 에러처리
            if len(stack) < 2:
                answer = 'error'
                break
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                elif token == '/':
                    result = num1 // num2
                stack.append(str(result))
        else:
            stack.append(token)
    print("#{0} {1}".format(test_case, answer))

# 테스트 케이스 9/10 나오는 코드
# T = int(input())
# for test_case in range(1, T + 1):
#     # input이 띄워쓰기 단위로 구분되어 있으므로, split()을 사용하여 list로 받아냅니다.
#     formula = list(input().split())
#     # 계산을 위한 스택 선언
#     stack = []
#     answer = 0
#
#     for token in formula:
#         if token.isdigit():  # isdigit() 메서드를 이용하여 숫자인지 판별한다.
#             stack.append(token)
#         elif token in '+-/*':  # token이 연산자라면
#             if len(stack) != 0:
#                 num2 = int(stack.pop())
#             else:
#                 answer = 'error'
#                 break
#
#             if len(stack) != 0:
#                 num1 = int(stack.pop())
#             else:
#                 answer = 'error'
#                 break
#
#             if token == '+':
#                 result = num1 + num2
#             elif token == '-':
#                 result = num1 - num2
#             elif token == '*':
#                 result = num1 * num2
#             elif token == '/':
#                 result = num1 // num2
#             stack.append(str(result))
#         elif token == '.':
#             if stack:
#                 answer = stack.pop()
#                 break
#             else:
#                 answer = 'error'
#     # 예외 처리: 후위 표기식의 마지막이 연산자가 아니라면 에러처리
#     if formula[-2] not in '+-*/':
#         answer = 'error'
#     print('#{0} {1}'.format(test_case, answer))