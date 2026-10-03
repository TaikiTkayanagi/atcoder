N, V = map(int , input().split())
W = list(map(int, input().split()))

max_v = 0
for i in range(N):
    for j in range(i+1, N):
        if (i+1) + (j+1) > V:
            break
        for k in range(j+1, N):
            if (i+1) + (j+1) + (k+1) > V:
                break
            total = W[i] + W[j] + W[k]
            if total > max_v:
                max_v = total 

print(max_v)