import sys
sys.stdin = open("Forth_input.txt", "r")

tc = int(input())

priority = {'.':3, '*': 2, '/': 2, '+': 1, '-': 1, '(':0, ')':0 } # 연산자 우선순위를 위한 딕셔너리

def calculator(arr) :
    numbers = []        # 피연산자를 담을 공간
    for i in range(len(arr)-1) :
        if arr[i] not in priority :     # 배열에서 들어온 값이 우선순위에 없다 -> 피연산자
            numbers.append(int(arr[i])) # 피연산자 배열에 넣는다.
        else :                          # 연산자일 경우에
            if len(numbers) < 2:        # 피연산자가 2개 미만이면 에러
                return "error"
            else :                      # 피연산자 2개 이상이면 연산 가능
                num2 = numbers.pop()    # 차례대로 피연산자 꺼낸다. 2개
                num1 = numbers.pop()
                if arr[i] == '*':       # 연산자 대로 계산 후 계산 결과값을 스택에 넣는다.
                    temp = num1 * num2
                    numbers.append(temp)
                elif arr[i] == '/':
                    temp = num1 // num2
                    numbers.append(temp)
                elif arr[i] == '+':
                    temp = num1 + num2
                    numbers.append(temp)
                elif arr[i] == '-':
                    temp = num1 - num2
                    numbers.append(temp)
                elif arr[i] == '.':
                    return numbers[-1]
    if len(numbers) > 1:            # 식을 다 끝냈는데 숫자가 2개 이상 남아있으면 에러
        return "error"
    else :                          # 에러가 아니면 제일 마지막 값(결과값 출력)
        return numbers[-1]


for t in range(tc) :
    express = list(input().split())

    result = calculator(express)
    print("#{} {}".format(t+1, result))