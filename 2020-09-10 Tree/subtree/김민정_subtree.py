import sys ; sys.stdin = open("subtree_input.txt","r")

def counter(s) :        # 함수를 실행한 만큼 count를 올려주면 된다.
    global counti
    if s :
        counter(tree[s][0])
        counti += 1
        counter(tree[s][1])

for tc in range(1, int(input())+1) :
    line, s = map(int, input().split())
    lines = list(map(int, input().split()))

    tree = [[0]*3 for _ in range(line+2)]

    for i in range(0, len(lines)-1, 2) :
        p, c = lines[i], lines[i+1]
        if tree[p][0] == 0 :
            tree[p][0] = c
        else :
            tree[p][1] = c
        tree[c][2] = p
    counti = 0
    counter(s)

    print("#{} {}".format(tc, counti))