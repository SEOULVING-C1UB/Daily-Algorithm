import sys
sys.stdin = open("Forth.txt")

T = int(input())

for t in range(1, T + 1):
    data = input().split()
    num_stack = []
    error = 0

    for d in range(len(data)-1):

        if data[d].isdigit():
            num_stack.append(data[d])

        else:
            try:
                num2 = int(num_stack.pop())
                num1 = int(num_stack.pop())
                if data[d] == "+":
                    num_stack.append(str(num1 + num2))
                elif data[d] == "-":
                    num_stack.append(str(num1 - num2))
                elif data[d] == "*":
                    num_stack.append(str(num1 * num2))
                elif data[d] == "/":
                    num_stack.append(str(num1 // num2))

            except:
                error = -1

    if error == 0 and len(num_stack) == 1:
        print("#{} {}".format(t, num_stack[0]))
    elif error == -1 or len(num_stack) > 1:
        print("#{} error".format(t))

# 왜안되는거야빡치넹
# T = int(input())
#
# for t in range(1, T+1):
#     data = input().split()
#     num_stack = []
#
#     for d in data:
#         # 숫자
#         if d != "+" and d != "-" and d != "*" and d != "/" and d != ".":
#             num_stack.append(int(d))
#         # 마침표
#         elif d == ".":
#             break
#         # 연산자
#         elif d == "+" or d == "-" or d == "*" or d == "/":
#             # 길이가 2이상
#             if len(num_stack) >= 2:
#                 num2 = int(num_stack.pop())
#                 num1 = int(num_stack.pop())
#                 if d == "+":
#                     num_stack.append(num1 + num2)
#                 if d == "-":
#                     num_stack.append(num1 - num2)
#                 if d == "*":
#                     num_stack.append(num1 * num2)
#                 if d == "/":
#                     num_stack.append(num1 / num2)
#             # 길이가 1이하
#             else:
#                 num_stack.append(d)
#                 break
#     if len(num_stack) >= 2 or len(num_stack) == 0:
#         print("#{} error".format(t))
#     if len(num_stack) == 1:
#         print("#{} {}".format(t, num_stack[0]))