t = int(input())

for i in range(1, t+1):
    cmd = list(input().split())
    # 스택을 쌓을 공간
    stack = []
    # 연산자인지 숫자인지 비교하기 위해 만든 string
    yeon = "+*-/."

    for c in cmd:
        # 연산 식이 잘못되어 에러가나는 경우를 식별하기위해 try사용
        try:
            # 연산이 아니면 스택에 푸시
            if c not in yeon:
                stack.append(int(c))
            # 연산이면서 .이 아닌 경우의 연산
            elif c != ".":
                if c == "+":
                    ans = stack[-2] + stack[-1]
                elif c == "*":
                    ans = stack[-2] * stack[-1]
                elif c == "-":
                    ans = stack[-2] - stack[-1]
                elif c == "/":
                    ans = stack[-2] // stack[-1]
                # 위의 연산에서 생성된 값을 ans에 저장하고 스택의 마지막 주수를 뽑아낸 후 push
                stack.pop()
                stack.pop()
                stack.append(ans)
            # TC10개중에 하나가 틀리길래 뭔가하고 봤더니 .이 나올때 스택에 숫자가 하나만 있어야 되는거였다.
            # 그래서 스택에 원소가 2개 이상이면 오류가 나게 만들어 except문으로 빠지게 처리
            else:
                if len(stack) == 1:
                    print("#{} {}".format(i, stack[-1]))
                else:
                    # 오타아님. 일부러 오류내는거임.
                    st
        except:
            print('#{} error'.format(i))
            break