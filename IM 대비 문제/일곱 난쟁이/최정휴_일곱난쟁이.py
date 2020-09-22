'''
<접근방법>
 : 7명의 조합을 찾는거보다 2명을 찾는게 이득이지
 1) 난쟁이 키를 받아와 총합을 구한다
 2) 이중 반복문을 통해 두명짜리 조합을 찾고 총합에서 빼면 100이되는지 확인
<주의사항>
 1) 이중반복문은 break로 한번에 못빠져나오니까 함수에 넣어서 리턴으로 빠져나오자
 2) del쓸때 dwarfs[i] 먼저 제거하면 인덱스 꼬인다. 뒤부터 제거해라
'''

dwarfs = [int(input()) for _ in range(9)]               
dwarfs.sort()                                           # 오름차순으로 뽑아야 하니까 미리 소트

total_h = sum(dwarfs)                                   # 9명의 총합을 미리 구해둠
def find():
    for i in range(8):                                  # 가짜 두명 찾는 이중반복문
        for j in range(i+1,9):
            if total_h - dwarfs[i] - dwarfs[j] == 100:  # 두명을 빼서 100이 되면 끝
                del dwarfs[j]                           # j번째 지우고, i번째 지우고
                del dwarfs[i]
                return
find()
for dwarf in dwarfs:
    print(dwarf)