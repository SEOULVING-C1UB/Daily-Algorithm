# 1. Using function in each loop shorten executing time.
# 2. Separate case to use DFS, BFS. In this problem, BFS is faster.
# 3. Check table using 'hash' is faster and more efficient in memory than using 'list'.


from collections import deque
import sys

sys.stdin = open('연산_input.txt', 'r')


# For shorten time, make function each step.
def calc_num(num, stat):
    if stat == 0:
        return num + 1
    elif stat == 1:
        return num - 1
    elif stat == 2:
        return num - 10
    else:
        return num * 2


def bfs():
    q = deque([[N, 0]])
    while q:
        n, cnt = q.popleft()
        if check.get(n, 0):  # check visited
            continue
        check[n] = 1
        cnt += 1
        for i in range(4):
            temp = calc_num(n, i)
            if temp == M:
                return cnt
            if 1 <= temp <= 1000000:
                q.append([temp, cnt])


for tc in range(int(input())):
    N, M = map(int, input().split())
    check = {}
    print('#{} {}'.format(tc + 1, bfs()))
