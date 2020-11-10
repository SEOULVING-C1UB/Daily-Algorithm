import sys
sys.stdin = open("러시아국기_input.txt", "r")

def power(k, r) :
    global min_counter
    for i in range(0, k-r+1) :
        tempi = seq_list[i:i+r]
        seti.append(tempi)
        now_counter = counter(tempi)
        if min_counter > now_counter :
            min_counter = now_counter
    r -= 1
    if r == 0 : return
    else : return power(k,r)


def counter(b) :
    global m, n
    temp_counti = 0
    for y in b :
        for x in range(m) :
            if arr[y-1][x] != 'B' :
                temp_counti += 1

    if b[0] != 2 :
        for y in range(1, b[0]-1) :
            for x in range(m) :
                if arr[y][x] != 'W' :
                    temp_counti += 1
    if b[-1] != (n-1) :
        for y in range(b[0], n-1) :
            for x in range(m) :
                if arr[y][x] != 'R' :
                    temp_counti += 1
    return temp_counti



def basic(m) :
    counti = 0
    for x in range(m) :
        if arr[0][x] is not 'W' :
            temp_arr[0][x] = 'W'
            counti += 1
        if arr[-1][x] is not 'R' :
            temp_arr[-1][x] = 'R'
            counti += 1
    return counti

tc = int(input())

for t in range(tc) :
    min_counter = 999999
    n, m = map(int, input().split())

    arr = []
    temp_arr = []

    seq_list = [i for i in range(2, n+2)]
    seti = []
    for i in range(n) :
        temp = list(input())
        arr.append(temp)
        temp_arr.append(temp)

    basic_cnt = basic(m)

    power(n-2, n-2)

    result = min_counter + basic_cnt
    print("#{} {}".format(t+1, result))
