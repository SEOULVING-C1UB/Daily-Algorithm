import sys

sys.stdin = open("D4_7465_input.txt", "r")

# 그래프 이론 "서로소집합(disjoint set)"을 이용한 풀이
# 관심 있는 분들은 아래 링크 한번 보세요 DFS보다 간단하고 빠름
# https://youtu.be/-YQkA9vVqu8?t=4681


# 노드들을 묶는(union)함수
# 서로 연결된 두 노드에 대해, 루트 노드를 기준으로 묶음
# 연결된 노드들 중에서는(그룹 내에서는) 번호가 가장 작은 노드가 root
def grouping():
    for relation in people:
        a = find_parent(relation[0])
        b = find_parent(relation[1])
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    for i in range(1, n+1):
        parent[i] = find_parent(i)

    return len(set(parent))-1


# 노드의 루트 노드를 리턴하는 함수
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]    


t = int(input())
for test_case in range(t):    
    n, m = map(int, input().split())
    # 루트 노드를 저장하는 리스트
    parent = [i for i in range(n+1)]
    # 사람들 간의 연결을 저장하는 리스트
    people = []
    for _ in range(m):
        a, b = map(int, input().split())
        people.append((a, b)) 
    print('#' + str(test_case + 1), grouping())
