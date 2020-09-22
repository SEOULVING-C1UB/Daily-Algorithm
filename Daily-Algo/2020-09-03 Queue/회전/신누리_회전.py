import sys
sys.stdin = open("(5097)회전_input.txt")


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    # 문제의 의도는 Queue니 enQueue deQueue해야하나 잠시 고민했지만..
    # 결국 직관적으로 index로 계산해서 반환했음.
    print('#{} {}' .format(t+1, num[M % N]))
