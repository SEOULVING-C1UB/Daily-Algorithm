# set 변수형을 사용해  중복되는 값은 알아서 하나로 통합되게 한다.

def powerset(arr) :             # 비트연산으로 모든 부분집합을 구한다.
    for i in range(1 << len(arr)) :
        temp = []
        sumi = 0
        for j in range(len(arr)) :
            if i & (1 << j ) :
                temp.append(arr[j])
                sumi += arr[j]
        mypower.append(temp)
        seti.add(sumi)


for tc in range(1, int(input())+1) :

    N = int(input())
    arr = list(map(int, input().split()))
    seti = {0}
    mypower = []

    powerset(arr)


    result = 0
    print("#{} {}".format(tc, len(seti)))