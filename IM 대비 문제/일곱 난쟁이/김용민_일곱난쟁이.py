num = 9
heights = []

for _ in range(num):
    height = int(input())
    heights.append(height)

ans = []
for i in range(1 << len(heights)):          # 부분집합 생성
    tmp = []
    for j in range(len(heights)+1):         # 원소의 수만큼 비트를 비교함
        if i & (1 << j):                    # i의 j번째 비트가 1이면 j 번째 원소 출력
            tmp.append(heights[j])          # tmp에 원소 저장후
    if len(tmp) == 7 and sum(tmp) == 100:   # 그 길이가 7이고 합이 100인 경우만
        ans.append(tmp)                     # ans에 저장
result = sorted(ans[0])                     # 정렬
for i in result:                            # 출력
    print(i)
