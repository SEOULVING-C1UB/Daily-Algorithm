import sys
sys.stdin = open('input.txt', 'r')

T = 10


def cal(node):
    if node:
        if v[node].isdecimal(): # 숫자라면 값 반환
            return int(v[node])
        else:                   # 연산자라면 자식노드로 해당 연산 수행(각 값은 자식노드로 재귀함수 실행)
            if v[node] == '+':
                return cal(firstChild[node]) + cal(secondChild[node])
            elif v[node] == '-':
                return cal(firstChild[node]) - cal(secondChild[node])
            elif v[node] == '*':
                return cal(firstChild[node]) * cal(secondChild[node])
            elif v[node] == '/':
                return cal(firstChild[node]) / cal(secondChild[node])

for test_case in range(1, T + 1):
    n = int(input())
    v = [0] * (n+1)
    firstChild = [0] * (n+1)
    secondChild = [0] * (n+1)
    for i in range(n):
        temp = list(input().split())
        num = int(temp[0])  # 노드 번호
        # 노드에 해당하는 값 추가
        v[num] = temp[1]
        if not v[num].isdecimal():  # 연산자라면 자식 노드 번호 부여
            firstChild[num] = int(temp[2])
            secondChild[num] = int(temp[3])

    print('#{} {}'.format(test_case, int(cal(1))))