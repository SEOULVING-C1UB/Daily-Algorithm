import sys
sys.stdin = open('4874_input.txt', 'r')

op = ['+', '-', '*', '/']

def cal():
    numbers = []
    for i in range(len(inp)):
        if inp[i] not in op and inp[i] != '.':      # inp[i]가 정수이면 리스트에 append 해준다
            numbers.append(int(inp[i]))
        elif inp[i] in op:                          # 연산자이면 n2, n1 순서로 pop을 해준다
            try:                                    # 하지만 연산자가 남아있지만 len(numbers)==1일
                n2 = numbers.pop()                  # 경우 에러가 뜨면서 함수는 끝나고 'error'을 리턴한다
                n1 = numbers.pop()
            except:
                return 'error'
            if inp[i] == '+':                       # 위에서 n2,n1에 정수가 저장되면 해당하는 연산을 하고 다시 리스트에 append 한다
                temp = n1 + n2
            elif inp[i] == '-':
                temp = n1 - n2
            elif inp[i] == '*':
                temp = n1 * n2
            elif inp[i] == '/':
                temp = n1 // n2
            numbers.append(temp)
    if len(numbers) > 1:                            # 만약 정수의 개수가 2이상인데 남은 연산자가 없어도 'error'을 리턴한다
        return 'error'
    else:
        return numbers[0]                           # 위 에러에 해당사항이 없다면 number의 0번 인덱스를 리턴한다

for c in range(int(input())):
    inp = input().split()
    print('#{} {}'.format(c+1, cal()))