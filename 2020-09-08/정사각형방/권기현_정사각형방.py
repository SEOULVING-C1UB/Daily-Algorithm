import sys

sys.stdin = open('1861.txt')

total_tc = int(input())


def traveler(start_value,i, j,  distance):
    global max_distance
    global starting_point
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    if distance > max_distance or (distance == max_distance and start_value < starting_point ):
        max_distance = distance
        starting_point = start_value
    for dir in range(4):
        if i+dx[dir]>=0 and  i+dx[dir]<N and j+dy[dir]>=0 and  j+dy[dir]<N and room_escape[i+dx[dir]][j+dy[dir]]==room_escape[i][j]+1:
            distance += 1
            # print(f"travelling from {i}, {j} to {i+dx[dir]}, {j+dy[dir]} distance is {distance}")
            traveler(start_value, i+dx[dir],j+dy[dir], distance)



for tc in range(1, total_tc+1):
    N = int(input())
    room_escape = [list(map(int, input().split())) for _ in range (N)]
    distance_dict={}
    max_distance = 0
    starting_point=1000000
    for i in range(N):
        for j in range(N):
            distance_dict[room_escape[i][j]]= traveler(room_escape[i][j], i,j,1)




    print("#%d"%(tc), starting_point, max_distance )