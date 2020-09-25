w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dy, dx = 1, 1
n = 0
while n < t:
    if p == 0:
        dx = 1
    elif p == w:
        dx = -1
    if q == 0:
        dy = 1
    elif q == h:
        dy = -1

    n += 1
    p += dx
    q += dy
    if visited[q][p]:
        temp = t % (w * h)
        find = False
        for j in range(h + 1):
            for i in range(w + 1):
                if visited[j][i] == temp:
                    p, q = i, j
                    find = True
                    break
            if find:
                break

        break
    else:
        visited[q][p] = n

print(p, q)
