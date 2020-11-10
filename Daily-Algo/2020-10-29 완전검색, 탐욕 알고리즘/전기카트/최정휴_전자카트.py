'''
<문제해결>
 : 처음과 끝은 항상 1번 노드여야 하므로 나머지 노드들의 모든 순열에 대해 완전검색을 진행한다.
1) 1번 노드를 제외한 나머지 노드들의 순열을 만든다.
2) 앞과 뒤에 1을 붙여 만든 루트를 통해 비용을 계산한다.
3) 현재값을 넘어버리면 가지치기.
4) 루트를 모두 순회한 뒤 최솟값이 정답

<추가사항>
1) 순열을 짜는것도 좋지만 가져와서 써도 크게 문제없다.
'''

import sys
sys.stdin = open("5189_전자카트.txt")

import itertools

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    per = list(itertools.permutations(list(range(2, n+1)), n-1))    # 1번 노드를 제외한 노드들의 순열 생성
    
    field = [list(map(int, input().split())) for _ in range(n)]
    ans = 1000000000                                                # 충분히 큰값으로 정답 설정하여 갱신에 문제가 없게끔
    for p in per:                                                   # 각 조합에 대해 루트 생성
        route = [1] + list(p) + [1]                                 # 각 루트의 처음과 끝에 1 추가
        s = 0
        for i in range(n):                                          # 루트를 순회하며 구해진 비용에 대해
            s += field[route[i]-1][route[i+1]-1]
            if s >= ans:                                            # 현재의 최소를 넘기면 가지치기
                break
        if s < ans:                                                 # 끝까지 순회 후 최솟값 갱신
            ans = s
    print(f'#{tc} {ans}')