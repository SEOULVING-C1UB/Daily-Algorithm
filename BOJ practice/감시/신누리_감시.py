def setdirection(x, y, t):
    if t == 5:
        for k in range(4):
            a, b = x + dir1[k], y + dir2[k]
            while 0 <= a < N and 0 <= b < M:
                if arr[a][b] == 0:
                    arr[a][b] = 7
                elif arr[a][b] == 6:
                    break
                a += dir1[k]
                b += dir2[k]
    elif t == 4:
        mini = 0x7FFFFFFF
        for k in range(4):
            cnt = 0
            a, b = x + dir1[k], y + dir2[k]
            while 0 <= a < N and 0 <= b < M:
                if arr[a][b] == 0:
                    cnt += 1
                elif arr[a][b] == 6:
                    break
                a += dir1[k]
                b += dir2[k]
            if cnt < mini :
                mini = cnt
                minidx = k
        if minidx >=0:
            for k in range(4):
                if k != minidx:
                    a, b = x + dir1[k], y + dir2[k]
                    while 0 <= a < N and 0 <= b < M:
                        if arr[a][b] == 0:
                            arr[a][b] = 7
                        elif arr[a][b] == 6:
                            break
                        a += dir1[k]
                        b += dir2[k]
    elif t == 3:
        maxi, maxidx = 0, -1
        for k in range(4):
            cnt = 0
            for p in [0,1]:
                a, b = x + dir1[(k+p)%4], y + dir2[(k+p)%4]
                while 0 <= a < N and 0 <= b < M:
                    if arr[a][b] == 0:
                        cnt += 1
                    elif arr[a][b] == 6:
                        break
                    a += dir1[(k+p)%4]
                    b += dir2[(k+p)%4]
            if cnt > maxi:
                maxi = cnt
                maxidx = k
        if maxidx >= 0:
            for p in [0,1]:
                a, b = x + dir1[(maxidx+p)%4], y + dir2[(maxidx+p)%4]
                while 0 <= a < N and 0 <= b < M:
                    if arr[a][b] == 0:
                        arr[a][b] = 7
                    elif arr[a][b] == 6:
                        break
                    a += dir1[(maxidx+p)%4]
                    b += dir2[(maxidx+p)%4]
    elif t == 2:
        maxi, maxidx = 0, -1
        for k in range(2):
            cnt = 0
            for p in [0,2]:
                a, b = x + dir1[k+p], y + dir2[k+p]
                while 0 <= a < N and 0 <= b < M:
                    if arr[a][b] == 0:
                        cnt += 1
                    elif arr[a][b] == 6:
                        break
                    a += dir1[k+p]
                    b += dir2[k+p]
            if cnt > maxi:
                maxi = cnt
                maxidx = k
        if maxidx >= 0:
            for p in [0,2]:
                a, b = x + dir1[maxidx+p], y + dir2[maxidx+p]
                while 0 <= a < N and 0 <= b < M:
                    if arr[a][b] == 0:
                        arr[a][b] = 7
                    elif arr[a][b] == 6:
                        break
                    a += dir1[maxidx+p]
                    b += dir2[maxidx+p]
    elif t == 1:
        maxi, maxidx = 0, -1
        for k in range(4):
            cnt = 0
            a, b = x + dir1[k], y + dir2[k]
            while 0 <= a < N and 0 <= b < M:
                if arr[a][b] == 0:
                    cnt += 1
                elif arr[a][b] == 6:
                    break
                a += dir1[k]
                b += dir2[k]
            if cnt > maxi:
                maxi = cnt
                maxidx = k
        if maxidx >= 0:
            a, b = x + dir1[maxidx], y + dir2[maxidx]
            while 0 <= a < N and 0 <= b < M:
                if arr[a][b] == 0:
                    arr[a][b] = 7
                elif arr[a][b] == 6:
                    break
                a += dir1[maxidx]
                b += dir2[maxidx]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir1 = [1, 0, -1, 0]
dir2 = [0, 1, 0, -1]

cameras = []
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            cameras.append([arr[i][j], i, j])
cameras.sort(reverse=True)
for cam in cameras:
    setdirection(cam[1], cam[2], cam[0])

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result +=1
print(result)

'''
반례
4 6
2 6 0 3 0 2
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 6 1
correct = 8

4 4
0 4 0 2
0 0 0 2
0 0 0 0
3 5 0 0
correct = 1
'''
