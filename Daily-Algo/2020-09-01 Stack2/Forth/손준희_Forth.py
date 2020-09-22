import sys
sys.stdin = open('Forth_input.txt', 'r')

def calcul(test_str):
    stack = []
    for ch in test_str:
        if ch.isdigit():        # 숫자면
            stack.append(ch)    # 추가
        elif ch == '+' or ch == '-' or ch == '*' or ch == '/':  # 연산자면
            if len(stack) > 1:  # 스택에 둘 이상 있을 때만
                ch1 = stack.pop()
                ch2 = stack.pop()
                stack.append(str(int(eval(ch2+ch+ch1))))    # 계산하고 추가
            else:
                return 'error'  # 아니면 에러
        else:
            if len(stack) == 1:     # 암것도 아닌데(.인데) 1개 남았으면
                return stack.pop()  # 답이므로 정답
            else:                   # 여러 개 남았으면 연산자 부족으로
                return 'error'      # 계산 안 된 것이므로 에러

testcase = int(input())
for i in range(testcase):
    test_str = input().split()
    print('#{} {}' .format(i+1, calcul(test_str)))


# def digit_to_int(test_str):
#     for ch in test_str:
#         if ch.isdigit():
#             test_str[test_str.index(ch)] = int(ch)
#
# def calcul_str(test_str):
#     j = 0
#     while test_str[j] != '.':
#         if test_str[j] == '+':
#             if j > 1 and type(test_str[j-2]) is int and type(test_str[j-2]) is int:
#                 test_str[j-2] = test_str[j-2] + test_str[j-1]
#                 test_str.pop(j-1)
#                 test_str.pop(j-1)
#                 j -= 2
#             else:
#                 return ['error']
#         elif test_str[j] == '*':
#             if j > 1 and type(test_str[j-2]) is int and type(test_str[j-2]) is int:
#                 test_str[j-2] = test_str[j-2] * test_str[j-1]
#                 test_str.pop(j-1)
#                 test_str.pop(j-1)
#                 j -= 2
#             else:
#                 return ['error']
#         elif test_str[j] == '-':
#             if j > 1 and type(test_str[j-2]) is int and type(test_str[j-2]) is int:
#                 test_str[j-2] = test_str[j-2] - test_str[j-1]
#                 test_str.pop(j-1)
#                 test_str.pop(j-1)
#                 j -= 2
#             else:
#                 return ['error']
#         elif test_str[j] == '/':
#             if j > 1 and type(test_str[j-2]) is int and type(test_str[j-2]) is int:
#                 test_str[j-2] = test_str[j-2] // test_str[j-1]
#                 test_str.pop(j-1)
#                 test_str.pop(j-1)
#                 j -= 2
#             else:
#                 return ['error']
#         else:
#             j += 1
#     if len(test_str) == 2 and type(test_str[0]) is int:
#         return test_str
#     else:
#         return ['error']
#
# testcase = int(input())
# for i in range(testcase):
#     test_str = input().split()
#     digit_to_int(test_str)
#     print('#{} {}' .format(i+1, calcul_str(test_str)[0]))
