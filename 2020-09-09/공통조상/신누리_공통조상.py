'''
[컨셉]
1) 3*V 배열에 입력을 받아와 저장한다. V[idx]에는 차례로 child1, child2, parent의 정보가 담긴다.
2) A에 대해 부모 노드를 저장해 리스트 parents에 담는다.
3) B에 대해 부모 노드를 하나씩 확인해가면서, parents와 공통이면 common이라는 변수에 담는다.
   - 2, 3에서 확인 과정은 루트 노드가 아닌 동안 반복된다. 따라서, 3에서 만약 common이 정해지지 않았다면 common은 1이다.
4) common에서 traversal을 하며 subtree의 노드의 개수를 세서 cnt에 저장한다.
   - 만약 common == 1이라면, cnt는 모든 노드의 개수와 같으니 불필요한 순회를 생략한다.
'''

# 순회 (preorder traversal)
def preorder(k) :
    global cnt
    if k :
        cnt +=1
        preorder(T[k][0])
        preorder(T[k][1])


TC = int(input())
for tc in range(TC) :
    # 입력 받기
    V, E, A, B = map(int, input().split())
    temp = list(map(int, input().split()))
    
    # 1) 3*V 배열에 입력을 받아와 저장한다. V[idx]에는 차례로 child1, child2, parent의 정보가 담긴다.
    T = [[0]*3 for _ in range(V+1)]
    for e in range(E) :
        p, c = temp[2*e], temp[2*e+1]     # 부모, 자식의 idx 각각 저장
        if not T[p][0]  :                 # child1이 없다면, 0번째에 저장
            T[p][0] = c
        else :                            # child1이 있다면, 1번째에 저장
            T[p][1] = c
        T[c][2] = p                       # 자식 기준으로 부모 저장

   # 2) A에 대해 부모 노드를 저장해 리스트 parents에 담는다.
    parents =[1]                          # 루트 노드인 1은 무조건 부모 노드에 포함된다.
    parent = T[A][2]                      # A 기준으로 부모 노드 찾기
    while parent != 1 :                   # 루트 노드가 아닌 동안 부모 노드 찾아서 추가.
        parents.append(parent)
        parent = T[parent][2]

   # 3) B에 대해 부모 노드를 하나씩 확인해가면서, parents와 공통이면 common이라는 변수에 담는다.     
    common = 1                            # 공통된 노드를 담을 공간. B의 루트가 아닌 모든 부모 노드를 찾아도 없다면, 1이 공통이다.
    parent = T[B][2]                      # B 기준으로 부모 노드 찾기
    while parent != 1 :                   # 루트 노드가 아닌 동안 부모 노드 찾아서 비교
        if parent in parents :
            common = parent
            break                         # 가장 작은 subtree를 찾아야 하기에 break.
        parent = T[parent][2]

   # 4) common에서 traversal을 하며 subtree의 노드의 개수를 세서 cnt에 저장한다.     
    cnt = 0
    if common == 1 :                      # cnt는 모든 노드의 개수와 같으니, 순회 생략
        cnt = V
    else :                                # 순회하며 subtree의 노드 개수 count.
        preorder(common)
    print('#{} {} {}' .format(tc+1, common, cnt))
    