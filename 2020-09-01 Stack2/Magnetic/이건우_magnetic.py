#1220 magnetic



def magnet(array, rows) :
    count = 0                               # 교착상태의 수를 저장할 count 변수
    for i in range(rows) :
        pawn = array[0][i]                  # 각 열의 첫 원소를 pawn 변수에 저장한다
        for j in range(1,rows) :
            if pawn == 1:                   # 만약 pawn에 저장된 원소가 N극 성질을 가졌으면 다음을 한다
                if array[j][i] == 2:        # 비교대상이 S극이면 count += 1을 하고 pawn을 0으로 치기화해준다
                    count += 1
                    pawn = 0
            elif pawn == 2 :                # 만약 pawn에 저장된 원소가 S극일 경우 비교대상(arr[j][i])을 pawn에 저장한다
                pawn = array[j][i]
            elif pawn == 0 :                # 만약 pawn에 아무 자성체도 저장되어 있지 않으면 (pawn == 0) 그 비교대상을 pawn에 저장한다
                pawn = array[j][i]
    return count



case = 10
result = []
for i in range(case):
    rows = int(input())
    array = []
    for j in range(rows):
        row = list(map(int, input().split()))
        array.append(row)
    result.append(magnet(array, rows))

for i in range(case):
    print(f'#{i+1} {result[i]}')