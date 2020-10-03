w, h = map(int, input().split())
ans = 0
N = int(input())
# dr : dong's direction, ds : dong's distance from vertex
t = []
for _ in range(N):
    t.append(list(map(int, input().split())))
dr, ds = map(int, input().split())
# di : north, west, south, east
di = [1, 3, 2, 4]
dr_idx = di.index(dr)
lds = w - ds if dr in [1, 2] else h - ds
for i in range(N):
    # tr : target's direction, ts : target's distance from vertex
    tr, ts = t[i]
    tr_idx = di.index(tr)
    lts = w - ts if tr in [1, 2] else h - ts

    if abs(tr - dr) == 0:
        ans += abs(ts - ds)
    elif abs(tr_idx - dr_idx) == 2:
        if 1 in [tr, dr]:
            ans += min(ts + ds, lts + lds) + h
        else:
            ans += min(ts + ds, lts + lds) + w
    else:
        if [tr, dr] == [1, 3] or [tr, dr] == [3, 1]:
            ans += ts + ds
        elif [tr, dr] == [2, 4] or [tr, dr] == [4, 2]:
            ans += lts + lds
        elif [tr, dr] == [1, 4] or [tr, dr] == [3, 2]:
            ans += lts + ds
        else:
            ans += lds + ts
print(ans)
