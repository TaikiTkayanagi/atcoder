from collections import deque

N, M, S, T = map(int, input().split())
dist = {}

for _ in range(M):
    A, B = map(int, input().split())
    if A in dist:
        dist[A].append(B) 
    else:
        dist[A] = [B]


for d in dist:
    dist[d] = sorted(dist[d])

q = deque()
q.appendleft([0, S])
memo = {S: 0}
ans = -1
while len(q) != 0:
    fuel, place = q.popleft()
    
    if place == T:
        if ans == -1:
            ans = fuel 
        else:
            ans = min(ans, fuel)
        continue 

    if place not in dist:
        continue
        
    for i, d in enumerate(dist[place]):
        

        if i == 0:
            if d in memo and memo[d] <= fuel:
                continue
            q.appendleft([fuel, d])
            memo[d] = fuel
        else:
            if d in memo and memo[d] <= fuel + 1:
                continue
            q.append([fuel+1, d])
            memo[d] = fuel + 1


print(ans)