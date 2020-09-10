import sys
sys.stdin = open("5176_이진탐색.txt")

'''
<풀이과정>
: 중위 순회를 하며 1부터 차례로 값을 넣는다
'''

def joong(v):
    global cnt          # 전역변수 설정
    if v > n:           # 인덱스 확인하여 넘어가면 리턴
        return
    joong(2*v)          # 왼쪽 자식 재귀호출
    nodes[v] = cnt      # 현재노드에 값 저장
    cnt += 1            # 저장 후 cnt 1 증가
    joong(2*v+1)        # 오른쪽 자식 재귀호출

t = int(input())

for i in range(1,t+1):
    n = int(input())
    nodes = [0]*(n+1)
    cnt = 1
    joong(1)
    print('#{} {} {}'.format(i, nodes[1], nodes[n//2]))