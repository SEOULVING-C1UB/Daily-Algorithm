import sys
sys.stdin = open('input.txt', 'r')

## input을 받으면서 end time이 최소가 될 때를 minE에 저장한다
## 모든 작업시간에 있어 start time이 앞에서 구한 minE와 비교, 그 중 end time이 최소가 되는 값을 구해서
## 다시 minE에 할당한다. while문 한번 반복시마다 count에 1을 더하고 while문으로 반복하면서 만약 24시까지
## 모든 작업이 끝나서 더 이상 flag가 1이 되지 않을 때 break를 걸어서 while문 밖으로 나온다.

for tc in range(1,int(input())+1):
    N = int(input())
    minE = 25
    timetable = []
    for i in range(N):
        temp = list(map(int, input().split()))
        timetable.append(temp)
        if temp[1] < minE:
            minE = temp[1]
    count = 0
    while True:
        flag = 0
        tempMin = 25
        for i in range(N):
            start, end = timetable[i]
            if start < minE : continue
            else:
                if end < tempMin:
                    flag = 1
                    tempMin = end
        minE = tempMin
        count += 1
        if not flag: break

    print('#{} {}'.format(tc, count))