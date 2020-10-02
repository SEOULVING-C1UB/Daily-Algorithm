'''
[컨셉]
1) 입력을 받아온다.
  - (주의) 한 줄이 문자열로 들어온다는 점 주의!
2) cnt에는 단지의 수를, houses에는 각 단지 별 집의 수를 넣는다. 
3) grouping 함수를 통해 cnt와 houses를 구한다.
  - 기본적으로는 dfs의 알고리즘 사용.
  - 1을 찾으면 단지 찾기를 시작. 단지 내에서 집의 개수는 house로 세기, 단지가 끝나면 houses에 append.
  - 이미 방문한 집은 0으로 변경. (visited check)
4) 오름차순으로 정렬 후 출력. (cnt, cnt의 개수만큼 houses print.)
'''

# 컨셉 3
def grouping():
    global cnt
    for i in range(N):
        for j in range(N):
            if arr[i][j] :
                cnt +=1 
                S = [(i,j)]
                house = 0
                while S :
                    a, b = S.pop()
                    if arr[a][b] :
                        house += 1
                        arr[a][b] = 0
                        for k in range(4):
                            if 0 <= a+dir1[k] < N and 0 <= b+dir2[k] < N:
                                if arr[a+dir1[k]][b+dir2[k]]:
                                    S.append((a+dir1[k], b+dir2[k]))
                houses.append(house)

# 컨셉 1
N = int(input())
arr = [ list(map(int, list(input()))) for _ in range(N)]

# 컨셉 2
cnt = 0
houses = []
dir1 = [1, 0, -1, 0]
dir2 = [0, 1, 0, -1]
grouping()

# 컨셉 4
houses.sort() 
print(cnt)
for i in range(cnt):
    print(houses[i])