'''
[컨셉]
1) 직원으로 부분집합을 만들고, 그 부분집합의 합 중 B보다 크고 B와 가장 가까운 것을 고른다
2) mini라는 변수에 최솟값을 넣어 가지치기에 사용하고, 부분집합 만들기가 완성되면 update하는 방식
'''

# cursum을 활용해 가지치기
def subsetsum(k, N, cursum) :
    global mini
    if k == N :                             # 부분집합 만들기가 끝났다면
        if 0<= cursum - B < mini :          # cursum이 B 이상이며, B와의 차가 mini보다 작을 때
            mini = cursum - B               # 갱신
    else :
        if cursum < B + mini :              # 가지치기. 현재까지의 최솟값보다 작을 경우에만 진행
            subsetsum(k+1, N, cursum+H[k])  # k번 직원 선택
            subsetsum(k+1, N, cursum)       # k번 직원 미선택

T = int(input())
for t in range(T) :
    N, B = map(int, input().split())
    H = list(map(int, input().split()))     # 직원의 키가 담긴 list. 0~N-1번의 직원.
    # 결과 값이 담길 mini의 값은 모든 직원들의 키의 합 - B 로 초기화.
    mini = sum(H) - B
    # 부분집합의 합
    subsetsum(0, N, 0)
    print('#{} {}' .format(t+1, mini))
