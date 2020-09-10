import sys ; sys.stdin = open("이진힙_input.txt", "r")

def heapPush(value):            # 전위 (수업시간에 배운 최소힙 활용함)
    global heapCount
    heapCount += 1
    heap[heapCount] = value
    current = heapCount
    parent = current // 2
    while parent and heap[parent] > heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current // 2

def finder() :              # 조상 노드의 합을 구하는 함수
    global N
    counti = 0
    indexi = N
    while indexi :
        indexi = indexi // 2
        counti += heap[indexi]
    return counti

for tc in range(1, int(input())+1) :
    heapCount = 0
    N = int(input())
    temp = list(map(int, input().split()))
    heap = [0 for _ in range(N+1)]
    for i in range(N) :
        heapPush(temp[i])
    result = finder()

    print("#{} {}".format(tc, result))


