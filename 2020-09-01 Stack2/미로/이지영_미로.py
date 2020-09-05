import sys
sys.stdin = open("미로_input.txt")

def DFS(miro, startX, startY):

    # 방문한거, 방문할거 리스트로 만들기
    visited, needVisit = [], []

    #방향 (x,y) 형태
    directions = [
        (0, 1),  # up
        (0, -1),  # down
        (1, 0),  # right
        (-1, 0)  # left
    ]

    # 우선 들어오는 시작점을 방문할거에 넣는다
    needVisit.append((startX, startY))

    #방문할 곳이 있다면?
    while needVisit:

        # 방문할거니까 팝해서 needVisit에서 빼주고
        # 현위치를 position에 넣어줌
        position = needVisit.pop()


        #이게 내가 찾는 출구라면? 끝
        if miro[position[1]][position[0]] == 3:
            return 1

        #그게 아니라면 방문했는지 확인부터한다
        #아직 방문 안했으면 visited에 넣어주고(=이제 하니까)
        elif position not in visited:
            visited.append(position)

            # 양옆위아래로 탐색한다
            for x, y in directions:

                newX = position[0]+x
                newY = position[1]+y

                # 양수 & N보다 작아야함 (양수여야 하는 이유는 파이썬은 -1해도 리스트 거꾸로 돌아서 결과가 나오니까)
                if 0<= newX and newX<N and 0<=newY and newY<N:

                    # 만약 길이 있으면 방문할거에 넣어주고
                    if miro[newY][newX] == 0:
                        needVisit.append((newX, newY))

                    # 출구 나오면 걍 끝이다
                    elif miro[newY][newX] == 3:
                        return 1
                    
    # 다 돌았는데도 리턴을 안했다? 갈 수 있는 길에서 출구가 없는거임
    return 0

T = int(input())

for tc in range(1, T+1):

    N = int(input())    #미로 크기

    miro = [list(map(int, input())) for _ in range(N)]

    # 시작 X랑 Y값
    startX = 0  
    startY = 0

    for i in range(N):
        if 2 in miro[i]:
            startX = miro[i].index(2)   #시작점 찾아주기
            startY = i


    print('#{} {}'.format(tc, DFS(miro, startX, startY)))
