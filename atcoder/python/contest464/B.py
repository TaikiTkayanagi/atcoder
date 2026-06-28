H, W = map(int, input().split())
C = []
ans = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    t = list(input())
    C.append(t)

for i in range(H):
    is_ok = True
    for j in range(W):
        if C[i][j] == "#":
            is_ok = False 
            break
    
    if not is_ok:
        break
    else:
        for j in range(W):
            ans[i][j] = -1

for i in range(H - 1, 0, -1):
    is_ok = True
    for j in range(W):
        if C[i][j] == "#":
            is_ok = False 
            break
    
    if not is_ok:
        break
    else:
        for j in range(W):
            ans[i][j] = -1

if len(C) != 0:
    for i in range(W):
        is_ok = True
        for j in range(H):
            if C[j][i] == "#":
                is_ok = False
        
        if not is_ok:
            break
        else:
            for j in range(H):
                ans[j][i] = -1
    

if len(C) != 0:
    for i in range(W-1, 0, -1):
        is_ok = True
        for j in range(H):
            if C[j][i] == "#":
                is_ok = False
        
        if not is_ok:
            break
        else:
            for j in range(H):
                ans[j][i] = -1
            

for i in range(len(C)):
    is_print = False
    for j in range(len(C[i])):
        if ans[i][j] == -1:
            continue
        is_print = True
        print(C[i][j], end='')
    if is_print:
        print()
     