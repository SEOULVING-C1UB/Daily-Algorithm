"""
First trial
You can notice that you can approach always from long width and height
to short width and height. Find area of big rectangle, then subtract
area of small rectangle.
"""

K = int(input())
infos = []
for _ in range(6):
    infos.append(list(map(int, input().split())))
w = sum([info[1] for info in infos if info[0] == 3])
h = sum([info[1] for info in infos if info[0] == 2])

# l1 : longest, l2 : second
if w > h:
    l1, l2 = w, h
else:
    l1, l2 = h, w

l1_idx = [info[1] for info in infos].index(l1)
if infos[l1_idx - 1][1] == l2:
    s1 = l1 - infos[l1_idx - 2][1]
    s2 = l2 - infos[(l1_idx + 1) % 6][1]
else:
    s1 = l1 - infos[(l1_idx + 2) % 6][1]
    s2 = l2 - infos[l1_idx - 1][1]

print(K * ((l1 * l2) - (s1 * s2)))

"""
Second Trial
I think I can make this code better and shorter.
Use same algorithm, but make code better.
The ways that TaeYang walked always follow next pattern.
[long width, long height, short width, empty height, empty width, short height]
So we can notice ((index of long) + 3) % 6 = index of empty 
"""

K = int(input())
# w : ways that TaeYang walked
w = [int(input().split()[1]) for _ in range(6)]
# a,b : indexes of rectangle's long sides, c,d : indexes of empty rectangle's side
a = w.index(max(w))
b = w.index(max(w[a - 1], w[a + 1]))
c = (a + 3) % 6
d = (b + 3) % 6
print(K * ((w[a] * w[b]) - (w[c] * w[d])))
