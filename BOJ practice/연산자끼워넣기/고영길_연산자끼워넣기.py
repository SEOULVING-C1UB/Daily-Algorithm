def cal(n1, n2, oper):
    if oper == 0:
        return n1 + n2
    elif oper == 1:
        return n1 - n2
    elif oper == 2:
        return n1 * n2
    else:
        return int(n1 / n2)


def dfs(res, idx, oper):
    global maxi, mini
    if idx == N - 1:
        mini = min(mini, res)
        maxi = max(maxi, res)
        return

    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            dfs(cal(res, numbers[idx + 1], i), idx + 1, oper)
            oper[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))
mini = 1000000000
maxi = -1000000000
dfs(numbers[0], 0, opers)
print(maxi)
print(mini)
