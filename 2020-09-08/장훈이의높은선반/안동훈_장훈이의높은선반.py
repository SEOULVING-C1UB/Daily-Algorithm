import sys
sys.stdin = open('장훈이의 높은 선반_input.txt')

def dfs(idx, sum, people):
    if sum >= b: # 정훈이의 높은 선반보다 높아지면 정답군에 담는다.
        answer.append(sum)
        return
    if idx == n: # idx 벗어나면
        return
    dfs(idx+1, sum+people[idx], people)
    dfs(idx+1, sum, people)

T = int(input())
for test_case in range(1, T + 1):
    answer = [] # b를 넘는 모든 정답군을 담을 것이다.
    n, b = map(int ,input().split())
    h = list(map(int ,input().split()))

    # dfs 재귀로 문제를 해결해 보자.
    dfs(0, 0, h)

    answer = sorted(answer)

    print("#{0} {1}".format(test_case, answer[0]-b))
