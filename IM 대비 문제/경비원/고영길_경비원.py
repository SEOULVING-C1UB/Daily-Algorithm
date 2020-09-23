'''
Set reference point: vertex between lines 1 and 3,
calculates the clockwise distance from the each point to reference vertex.
Next, compare distance to the vertex with the opposite direction.
'''
w, h = map(int, input().split())
p = 2 * (w + h)  # perimeter of rectangle
# dist : (list) store the choices of distance from dong to target
dist = []

for _ in range(int(input()) + 1):
    a, b = map(int, input().split())
    # calculates the clockwise distance
    dist.append([0, p - b, h + b, b, p - w - b][a])

dong = dist.pop()
ans = 0
for point in dist:
    # cwd : clockwise distance
    cwd = abs(dong - point)
    ans += min(cwd, p - cwd)
print(ans)