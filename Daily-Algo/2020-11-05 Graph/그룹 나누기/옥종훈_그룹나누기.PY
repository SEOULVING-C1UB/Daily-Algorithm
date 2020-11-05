import sys

sys.stdin = open("그룹나누기_input.txt", "r")

def find_leader(x):
    if team_leader[x] != x:
        team_leader[x] = find_leader(team_leader[x])
    return team_leader[x]


def union(x, y):
    lx = find_leader(x)
    ly = find_leader(y)
    # 두 팀이 합치면 번호가 빠른 사람을 리더로 함
    if lx < ly:
        team_leader[ly] = lx
    else:
        team_leader[lx] = ly


def teams():
    i = 0
    while i < (len(requests)):
        union(requests[i], requests[i+1])
        i += 2
    

    # 팀이 몇 개인지 체크: 리더가 몇 명인지 체크
    # 리더 여부를 나타내는 배열 생성
    leaders = [0]*(n+1)
    for i in range(1, n+1):
        # 먼저 변경된 리더를 업데이트
        team_leader[i] = find_leader(i)
        # 각 출석번호를 순회하며 리더에 체크
        leaders[team_leader[i]] = 1
    
    result = 0
    for i in range(1, n+1):
        if leaders[i]:
            result += 1
    print(leaders)
    return result

t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    requests = list(map(int, input().split()))
    # 한 팀의 리더는 1명: 리더가 다르면 다른 팀
    # 먼저 자기 자신을 리더로 초기화
    team_leader = [i for i in range(n+1)]
    print('#' + str(test_case + 1), teams())