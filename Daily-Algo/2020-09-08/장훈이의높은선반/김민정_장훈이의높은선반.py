
powerset = []

def setmaker(B) :
    mini = 100
    for i in range(1 << len(arr)) :     # 비트연산으로 모든 부분집합을 구한다.
        temp = []
        temp_cnt = 0
        for j in range(len(arr)) :
            if i & (1<<j) :
                temp.append(arr[j])
                temp_cnt += arr[j]
        now = temp_cnt - B          # 현재 부분집합 합에서 만족해야 하는 값 B를 뺀다.
        if now >= 0 :               # 만약 현재 값이 0보다 크고
            if now <= mini :        # min값보다 작으면 min 값은 현재 값
                mini = now
        if mini == 0 :              # 예외처리
            break
    return mini


for tc in range(1, int(input()) + 1 ) :
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = setmaker(B)
    print("#{} {}".format(tc, result))