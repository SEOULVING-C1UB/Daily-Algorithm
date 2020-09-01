for t in range (1, 11) :
    # 우선순위 설정. isp의 0은 무의미한 값으로 제일 낮은 우선순위 설정.
    isp = {"0": -1, "*" : 2, "+" : 1, "(" : 0}
    icp = {"*" : 2, "+" : 1, "(" : 3}
    N = int(input())
    # 중위표기식으로 들어오는 input
    origin = list(input())
    # 후위표기식으로 바꿔 저장할 배열
    postfix = []
    # 원래 stack 비워뒀었는데, while icp[origin[i]] <= isp[stack[top]] : 하면서 오류나서 무의미한 값 넣어두고 시작
    stack = ["0"]
    top = 0
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(N) :
        # 피연산자라면 postfix에 바로 추가
        if origin[i] in numbers : 
            postfix.append(int(origin[i]))
        # 연산자라면
        else :
            # 닫는 괄호일 때는 stack에서 여는 괄호가 나올 때까지 pop해서 postfix에 추가
            if origin[i] == ")" :
                while stack[top] != "(" :
                    operator = stack.pop()
                    top -=1
                    postfix.append(operator)
                # 여는 괄호 빼주기
                stack.pop()
                top -=1
            # 그 외의 경우에는
            else :
                # 넣는 연산자의 우선순위가 stack의 top의 우선순위보다 높아질 때까지 pop해서 postfix에 추가하다가
                while icp[origin[i]] <= isp[stack[top]] :
                    operator = stack.pop()
                    top -=1
                    postfix.append(operator)
                # stack에 push
                stack.append(origin[i])
                top +=1

    # 피연산자 저장할 list 
    operand = []
    flag = True
    # postfix를 순회하며 연산수행
    for i in range(len(postfix)) :
        if postfix[i] in ["+", "*"] :
            b = operand.pop()
            a = operand.pop()
            if postfix[i] == "+" :
                operand.append(a+b)
            elif postfix[i] == "*" :
                operand.append(a*b)
        else :
            operand.append(postfix[i])
    print('#{} {}' .format(t, operand[0]))