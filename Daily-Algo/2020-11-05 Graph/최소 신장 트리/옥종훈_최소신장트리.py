import sys

sys.stdin = open("최소신장트리_input.txt", "r")

def find_leader(x):
    if team_leader[x] != x:
        team_leader[x] = find_leader(team_leader[x])
    return team_leader[x]


def union(x, y):
    lx = find_leader(x)
    ly = find_leader(y)
    # 두 팀이 합치면 번호가 빠른 사람을 리더로 함
    if lx <= ly:
        team_leader[ly] = lx
    else:
        team_leader[lx] = ly


def kruskal():
    cnt = 0
    result = 0

    for i in range(E):
        lx = find_leader(edges[i][0])
        ly = find_leader(edges[i][1])
        if lx != ly:
            result += edges[i][2]
            cnt += 1
            union(lx, ly)
        if cnt == V:
            break
    return result
    

t = int(input())
for test_case in range(t):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    team_leader = [i for i in range(V+1)]
    print('#' + str(test_case + 1), kruskal())