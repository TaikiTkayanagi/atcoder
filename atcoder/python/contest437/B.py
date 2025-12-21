H, W, N = map(int, input().split())

map = []
for i in range(H):
    row = input().split()
    map.append(row)

ans = [0] * H
for i in range(N):
    b = input()
    for i, m in enumerate(map):
        if b in m:
            ans[i] += 1
            break

max = 0
for a in ans:
    if a > max:
        max = a
print(max)
