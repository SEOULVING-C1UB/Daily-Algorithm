# node의 값에 대한 연산자 유무를 체크하기 위해 리스트를 생성시켜 줍니다.
# 향후 containment test를 통해 구분합니다.
operator = ['+', '-', '*', '/']
# node의 값이 연산자인 경우 연산 기능을 수행하는 함수입니다.
# return value가 있는 함수입니다.
def cal(op, n1, n2):
    result = 0
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    return result

for t in range(1,11):
    # 입력값
    N = int(input())                    # 노드의 수
    tree = [[0]*3 for _ in range(N+1)]  # 순회를 위한 tree 생성

    # tree 안 의 값 채우기
    for i in range(1,N+1):
        tmp = list(input().split())     # 주어지는 입력 길이가 모두 다르므로 우선 리스트를 받습니다.
        node = int(tmp[0])              # 0번쨰는 항상 node에 해당하므로 int로 바꿔줍니다.
        value = tmp[1]                  # 1번째는 node의 value에 해당하며, 연산자를 기본값으로 할당합니다.
        if value not in operator:       # 만약, 연산자가 아니라면
            value = int(tmp[1])         # value를 int로 형변환합니다.
        if len(tmp)>2:                  # lenth는 무조건 2,4로 주어질 것이기에 이렇게 해보았습니다. (아니면 계산이 안됨..)
            left = int(tmp[2])          # 4개가 주어진 경우 왼쪽, 오른쪽을 할당하여 int 형변환 하고
            right = int(tmp[3])
            tree[node][1] = value       # 각각 node를 기준으로 1번에는 value, 0은 left, 2는 right를 할당합니다.
            tree[node][0] = left
            tree[node][2] = right
        else:
            tree[node][1] = value
    # 드디어 트리 끝!
    # 이제 순회 시작!, 후위 순회법을 사용합니다.
    def postorder(n):
        # basis point입니다.
        if n > N or n==0: return    # n이 더 커지면 인덱스 error, n이 0인 경우는 없으므로 return 처리 합니다.
        else:
            # 우선 node에 대해 value, left, right를 따로 저장합니다.
            left = tree[n][0]
            right = tree[n][2]
            val = tree[n][1]
            # 후위 순회를 위해 left, right를 탐색한 후
            postorder(left)
            postorder(right)
            # basis point에서 걸리지 않으면 마지막 호출에 대해 계산을 시작합니다.
            if val in operator:     # 만약, val가 연산자라면 앞서 정의한 cal함수에 인자를 넣습니다.
                tree[n][1] = cal(val,tree[left][1],tree[right][1])
    # tree root = 1
    postorder(1)
    # tree[1][1]이 최종 결과 값이며, int로 자료형을 변한해야 합니다.
    print('#{} {}'.format(t,int(tree[1][1])))