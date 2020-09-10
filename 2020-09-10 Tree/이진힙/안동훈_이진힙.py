import sys
sys.stdin = open('이진힙_input.txt')

def heap_insert(value):
    global idx
    binary_heap[idx] = value # 먼저 heap에 값을 넣는다.
    num = idx
    idx += 1
    while True:
        if num//2 != 0 and binary_heap[num//2] > binary_heap[num]: # 부모 노드가 있고, 부모 노드의 값이 자식보다 크면 서로 바꾼다.
            binary_heap[num//2], binary_heap[num] = binary_heap[num], binary_heap[num//2]
            num = num//2
        else:
            break

T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    n = int(input())
    values = list(map(int,input().split()))
    binary_heap = [0] * (n+1) # 이진 힙 생성
    idx = 1
    for value in values: # 이진 힙에 값을 넣는다.
        heap_insert(int(value))

    # 마지막 값(binary_heap[n])의 조상들을 answer에 추가해준다.
    while n != 0:
        n = n//2
        answer += binary_heap[n]

    print("#{0} {1}" . format(test_case, answer))
