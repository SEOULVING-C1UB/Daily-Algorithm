# ordinary heappush
def heappush(n):
    global heapcount
    heap.append(n)
    heapcount += 1
    child = heapcount
    parent = child // 2
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent //= 2


for tc in range(1, int(input()) + 1):
    N = int(input())
    heap = [None]
    heapcount = 0
    for n in input().split():
        heappush(int(n))

    # ans : sum of all numbers upward from last node
    ans = 0
    while heapcount:
        heapcount //= 2
        ans += heap[heapcount]

    print('#{} {}'.format(tc, ans))
