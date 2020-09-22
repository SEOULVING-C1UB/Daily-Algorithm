'''
<문제풀이>
: 방문한 점수는 중복 방문하지 말고 풀기
1) 문제의 점수는 최대 100점이므로 점수의 최대합은 10000점이다. 방문표시를 할 리스트를 작성한다.
2) scores에 최소합인 0을 담고 문제를 하나씩 방문하며 더한후 결과를 scores에 덧붙인다.
3) 결과적으로 scores에는 현재 문재까지 나올수있는 합의 결과가 저장 된다.
4) 중복을 제거하기 위해 visited를 체크하여 scores에는 중복없는 부분합이 저장되도록한다.
5) 이를 마지막 문제까지 반복하여 scores의 길이가 정답이 된다.

<추가사항>
1) dfs, dp 등등 여러가지 시도에서 런타임에러와 시간초과를 만났다.. 젠장..
2) 중복체크를 set을 이용하는 방법도 있겠다.
'''

# <4차시도>
t = int(input())

for i in range(1, t+1):
    n = int(input())
    problems = list(map(int,input().split()))
    visited = [0]*10001                         # 방문체크용 리스트
    scores = [0]                                # 점수합 리스트에 최소합인 0을 저장
    for j in range(n):                          # 문제 점수들에 대하여
        now = []                                # 이번 문제에서 나올수있는 부분합을 저장하는 리스트
        for score in scores:                    # 현재까지 만들어진 부분합에 대하여
            if visited[score+problems[j]] != 1: # 부분합에 현재 문제점수를 더한 새로운 부분합의 중복확인
                visited[score+problems[j]] = 1  # 방문표시
                now.append(score+problems[j])   # 현재 만들어진 합 저장
        scores += now                           # 이번단계에서 만들어진 합들을 전체리스트에 저장

    print('#{} {}'.format(i,len(scores)))

# <1차시도>
# def score(i, s):
#     if i == n:
#         scores.append(s)
#     else:
#         score(i+1, s+problems[i])
#         score(i+1, s)

# t = int(input())

# for i in range(1, t+1):
#     n = int(input())
#     problems = list(map(int,input().split()))
#     scores = [0]
#     score(0,0)
#     print('#{} {}'.format(i,len(set(scores))))

# <2차시도>
# t = int(input())

# for i in range(1, t+1):
#     n = int(input())
#     problems = list(map(int,input().split()))
#     scores = [0]
#     for j in range(1<<n):
#         s = 0
#         for k in range(n):
#             if j & (1<<k):
#                 s += problems[k]

#     print('#{} {}'.format(i,len(set(scores))))

# <3차시도>
# t = int(input())

# for i in range(1, t+1):
#     n = int(input())
#     problems = list(map(int,input().split()))
#     scores = [0]
#     for j in range(n):
#         now = []
#         for score in scores:
#             now.append(score+problems[j])
#         scores += now

#     print('#{} {}'.format(i,len(set(scores))))