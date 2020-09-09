import sys
sys.stdin = open('7465.txt')



def friends(person):
    relation_tf[person]=True
    queue = []
    queue.extend(relation[person])
    # print(person, end=' : ')
    while queue:
        friend_of_friend = queue.pop(0)

        if relation_tf[friend_of_friend]==False:
            # print(friend_of_friend, end=' ')
            relation_tf[friend_of_friend] = True
            queue.extend(relation[friend_of_friend])
    # print()


total_tc = int(input())
for tc in range(1, total_tc+1):
    N, M = map(int, input().split())
    relation = {}
    relation_tf = [False for _ in range(N + 1)]
    for i in range(1, N+1):
        relation[i]=[]
    relation_tf = [False for _ in range (N+1)]


    for _ in range(M):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)

    group = 0
    for j in range(1, N+1):
        if relation_tf[j]==False:
            friends(j)
            group +=1
    print("#%d %d"%(tc, group))