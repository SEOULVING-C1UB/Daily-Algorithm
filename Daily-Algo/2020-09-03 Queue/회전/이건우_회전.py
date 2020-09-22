import sys
sys.stdin = open('회전_input.txt', 'r')




for c in range(int(input())):
    N, M = map(int, input().split())
    stack = input().split()
    for i in range(M):
        temp = stack.pop(0)         #앞에서 꺼내서 뒤로 넣는 행동을 M번 반복
        stack.append(temp)


    print('#{} {}'.format(c+1,stack[0]))