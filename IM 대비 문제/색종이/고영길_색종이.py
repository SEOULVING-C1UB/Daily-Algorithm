# black : space attached colored paper
black = set()
for i in range(int(input())):
    x, y = map(int, input().split())
    # attach paper
    black.update(set([(a, b) for a in range(x, x + 10) for b in range(y, y + 10)]))
print(len(black))
