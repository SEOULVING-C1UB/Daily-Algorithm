'''
[컨셉]
1) magnets에 4개의 자석에 대한 정보를 넣고, K번의 회전마다 rotate함수를 돌린다.
2) rotate는 맞닿은 자석들을 돌릴 수 있나 확인해 돌리고, 해당 자석을 돌리는 형식으로 구현했다.
   * 처음에 way라는 값을 주지 않아 무한 루프가 돌았었다. :(
3) magnets에 담긴 값을 활용해 조건에 맞춰 결과를 출력한다.
'''

def rotate(i, d, way):                              # i번 자석에서 d의 방향으로 돈다. 진행방향인 way에 맞춰 양옆의 자석 확인
                                                    # way는 2는 양옆, 0은 왼쪽만, 1은 오른쪽만 확인.
    if way == 2 or way == 0:                        # 왼쪽 확인
        if i-1 >= 0:                                # 0~3의 범위 내에 있고
            if magnets[i][6] != magnets[i-1][2]:    # 맞닿은 부분이 서로 다르다면
                rotate(i-1, -d, 0)                  # 그 자석도 돌리자.
    if way == 2 or way == 1:                        # 오른쪽 확인
        if i+1 <= 3:
            if magnets[i][2] != magnets[i+1][6]:
                rotate(i+1, -d, 1)
     
    if d > 0:                                       # 시계방향으로 돌리기
        temp = magnets[i][7]
        magnets[i] = [temp] + magnets[i][:7]
    else:                                           # 반시계방향으로 돌리가
        temp = magnets[i][0]
        magnets[i] = magnets[i][1:] + [temp]
 
 
TC = int(input())                               # Test Case의 개수
for tc in range(TC):
    K = int(input())                            # 회전 횟수
    magnets = []                                # 처음 자석 정보를 담는다
    for i in range(4):
        m = list(map(int, input().split()))
        magnets.append(m)
    for i in range(K):                          # K번 회전을 시작하면서
        idx, dir =  map(int, input().split())
        rotate(idx-1, dir, 2)                   # rotate 함수를 쓴다. 처음에는 자석 기준으로 좌우를 모두 확인해야하니 way에 2를 넣는다. 
 
    ans = 0                                     # 결과값을 담을 변수 
    for i in range(4):
        ans += magnets[i][0]*(2**i)             # 조건에 맞춰 연산해서 출력한다.
    print('#{} {}' .format(tc+1, ans))