def setdirection(t):
    maxi = 0
    if t == 1:
        for k in range(4):
            cnt = 0
            x, y = i + dir1[k], j+dir2[k]
            while 0 <= x < N and 0<= y < M:
                if arr[x][y] > 0:
                    break
                elif arr[x][y] == 0 :
                    cnt += 1
                x += dir1[k]
                y += dir2[k]
            if cnt > maxi:
                maxi = cnt
                maxidx = k
        x, y = i + dir1[maxidx], j+dir2[maxidx]
        while 0 <= x < N and 0<= y < M:
            if arr[x][y] > 0:
                break
            arr[x][y] = -1
            x += dir1[maxidx]
            y += dir2[maxidx]
    elif t == 2:
        pass
    elif t == 3:
        pass
    elif t == 4:
        mini = 0x7FFFFFFF
        for k in range(4):
            cnt = 0
            x, y = i + dir1[k], j+dir2[k]
            while 0 <= x < N and 0<= y < M:
                if arr[x][y] > 0:
                    break
                elif arr[x][y] == 0 :
                    cnt += 1
                x += dir1[k]
                y += dir2[k]
            if cnt < mini:
                mini = cnt
                minidx = k
        for k in range(4):
            if k != minidx :
                x, y = i + dir1[k], j+dir2[k]
                while 0 <= x < N and 0<= y < M:
                    if arr[x][y] > 0:
                        break
                    arr[x][y] = -1
                    x += dir1[k]
                    y += dir2[k]
    elif t == 5:
        for k in range(4):
            x, y = i + dir1[k], j+dir2[k]
            while 0 <= x < N and 0<= y < M:
                if arr[x][y] > 0:
                    break
                arr[x][y] = -1
                x += dir1[k]
                y += dir2[k]      

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir1 = [1, 0, -1, 0]
dir2 = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            setdirection(arr[i][j])               

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result +=1
# print(arr)
print(result)
