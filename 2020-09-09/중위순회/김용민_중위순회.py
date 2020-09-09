import sys
sys.stdin = open("중위순회.txt")

def inorder(node):
    global ans                  # 답
    if node:                    # 노드가 0이 아니라면(값이 있다면)
        inorder(tree[node][0])  # 현재 노드에서 왼쪽자식노드 기준으로 재귀호출
        ans += tree[node][2]    # 중위순회
        inorder(tree[node][1])  # 현재 노드에서 오른쪽자식노드 기준으로 재귀호출

T = 10

for t in range(1, T+1):
    N = int(input())
    ans = ""                                # 답 초기화
    tree = [[0] * 3 for _ in range(N+1)]    # 트리 초기화
    for i in range(1, N+1):                 # N번 만큼씩 반복하며 한줄씩 입력 받음
        tmp = list(input().split())         # 한줄 입력 받아서
        if len(tmp) == 4:                   # 그 길이가 4이면
            tree[i][0] = int(tmp[2])        # i번째 트리의 0번 인덱스에 tmp의 2번 인덱스 값(왼쪽자식노드 값)입력
            tree[i][1] = int(tmp[3])        # i번째 트리의 1번 인덱스에 tmp의 3번 인덱스 값(오른쪽자식노드 값)입력
            tree[i][2] = tmp[1]             # i번째 트리의 2번 인덱스에 tmp의 1번 인덱스 값(알파벳)입력
        elif len(tmp) == 3:                 # 그 길이가 3이면
            tree[i][0] = int(tmp[2])        # i번째 트리의 0번 인덱스에 tmp의 2번 인덱스 값(왼쪽자식노드 값)입력
            tree[i][2] = tmp[1]             # i번째 트리의 2번 인덱스에 tmp의 1번 인덱스 값(알파벳)입력
        else:                               # 그 길이가 2이면
            tree[i][2] = tmp[1]             # i번째 트리의 2번 인덱스에 tmp의 1번 인덱스 값(알파벳)입력

    """
    최종트리 모습
    ex)
    [[0,  0,  0 ]
     [2,  3, 'W']
     [4,  5, 'F']
     [6,  7, 'R']
     [8,  0, 'O']
     [0,  0, 'T']
     [0,  0, 'A']
     [0,  0, 'E']
     [0,  0, 'S']
    """
    inorder(1)                          # 함수실행
    print("#{} {}".format(t, ans))      # 답 출력