import sys

sys.stdin = open("D4_3752_가능한시험점수_input.txt", "r")


# Greedy: sum_set의 최대 크기 10000(100*100)이고 최대 100번 반복 - 100만번 연산
def score_cases():
    # 점수의 합들을 보관하는 sum_set
    sum_set = set()
    sum_set.add(score_list[0])
    
    # score_list를 돌면서 각각의 점수를 sum_set의 원소들에 더한 합 temp를 생성
    # temp를 sum_set에 더해주어 갱신   
    # sum_set내에 원소가 있어야 하므로 0번째 점수는 미리 더하고 1번 인덱스부터 반복
    for i in range(1, len(score_list)):
        temp = []
        for element in sum_set:
            temp.append(element+score_list[i])
        # score_list의 원소를 먼저 sum_set에 넣으면 자기자신을 더한 것까지 추가되므로 나중에 넣음
        sum_set.add(score_list[i])
        sum_set.update(temp)
    
    # 문제를 다 틀렸을 경우까지 추가해서 sum_set의 크기에 1을 더해 리턴
    return len(sum_set) + 1


# 수업시간 풀이: dfs
def score_dfs(k, s):
        if visit[k][s]:
            return
        visit[k][s] = 1
        if k == n:
            return
        score_dfs(k+1, s)
        score_dfs(k+1, s + score_list[k])


t = int(input())
for test_case in range(t):    
    n = int(input())
    score_list = sorted(list(map(int, input().split())))
    
    visit = [0]*10001
    print('#' + str(test_case + 1), score_cases())    
    print('#' + str(test_case + 1), score_dfs(0, 0))    
    print('#' + str(test_case + 1), score_bfs())    
