import sys

# # 중복순열 생성 함수
# def product(arr, n):
#     for i in range(len(arr)):
#         if n == 1:
#             yield [arr[i]]
#         else:
#             for next in product(arr, n-1):
#                 yield [arr[i]] + next

# sys.stdin = open('격자판의 숫자 이어 붙이기.txt', 'r')
# T = int(input())
# for t in range(1, T + 1):
#     print(f'#{t}', end=" ")
#     arr = [list(map(int, input().split())) for _ in range(4)]
#     # 동서남북
#     dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    # results = []  # 만들 수 있는 7자리 string 저장
    # # 임의의 위치이므로 모든 좌표 검사
    # for r in range(4):
    #     for c in range(4):
    #         start = [r, c]
    #         for p in product([0, 1, 2, 3], 6): # 중복순열로 동서남북 이동 패턴 결정
    #             x, y = start[0], start[1] # 패턴 변경 시 첫 좌표 초기화
    #             string = str(arr[x][y]) # 임의의 첫 좌표 string으로 입력
    #
    #             for i in p: # 중복순열로 결정한 패턴대로 이동
    #                 if (0 <= x + dx[i] <= 3) and (0 <= y + dy[i] <= 3): # 이동할 좌표가 0~3 사이일 때만(격자판을 벗어나지 않을때만)
    #                     string += str(arr[x + dx[i]][y + dy[i]]) # 이동한 좌표의 값 strings에 추가
    #                     # 이동한 좌표로 이동
    #                     x = x + dx[i]
    #                     y = y + dy[i]
    #                 else:
    #                     break # 격자를 벗어난 경우 루프 탈출
    #             # 하나의 패턴 완료 후 생성된 string이 results에 없고(중복 방지), 문자열 길이가 7이면
    #             if string not in results and len(string) == 7:
    #                 results.append(string) # results에 추가
    # # 모든 좌표별 모든 패턴 검사 후 results에 추가
    # print(len(results))


def function(r, c, n, string):
    if n == 6:
        results.append(string)
    else:
        for i in range(4):
            if 0 <= r + dr[i] < 4 and 0 <= c + dc[i] < 4:
                function(r + dr[i], c + dc[i], n + 1, string + arr[r + dr[i]][c + dc[i]])

sys.stdin = open('격자판의 숫자 이어 붙이기.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    arr = [list(input().split()) for _ in range(4)]
    # 동서남북
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    results = []
    for r in range(4):
        for c in range(4):
            function(r, c, 0, arr[r][c])
    print(len(set(results)))

# t = int(input())
# for i in range(1,t+1):
#     field = [list(input().split()) for _ in range(4)]
#     worms = []
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     for y in range(4):
#         for x in range(4):
#             makeworm(x, y, 0, field[y][x])
#     print('#{} {}'.format(i,len(set(worms))))