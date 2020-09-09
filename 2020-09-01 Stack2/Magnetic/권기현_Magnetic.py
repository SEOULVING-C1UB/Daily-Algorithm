import sys
sys.stdin = open('input.txt')


for tc in range(1, 11) :
    N = int(input())
    table = [list(map(int, input().split())) for _ in range (N)]
    cnt = 0
    for i in range(N) :
        stack =[]
        for j in range(N) :
            if table[j][i] :
                stack.append(table[j][i])
        for k in range(len(stack)-1) :
            if stack[k] == 1 and stack[k+1] ==2 :
                cnt+=1
    print('#%d %d'%(tc, cnt))
