import sys ; sys.stdin = open("노드의힙_input.txt", "r")

def calculator(V) :
    while True :
        parent = V // 2         # 부모 노드는 현재노드 나누기 2
        left = tree[parent * 2]     
        right = tree[parent * 2 + 1]    
        tree[parent] = left + right
        V -= 2      # 다음 순번을 위해 V에서 2를 빼준다. 
        if parent == L : return tree[L]     # 만약 부모노드 인덱스가 L 에 도달하면, 함수 종료

for tc in range(1, int(input())+1) :
    V, M, L = map(int, input().split())
    if V % 2 :          # 노드 수가 홀수 일 경우 노드 개수+1 만큼 리스트 초기화
        tree = [0] * (V+1)
    else :              # 노드 수가 홀수 일 경우는 right값이 비는 현상이 발생하기 때문에 개수+2만큼 리스트 초기화
        tree = [0] * (V+2)
    for m in range(M) :
        idx, value = map(int, input().split())
        tree[idx] = value

    print("#{} {}".format(tc, calculator(V)))