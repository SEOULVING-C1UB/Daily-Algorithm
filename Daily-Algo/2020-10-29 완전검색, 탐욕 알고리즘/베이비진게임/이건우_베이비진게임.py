import sys
sys.stdin = open('input.txt','r')

## permutation 이용
## 문제에서 '6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다'라는 조건이 있다.
## 한사람의 카드가 3개 이상일때부터 permutation을 돌린다
## babyGin함수의 경우 카드가 6개일때만 4~6번 카드에 대해서 확인을해준다.
## 실행 도중 flag = 1(성공)이 나오면, winner가 1 or 2번 선수인지 표시후 break를 통해 for문을 나온다




def babyGin(arr):
    global flag
    check = 0

    if arr[0] == arr[1] and arr[1] == arr[2]: check += 1
    if len(arr) == 6:
        if arr[3] == arr[4] and arr[4] == arr[5]: check += 1

    if arr[0] +1 == arr[1] and arr[1] + 1 == arr[2]: check += 1
    if len(arr) == 6:
        if arr[3] +1 == arr[4] and arr[4] + 1 == arr[5]: check += 1

    if check >= 1:
        flag = 1
        return


def perm(arr,n,k):
    if k == n:
        babyGin(t)
    else:
        for i in range(n):
            if visit[i]: continue
            t[k] = arr[i]
            visit[i] = 1
            perm(arr, n, k+1)
            visit[i] = 0



for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    winner = 0
    for i in range(0,len(arr),2):
        arr1.append(arr[i])
        if len(arr1)>=3:
            flag = 0
            visit = [0] * len(arr1)
            t = [0] * len(arr1)
            perm(arr1, len(arr1), 0)
            if flag:
                winner = 1
                break
        arr2.append(arr[i+1])
        if len(arr2)>=3:
            flag = 0
            visit = [0] * len(arr2)
            t = [0] * len(arr2)
            perm(arr2, len(arr2), 0)
            if flag:
                winner = 2
                break


    print('#{} {}'.format(tc, winner))

