# Queue 6일차 5097.회전
#  0.12630s
tc = int(input())

for t in range(tc) :
    num, roti = map(int, input().split())
    queue = list(map(int, input().split()))
    for i in range(roti) :
        queue.append(queue.pop(0))
    print("#{} {}".format(t+1, queue[0]))