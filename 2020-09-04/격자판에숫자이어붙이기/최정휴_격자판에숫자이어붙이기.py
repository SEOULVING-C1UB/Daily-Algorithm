# 주석은 내일 달께요~!!

def makeworm(x,y,n,worm):
    if n == 6:
        worms.append(worm)
    else:
        for i in range(4):
            if 0<=x+dx[i]<4 and 0<=y+dy[i]<4:
                makeworm(x+dx[i], y+dy[i], n+1, worm+field[y+dy[i]][x+dx[i]])


t = int(input())
for i in range(1,t+1):
    field = [list(input().split()) for _ in range(4)]
    worms = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for y in range(4):
        for x in range(4):
            makeworm(x, y, 0, field[y][x])
    print('#{} {}'.format(i,len(set(worms))))