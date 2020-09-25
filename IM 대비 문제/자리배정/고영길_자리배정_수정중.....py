def is_wall(j, i):
    global r_wall, l_wall, d_wall, u_wall
    if j == d_wall:
        d_wall -= 1
        return True
    elif j == u_wall:
        u_wall += 1
        return True

    if i == l_wall:
        l_wall += 1
        return True
    elif i == r_wall:
        r_wall -= 1
        return True
    return False

C, R = map(int, input().split())
K = int(input())

r_wall = C + 1
l_wall = 0
d_wall = R + 1
u_wall = 0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

d_idx = 0
cnt = 1
y, x = 1, 1

if K > C * R:
    print(0)
else:
    while True:
        print(y,x,d_idx)
        if cnt == K:
            print(x, y)
            break

        ny = y + dy[d_idx]
        nx = x + dx[d_idx]
        if is_wall(ny,nx):
            d_idx = (d_idx + 1) % 4

        y += dy[d_idx]
        x += dx[d_idx]
        cnt += 1