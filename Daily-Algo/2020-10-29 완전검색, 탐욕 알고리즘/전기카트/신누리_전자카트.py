'''
[컨셉]
1) 방문해야 하는 구역들을 두고(2~n번 구역) 순열을 만든다.
2) 순열이 다 만들어지면, 가중치를 계산해서 최솟값으 갱신한다.
'''

def perm(n, k):
    global mini
    if k == n:
        ans = 0
        ans += arr[0][areas[0]]
        ans += arr[areas[n-1]][0]
        for i in range(n-1):
            ans += arr[areas[i]][areas[i+1]]
        if ans < mini: mini = ans
    else:
        for i in range(k, n) :
            areas[k], areas[i] = areas[i], areas[k]
            perm(n, k+1)
            areas[i], areas[k] = areas[k], areas[i]


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mini = 0xFFFFFFF
    areas = list(range(1, N))
    perm(N-1, 0)
    print('#{} {}' .format(t+1, mini))