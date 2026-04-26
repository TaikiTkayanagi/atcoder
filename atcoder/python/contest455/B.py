H, W = map(int, input().split())
grid = []

for _ in range(H):
    grid.append(list(input()))
    

ans = 0
for h1 in range(H):
    for w1 in range(W):
        for h2 in range(h1, H):
            for w2 in range(w1, W):
                for i in range(h1, h2+1):
                    is_ok = True
                    for j in range(w1, w2+1):
                        if grid[h1 + h2 - i][w1 + w2 - j] != grid[i][j]:
                            is_ok = False
                    
                    if not is_ok:
                        break

                    if i + 1 == h2 + 1:
                        ans += 1
        
print(ans)