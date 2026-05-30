N, Q = map(int, input().split())
block: dict[int, int] = {}
place = [0] * N
block[0] = N
minus = 0


for i in range(Q):
    query, v = map(int, input().split())

    if query == 1:
        p = place[v-1]
        block[p] -= 1
        if not p + 1 in block:
            block[p+1] = block[p] + 1
            
        place[v-1] += 1
        
        if block[minus] == 0:
            minus += 1
    else:
        print(N - block[(v + minus)-1] if v+minus in block else 0)

        
    