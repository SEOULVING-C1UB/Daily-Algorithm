'''
[컨셉]
1) player A, B에 각각 2개씩 넣은 상태에서 시작
2) 그 뒤로 하나씩 카드를 나눠받을 때마다 babygin 여부 확인
   - 이거 확인은 각 플레이어의 카드 덱을 sort한 뒤에, i번째와 i-1번째를 비교해가며 triplet과 run 여부 각각 확인
'''

def babygin(li):
    li.sort()
    run = 0
    triplet = 0
    for i in range(1, len(li)):
        if li[i] == li[i-1]:
            triplet +=1
        else:
            triplet = 0
        if li[i] == li[i-1]+1:
            run += 1
        else:
            if li[i] != li[i-1]: # 7 8 8 9 도 연속임을 고려하지 않았었음 :(
                run = 0
        if triplet>=2 or run>=2:
            return True
    return False


T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    A = [arr[0], arr[2]]
    B = [arr[1], arr[3]]
    result = 0
    for i in range(4, len(arr)):
        if i %2 == 0:
            A.append(arr[i])
            if babygin(A) : result = 1
        else:
            B.append(arr[i])
            if babygin(B): result = 2
        if result: break
    print('#{} {}' .format(t+1, result))
