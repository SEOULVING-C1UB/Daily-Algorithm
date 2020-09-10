
ops = ['+', '-', '*', '/']

def postorder(node):        # 중위연산으로 처리
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        value = tree[node][2]
        if value in ops :           # 만약 value 값이 연산자면
            second = num_list.pop() # 스택에 저장되어있는 애들을 꺼내서
            first = num_list.pop()
            num_list.append(calculator(first, second, value))   # 연산 실행 후 num_list에 넣는다. 
        else :
            num_list.append(int(value))


def calculator(first, second, value) :  # 연산 함수
    if value == ops[0] :
        result = first + second
    elif value == ops[1] :
        result = first - second
    elif value == ops[2] :
        result = first * second
    elif value == ops[3] :
        result = first // second
    return result

for tc in range(1, 11) :
    V = int(input())
    tree = [[0]*3 for _ in range(V+1)]
    for i in range(1, V+1) :
        temp = list(input().split())
        tree[i][2] = temp[1]
        if len(temp) == 4 :
            tree[i][0] = int(temp[2])
            tree[i][1] = int(temp[3])
    num_list = []
    postorder(1)

    print("#{} {}".format(tc, num_list[0] ))