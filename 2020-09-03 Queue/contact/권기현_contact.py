import sys
sys.stdin = open('1238.txt')

def bfs(start_input):
    queue = []
    queue.append(start_input)
    while queue:
        start = queue.pop(0)
        for contact in range(101):
            if table[start][contact] == 1 and dtf[contact]==0:
                dtf[contact]=dtf[start]+1
                queue.append(contact)


    last_list = [i for i, x in enumerate(dtf) if x == max(dtf)]
    return max(last_list)



for tc in range(1, 11):

    #input
    N, initial = map(int, input().split())
    relations = list(map(int, input().split()))

    #table maker
    table = [[0 for _ in range (101)] for _ in range (101)]
    dtf = [0 for _ in range (101)]
    for i in range (N//2):
        table[relations[2*i]][relations[2*i+1]] = 1

    print("#%d %d"%(tc, bfs(initial)))


