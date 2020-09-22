'''
[컨셉]
코드 1) 리스트의 N번 index에, N번 노드의 값, 왼쪽 자식, 오른쪽 자식을 넣는 방법
       - 만약 자식이 없어 비어있는 경우, 0을 채워줌.
코드 2) 완전 이진 트리임을 고려하여, 리스트의 N번 index에 N번 노드의 값만 저장하는 경우
       - inorder traversal을 진행할 때, 왼쪽 자식, 오른쪽 자식의 index를 계산.
* 2번이 실행시간도, 코드도 더 짧음
'''

# 코드 1
def inorder(x) :                                # 중위 순회
    if x :                                      # x가 0이 아니라면
        inorder(T[x][1])                        # 왼쪽 자식
        print(T[x][0], end='')
        inorder(T[x][2])                        # 오른쪽 자식
 
for t in range(1, 11) :
    N = int(input())
    T = [[] for _ in range (N+1)]               # tree
    for i in range(1, N+1) :                    
        temp = list(map(str, input().split()))  # temp에 담아두고
        if len(temp) < 4 :                      # 자식이 없어 길이가 4가 안되면, 부족한만큼 0을 채운다.
            for k in range(4-len(temp)) :
                temp.append(0)
        T[i].append(temp[1])                    # idx에 맞는 자리에 값 채우기
        T[i].append(int(temp[2]))               # 왼쪽 자식 채우기
        T[i].append(int(temp[3]))               # 오른쪽 자식 채우기
    print('#{} ' .format(t), end='')
    inorder(1)                                  # 루트 노드부터 중위순회
    print()


# 코드 2
def inorder(x) :                                # 중위 순회
    if x <=N :                                  # x가 N이하여야 존재하는 노드임
        inorder(x*2)                            # 왼쪽 자식
        print(T[x], end='')
        inorder(x*2 +1)                         # 오른쪽 자식
 
for t in range(1, 11) :
    N = int(input())
    T = [0]                                     # tree
    for i in range(1, N+1) :
        T.append(list(map(str, input().split()))[1])  # N번째 값만 넣어두기  
    print('#{} ' .format(t), end='')
    inorder(1)                                  # 루트 노드부터 중위순회
    print()
