import sys
sys.stdin = open('5174.txt')


#12 이제 traverse함수를 만듭니다.
def traverse(node):
    global cnt
    if node:
        #13 node로 이동할때마다 global cnt를 1늘려줍니다.
        cnt +=1
        #14 left child와 right child를 계속 traverse합니다.
        traverse(tree[node][0])
        traverse(tree[node][1])






total_tc = int(input())


for tc in range(1, total_tc+1):
    E, N = map(int, input().split())
    #1 E+1개=전체노드의갯수 만큼의 이차원행렬을 만들어둡니다. 값은 0으로 초기화해둡니다.
    #2 리스트안의 값은 차례대로 left child, right child, parent 로 설정하겠습니다.
    tree = [[0, 0, 0] for _ in range (E+2)]

    #3 인풋을 받아 parent child  관계를 tree에 입력해줍니다.
    input_list = list(map(int, input().split()))
    for i in range(E):
        #4 짝수번째는 parent, 홀수번째는 child로 설정해줍니다.
        parent = input_list[2*i]
        child = input_list[2*i+1]
        #5 left chld가 비어있다면 left child에 배정해주고 child의 리스트로 이동해 parent도 설정해줍니다.
        if tree[parent][0]==0:
            tree[parent][0] = child
            tree[child][2] = parent
        #6 left child가 찼다면 right child에 배정해줍니다.
        elif tree[parent][1]==0:
            tree[parent][1]=child
            tree[child][2] = parent
        #7 혹시 모를 decoding을 위해 else를 설정해줍니다. 잘돌아간다면 위의 elif대신에 else를 사용 할 수 있습니다.
        else:
            print("1번에서 에러")
    #8 print 해보니 여기까진 괜찮은거 같습니다.
    #9 print(tree)


    #10 이제 N값을 주면 subtree를 구해야 합니다.
    #11 global로 cnt 값을 주고 subtree를 traverse하면서 cnt+=1 을 해주는 함수를 만들면 될 것 같습니다.
    cnt = 0
    traverse(N)
    print("#%d %d"%(tc, cnt))



