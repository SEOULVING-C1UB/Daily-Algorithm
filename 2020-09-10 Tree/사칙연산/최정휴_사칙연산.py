'''
<문제풀이>
: 후위순회를 이용해 연산을 시행한다.
1) 각 노드에 해당하는 인풋을 담을 리스트를 이차원배열로 생성한다.
2) 인풋의 첫번째 인자가 노드 번호이므로 해당 번호의 노드에 뒤따라오는 인풋을 넣는다.
    ex) 1 - 2 3 인 경우 1번 노드에 [-, 2, 3]을 저장
3) 해당 노드에 저장된 결과가 길이 1 인 리스트이면 말단 노드이므로 아무것도 하지않고
4) 그렇지 않은 경우 왼쪽 자식 노드를 확인하여 0번 값이 연산자이면 재귀호출
5) 오른쪽 자식노드에도 같은 방식으로 수행
6) 재귀 호출이 끝나면 자식노드에 대해 연산 수행하여 현재노드에 리스트로 저장

<추가사항>
1) 완전이진트리가 아니므로 인덱스 설정에 주의
2) 결과값낼때 소숫점이하 버림은 int로 해결하면됨
'''


def sachick(v):                                     # 후위 순회 할 재귀함수
    if len(nodes[v]) != 1:                          # 노드의 커멘드길이가 1이 아니면. 즉, 말단노드가 아니면
        if nodes[int(nodes[v][1])][0] in "+-*/":    # 왼쪽자식이 연산자이면 재귀호출
            sachick(int(nodes[v][1]))
        if nodes[int(nodes[v][2])][0] in "+-*/":    # 오른쪽자식이 연산자이면 재귀호출
            sachick(int(nodes[v][2]))
        nodes[v] = [yeon(nodes[int(nodes[v][1])][0], nodes[int(nodes[v][2])][0], nodes[v][0])]
                                                    # 재귀호출 끝난 후 왼쪽 자식과 오른쪽 자식 연산한 결과를 리스트로 저장
def yeon(a, b, c):                                  # 연산 함수
    if c == "+":
        return int(a) + int(b)
    elif c == "-":
        return int(a) - int(b)
    elif c == "*":
        return int(a) * int(b)
    else:
        return int(a) / int(b)

for i in range(1, 11):
    n = int(input())
    nodes = [[] for _ in range(n+1)]
    for j in range(n):
        cmd = list(input().split())
        nodes[int(cmd[0])] = cmd[1:]                # 인풋의 주소에 커멘드 저장
    sachick(1)
    print('#{} {}'.format(i, int(nodes[1][0])))