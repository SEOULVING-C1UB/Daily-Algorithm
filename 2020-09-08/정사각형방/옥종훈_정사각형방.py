import sys
from collections import deque

sys.stdin = open("D4_1861_input.txt", "r")


# 정사각형 방을 돌면서 bfs를 돌려 이동하는 방의 개수를 리턴
def square_room():
    # 이동하는 방의 갯수, 처음에 적힌 수를 저장하는 리스트
    result = []
    
    # 가지치기를 위한 체크리스트
    # 이미 방문한 숫자는 bfs를 시작하지 않아도 됨
    # 왜냐면 정확히 1만큼 큰 수 외에 방문할 수 없기 때문에, 조합이 유일하기 때문
    check = [1]*(n**2+1)
    
    temp = 0
    for i in range(n):
        for j in range(n):
            if check[room[i][j]]:
                dist = bfs((i, j))
                # 처음에 시작한 수로부터 끝난 수까지에 해당하는 체크리스트의 값을 0으로
                # 1~5까지 이동했다고 쳤을 때 다음에 2에서 시작해봐야 5까지만 갈 수 있기 때문
                for k in range(room[i][j], room[i][j]+dist):
                    check[k] = 0
                # 이동한 방의 수가 많거나 같을 때 갱신
                if dist >= temp:
                    temp = dist            
                    result.append((temp, room[i][j])) 
    result.sort()
    maximum = result[-1][0]    
    for i in range(len(result)):
        if result[i][0] == maximum:
            # 가장 많은 방의 갯수를 이동한 조합 중에서 번호가 제일 적은 것
            room_number = result[i][1]
            break

    print(room_number, maximum)


def bfs(v):
    result = 0        
    q = deque([v])    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        w = q.popleft()
        result += 1
        for i in range(4):
            nx = w[0]+dx[i]
            ny = w[1]+dy[i]
            if 0 <= nx < n and 0 <= ny < n and room[nx][ny] == room[w[0]][w[1]] + 1:
                q.append([nx, ny])               
    return result

t = int(input())
for test_case in range(t):    
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    print('#' + str(test_case + 1), end=" ")
    square_room()
