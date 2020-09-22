height = [int(input()) for _ in range(9)]

# find : double_break
find = False
# find all subset
for i in range(1 << 9):
    temp = []
    for j in range(10):
        if i & (1 << j):
            temp.append(height[j])
        if len(temp) == 7 and sum(temp) == 100:
            find = True
            break
    if find:
        break

for each in sorted(temp):
    print(each)
