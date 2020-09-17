import sys
sys.stdin = open('pmmd_input.txt', 'r')


def cal_root(i):    # i 노드의 값을 재귀로 불러오는 함수
    if tree[i][1] == '+' or tree[i][1] == '-' or tree[i][1] == '*' or tree[i][1] == '/':
        return str(int(eval(cal_root(int(tree[i][2])) + tree[i][1] + cal_root(int(tree[i][3])))))
    else:       # i 노드에 저장된 값이 숫자면 그대로 반환
        return tree[i][1]


for TC in range(10):
    N = int(input())
    tree = [0] + [input().split() for i in range(N)]
    print('#{} {}' .format(TC+1, cal_root(1)))