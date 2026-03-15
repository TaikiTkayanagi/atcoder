H, W, Q = map(int, input().split())
for _ in range(Q):
    q, e = map(int, input().split())

    if q == 1:
        H = H - e
        print(e * W)
    else:
        W = W - e
        print(e * H)
    
    