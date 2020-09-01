# 가위바위보 결과를 내줄 함수 작성.
# a, b는 인덱스와 가위바위보값을 갖는 리스트 형태
# b가 이기는 경우를 제외하면 a가 출력되게 작성
def gababo(a,b):
    if a[1]-b[1] == -1 or a[1]-b[1] == 2:
        return b
    else:
        return a

# 들어온 리스트를 왼쪽, 오른쪽 그룹으로 나누는 재귀함수 작성
def splitt(lst):
    n = len(lst)
    # 리스트에 원소가 두개 남으면 가위바위보에서 이긴 결과 리턴
    if n == 2:
        return gababo(lst[0], lst[1])
    # 리스트에 원소가 하나남으면 자동으로 승리하고 리턴
    elif n == 1:
        return lst[0]
    # 왼쪽, 오른쪽으로 나누어지는 재귀함수에 가위바위보 함수를 넣어 최종 승자 리턴
    else:
        return gababo(splitt(lst[0:(n+1)//2]), splitt(lst[(n+1)//2:n]))

t = int(input())

for i in range(1, t+1):
    n = int(input())
    lst = list(map(int,input().split()))
    lst_new = []
    # 일단 받아둔 가위바위보 값을 idx를 추가한 원소 두개짜리 리스트들의 리스트로 재구성
    for idx, p in enumerate(lst):
        lst_new.append([idx+1, p])

    print('#{} {}'.format(i, splitt(lst_new)[0]))