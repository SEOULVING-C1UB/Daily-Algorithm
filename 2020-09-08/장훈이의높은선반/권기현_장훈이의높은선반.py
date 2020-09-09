import sys
sys.stdin = open("5097.txt")



total_tc=int(input())

for tc in range(1, total_tc+1):

    N, M = map(int, input().split())
    number_queue = list(map(int, input().split()))
    for i in range (M):
        number_queue.append(number_queue.pop(0))
    print("#%d %d"%(tc, number_queue[0]))