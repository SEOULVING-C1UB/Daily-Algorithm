import sys
sys.stdin = open('중위순회_input.txt')

def in_order(node):
    if nodes[node][1]: # 좌 - 중간 - 우 순서
        in_order(nodes[node][1])
    print(nodes[node][0], end = '')
    if nodes[node][2]:
        in_order(nodes[node][2])


T = 10
for test_case in range(1, T + 1):
    n = int(input())
    nodes = [['.', 0, 0, 0] for _ in range(n+1)] # 노드의 값 ,왼쪽 자식, 오른쪽 자식, 부모 0이면 없다는 뜻
    for i in range(n): # 트리 만들기!!
        get_value = list(input().split())
        idx, value = int(get_value[0]), get_value[1]
        nodes[idx][0] = value
        try: # 자식 노드가 없을 수도 있으니 try - except로 버린다.
            left = int(get_value[2])
            nodes[idx][1] = left
            nodes[left][3] = idx
            right = int(get_value[3])
            nodes[idx][2] = right
            nodes[right][3] = idx
        except:
            pass

    print("#{0}" . format(test_case), end = ' ')
    in_order(1)
    print()