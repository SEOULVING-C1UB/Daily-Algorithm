import sys ; sys.stdin = open("이진검색_input.txt","r")

def in_order(node):
    global count
    global V
    if node <= V :
        in_order(node*2)
        tree[node] = count
        count += 1
        in_order(node*2+1)

for tc in range(1, int(input())+1) :
    V = int(input())
    count = 1
    tree = [0] * (V+1)
    in_order(1)

    print("#{} {} {}".format(tc,tree[1], tree[V//2]))


