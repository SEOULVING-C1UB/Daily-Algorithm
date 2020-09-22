def check_bingo():
    cnt = 0
    # horizontal
    for j in range(5):
        if all(check[j]):
            cnt += 1

    # vertical
    for i in range(5):
        if all([check[j][i] for j in range(5)]):
            cnt += 1

    # cross
    if all([check[j][j] for j in range(5)]):
        cnt += 1
    if all([check[j][4 - j] for j in range(5)]):
        cnt += 1

    # over the three lines
    if cnt >= 3:
        return True
    else:
        return False


board = [list(map(int, input().split())) for _ in range(5)]
# pos : position of number(index)
pos = [0 for _ in range(26)]
for j in range(5):
    for i in range(5):
        pos[board[j][i]] = [j, i]

call = []
for _ in range(5):
    call.extend(list(map(int, input().split())))

# check whether the numbers are called or not
check = [[False] * 5 for _ in range(5)]

for i in range(len(call)):
    now = pos[call[i]]
    check[now[0]][now[1]] = True
    if check_bingo():
        break
print(i+1)

