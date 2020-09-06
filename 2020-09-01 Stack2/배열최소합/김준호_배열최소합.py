import sys

sys.stdin = open("배열최소합_input.txt", "r")

T = int(input())

def dfs(cur_row, res):
    global min_res
    # 가지치기
    if res >= min_res:
        return
    # 최소값으로 바꿔주기
    if cur_row == n:
        if res < min_res:
            min_res = res
    # 사용가능한 열이면 다음행은 해당 열로 탐색
    for i in range(n):
        if check[i]:
            check[i] = 0
            dfs(cur_row + 1, res + mat[cur_row][i])
            check[i] = 1

for test_case in range(1, T + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    check = [1 for _ in range(n)]   # 1, 0 을 참, 거짓으로 이용한 배열
    min_res = 99999     # 다른 합들보다 무조건 크도록 초기값 설정
    dfs(0, 0)   # 첫 행, 합 : 0 에서 탐색 시작
    print('#{} {}'.format(test_case, min_res))