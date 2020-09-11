def asd(node):
    global cnt
    if node != 0:
        asd(board[node][0]) # 왼쪽
        cnt += 1
        asd(board[node][1]) # 오른쪽


def par(v):
    global par_list
    if v != 1:
        par_list += [board[v][2]]
        par(board[v][2])


T = int(input())

for tc in range(1,1+T):
    v,e,i,j = map(int,input().split())
    index = list(map(int,input().split()))
    board = [[0]*3 for _ in range(v+1)]
    for q in range(len(index)):
        if q%2 == 0:
            if board[index[q]][0] == 0:
                board[index[q]][0] = index[q+1]
                board[index[q + 1]][2] = index[q]
            else:
                board[index[q]][1] = index[q+1]
                board[index[q + 1]][2] = index[q]
    # board에 값 채우기 좌, 우, 부모의 값

    par_list = []
    par(i)
    par(j)
    # 주어진 i, j를 시작으로 해당 값의 부모 값을 하나의 리스트에 넣기
    # 만들어진 리스트(par_list)에서 처음으로 count가 2인 값이 가장 가까운 공통 조상이 됨
    # x라는 조상 노드를 기준으로 왼쪽과 오른쪽으로 나뉘기 때문에 x라는 조상 노드를 만나기 전까지는 겹치는 숫자가 없음

    for w in par_list:
        if par_list.count(w) == 2:
            parent = w
            break

    cnt = 0
    asd(parent)
    # par을 통해 찾은 가장 가까운 조상 값을 시작으로 cnt해줌
    print('#{} {} {}'.format(tc,parent,cnt))