'''
[컨셉]
1) 입력 받아서 트리에 저장
   - 처음에 map(str, ...)로 받아오고, 2번째 값이 연산자/피연산자일 때 분리해서 처리. 수는 전부 int형으로 변환.
2) 루트 노드에서 시작해서, 재귀함수 cal로 연산해서 반환
   - 연산자가 아니라면 return, 연산자라면 자식들로 연산한 값 저장해서 return
'''

operators = ['+', '-', '*', '/']
def cal(k) :
    if T[k][0] not in operators :                       # 피연산자라면, return
        return T[k][0]
    else :                                              # 연산자라면
        op, left, right = T[k][0], T[k][1], T[k][2]     # 연산자, 왼쪽 자식 idx, 오른쪽 자식 idx
        # 각 연산자에 맞게 연산 수행
        if op == '+' :
            T[k][0] = cal(left) + cal(right)
        elif op == '-' :
            T[k][0] = cal(left) - cal(right)
        elif op == '*' :
            T[k][0] = cal(left) * cal(right)
        elif op == '/' :
            T[k][0] = cal(left) / cal(right)
        # 계산한 값 return
        return T[k][0]
            

for tc in range(1, 11) :
    N = int(input())
    T = [[] for _ in range(N+1)]                # tree
    for n in range(N) :
        temp = list(map(str, input().split()))
        idx = int(temp[0])                      # idx : 몇 번 노드인지
        if temp[1] in operators :               # 연산자라면,
            T[idx].append(temp[1])
            T[idx].append(int(temp[2]))
            T[idx].append(int(temp[3]))
        else :                                  # 연산자가 아니라면 (피연산자라면)
            T[idx].append(int(temp[1]))
    result = int(cal(1))                        # 루트 노드로 시작. int는 정수부만 남기기 위해.
    print('#{} {}' .format(tc, result))