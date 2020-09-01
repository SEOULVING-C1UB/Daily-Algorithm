import sys
sys.stdin = open("(4874)Forth_input.txt")

T = int(input())
for t in range(T):
    temp = list(map(str, input().split()))
    # 피연산자를 담아둘 list
    operand = []
    # error 여부를 판단할 flag
    flag = True
    for i in range(len(temp)):
        # 만약 연산자이고
        if temp[i] in ["+", "-", "*", "/"]:
            # 연산할 피연산자도 충분하다면
            if len(operand) >= 2:
                # 두 개의 피연산자를 pop해서 a, b에 넣고
                b = operand.pop()
                a = operand.pop()
                # 연산을 수행한다.
                if temp[i] == "+":
                    operand.append(a + b)
                elif temp[i] == "*":
                    operand.append(a * b)
                elif temp[i] == "-":
                    operand.append(a - b)
                else:
                    operand.append(a // b)
            # 연산할 피연산자가 충분하지 않다면 오류가 났음을 표시
            else:
                flag = False
        # 만약 출력하라는 표시가 나오면
        elif temp[i] == ".":
            # 오류가 난 적 없고, 피연산자 list에 결과값만 남았다면
            if flag and len(operand) == 1:
                # 출력
                print('#{} {}'.format(t + 1, operand[0]))
            # 그 외의 경우에는 error 출력
            else:
                print('#{} error'.format(t + 1))
        # 만약 피연산자라면, 피연산자 배열에 추가
        elif temp[i] not in ["+", "-", "*", "/", "."]:
            operand.append(int(temp[i]))
