import sys
sys.stdin = open('회전_input.txt')

# 수학적으로 풀이가 가능한 문제로 보이지만, 큐를 실습하는 차원에서 풀이한다.

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    CircleQueue = list(map(int, input().split()))
    for i in range(m):
        value = CircleQueue.pop(0) # deQueue
        CircleQueue.append(value) # enQueue

    answer = CircleQueue.pop(0)
    print('#{0} {1}'.format(test_case, answer))