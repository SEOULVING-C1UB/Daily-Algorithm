# 부분집합
# swea 1486
T = int(input())

def janghoon(cur, total):
    # 전역변수
    global res
    # 선반 높이 이상이면 더 작은 값을 결과값으로
    if total >= b:
        res = min(res, total)
        return
    # 끝까지 탐색
    if cur == n:
        return
    # 이번 값을 포함하는 경우와 그렇지 않은경우
    janghoon(cur + 1, total + len_list[cur])
    janghoon(cur + 1, total)


for test_case in range(1, T + 1):
    n, b = map(int, input().split())
    len_list = list(map(int, input().split()))
    # 무한대로 선언
    res = float('inf')
    # 인덱스 0, 합 0으로 함수 호출
    janghoon(0, 0)
    print('#{} {}'.format(test_case, res - b))