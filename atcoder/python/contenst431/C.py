N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()
H_index = 0
value = 0
count = 0
h = H[H_index]
for b in B:
    if len(H) > H_index and b >= h:
        H_index += 1
        count += 1
        if len(H) > H_index:
            h = H[H_index]


print("Yes" if count >= K else "No")
