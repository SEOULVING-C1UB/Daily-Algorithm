'''
[컨셉]
1) 재귀로 접근. 4*4의 각 지점에서 시작해서, 사방으로 움직이며 재귀.
   base는 cnt로 반복 횟수 저장해서 처리.
2) 0으로 시작할 수도 있어서 numstr이라는 변수에 str으로 수를 담음
3) 중복된 수를 없애기 위해 set을 이용해서 중복 제거
'''

def findnum (x, y, cnt, numstr) :
    if cnt == 7 :               # 7개의 숫자를 모두 고르면
        result.append(numstr)   # 결과를 저장할 배열에 추가  
    else :
        numstr += str(arr[x][y])                                # str으로 추가해주고 
        cnt +=1                                                 # 고른 숫자의 개수에 +1
        for d in range(4) :                                     # 4방향으로 움직이며
            if 0 <= x+dir1[d] < 4 and 0 <= y + dir2[d] < 4 :    # 움직인 곳이 배열 범위 내에 있다면
                findnum(x+dir1[d], y+dir2[d], cnt, numstr)      # 그 지점에서 재귀

T = int(input())
for t in range(T) :
    arr = [list(map(int, input().split())) for _ in range(4)]

    # 4방향으로 움직이기 위해
    dir1 = [1, 0, -1, 0]
    dir2 = [0, 1, 0, -1]
    
    result = []
    # 배열의 각 칸에서 함수 시작
    for i in range(4) :
        for j in range(4) :
            findnum(i, j, 0, '')
    # 중복 제거
    result = list(set(result))
    print('#{} {}' .format(t+1, len(result)))