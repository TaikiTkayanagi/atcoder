H, W = map(int, input().split())

ans = [0 * H] * W

for i in range(H):
    for j in range(W):
        v = 0
        if i - 1 > -1:
            v += 1

        if i + 1 < H:
            v += 1

        if j - 1 > -1:
            v += 1
        
        if j + 1 < W:
            v += 1
        print(v, end=" ")
    
    print()