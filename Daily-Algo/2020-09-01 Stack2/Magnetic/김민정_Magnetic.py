# 자석 맨 위에는 N극이라 N극에 대한 조건을 먼저 걸어준다.

def finder(arr) :
    counti = 0      # 결과를 담을 변수
    for i in range(len(arr)) :  # 순서가 y열 방향이므로 주의한다.
        stack = []
        for j in range(len(arr)) :
            if arr[j][i] == 1 :     # 만약 N극이면
                stack.append(arr[j][i]) # 스택에 붙인다.
            elif arr[j][i] == 2 :   # 만약 S극이면
                if len(stack) > 0 and stack[-1] == 1 :  # stack이 비지 않았고, 가장 마지막 값이 N극이면
                    counti += 1     # N극과 S극 결합에 의해 붙어서 떨어진다.
                    stack = []      # 스택을 비워준다.
    return counti



for t in range(10) :
    my = int(input())

    arr = []

    for i in range(my) :
        temp = list(map(int, input().split()))
        arr.append(temp)


    result = finder(arr)

    print("#{} {}".format(t+1, result))