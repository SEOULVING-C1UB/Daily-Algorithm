import sys ; sys.stdin = open("1231_중위순회.txt", "r")
def preorder(node) :
    if node : # 0이 아닐 경우 실행
        preorder(tree[node][0])
        word.append(dict[node])
        preorder(tree[node][1])

for tc in range(1, 11) :
    V = int(input())
    tree = [[0] * 3 for _ in range(V+1)]
    dict = {}
    for i in range(V):
        tempi = input().split()
        p = int(tempi[0])
        if len(tempi) == 4 :
            cl = int(tempi[2])
            cr = int(tempi[3])
            tree[p][0] = cl
            tree[p][1] = cr
            tree[cl][2] = tree[cr][2] = p
        elif len(tempi) == 3 :
            cl = int(tempi[2])
            tree[p][0] = cl
            tree[cl][2] = p
        dict[p] = tempi[1]  # word저장

    word = []
    preorder(1)
    print("#{} {}".format(tc,"".join(map(str,word))))

