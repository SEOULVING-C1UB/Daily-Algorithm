import sys
sys.stdin = open('input.txt', 'r')

T = 10


def find(node):
    if node:
        find(firstChild[node])      # 앞선 노드 탐색
        print(word[node], end='')   # 해당 단어 출력
        find(secondChild[node])     # 뒷 노드 탐색

for test_case in range(1, T + 1):
    n = int(input())
    word = [0] * (n+1)  # 노드에 해당하는 단어를 담을 리스트
    firstChild = [0] * (n+1)    # 노드의 왼쪽 자식이 누군지
    secondChild = [0] * (n+1)   # 노드의 오른쪽 자식이 누군지
    for i in range(n):
        temp = list(input().split())    # 임시로 인풋을 받고
        num = int(temp[0])              # 처음 값은 노드 번호
        word[num] = temp[1]             # 두번째 값은 그 노드의 단어
        if num * 2 <= n:                # 첫 자식이 있다면
            firstChild[num] = int(temp[2])  # 해당 노드의 첫 자식 
            if num * 2 + 1 <= n:        # 둘째 자식이 있다면
                secondChild[num] = int(temp[3]) # 해당 노드의 두번째 자식

    print('#{}'.format(test_case), end=' ')
    find(1)
    print()