N, M = map(int, input().split())
candidate = {}
order = [] 
for _ in range(N):
    c = input()
    candidate[c] = 0 
    order.append(c)

for _ in range(M):
    m = input()
    if m in candidate:
        candidate[m] += 1
        continue
    
    estimate = []
    for c in order:
        if len(m) != len(c):
            continue
        mistake = 0
        for i in range(len(m)):
            if m[i] != c[i]:
                mistake += 1
            
            if mistake > 1:
                break 
        
        if mistake == 1:
            estimate.append(c)
    
    if len(estimate) == 1:
        candidate[estimate[0]] += 1
        

for o in order:
    print(candidate[o]) 