import sys
sys.stdin = open('5176.txt')


def traverse(node):
    global number
    # node는 N개있으므로 N개까지 재귀한다.
    if node<N+1:
        #아래 두줄은 기본적인 tree에서 노드 번호 부여하는방법이다.
        #왼쪽에는 node*2
        tree[node][1] = node*2
        #오른쪽에는 node*2 +1 을 부여한다
        tree[node][2] = node*2 +1
        #모든 설정이끝나면 inorder 순서로 재귀해주자. 말단 리프에게도 차일드가 배정되는 버그가 있지만 이문제에선 상관없다.
        traverse(tree[node][1])
        number += 1
        tree[node][0] = number
        traverse(tree[node][2])


total_tc = int(input())
# total_tc = 1

for tc in range(1, total_tc + 1):
    N = int(input())
    # tree를 설정해줘야한다. 순서대로 value, leftchild, rightchild로 설정한다.
    tree= [[0, 0, 0] for _ in range (N+1)]
    # 트리의 형태가 inorder과 관련이 있어보인다. Inorder 순서대로 번호를 매긴다면 될것같다.
    # Inorder로 트리를 타고들어가 순서대로 번호를 매겨보자
    # global로 number를 만들어서 이걸 1씩 키워서 이걸 value에 할당해준다
    number = 0
    # traverse는 1번 node 부터 시작
    traverse(1)
    print("#%d %d %d"%(tc, tree[1][0], tree[N//2][0]))





    # 아래는 말단리프에 차일드가 배정되는 에러를 해결하기 위한 시도입니다.
    # 근데 실패했습니다ㅜ
    # def traverse(node):
    #     global number
    #     # node는 N개있으므로 N개까지 재귀한다.
    #     if node < N + 1:
    #         number += 1
    #         # 아래 두줄은 기본적인 tree에서 노드 번호 부여하는방법이다.
    #         if node * 2 + 1 <= N:
    #             # 왼쪽에는 node*2
    #             tree[node][1] = node * 2
    #             # 오른쪽에는 node*2 +1 을 부여한다
    #             tree[node][2] = node * 2 + 1
    #
    #             # 모든 설정이끝나면 inorder 순서로 재귀해주자.
    #             # 중요한점은 말단까지 갔을때 말단이면 child설정을 안해주고 값만 줘야된다는것이다.
    #             # 그러기 위해선 위와 똑같은 if조건을 써야되지만 값을 설정해주는건 말단도 해줘야되므로 if문에서 빼주도록 한다
    #             traverse(tree[node][1])
    #         tree[node][0] = number
    #         # 그래서 번거롭지만 이렇게 if문을 나눠줘야한다.
    #         if node * 2 + 1 <= N:
    #             traverse(tree[node][2])
