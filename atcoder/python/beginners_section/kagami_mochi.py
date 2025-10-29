n = int(input())
d: list[int] = []
for i in range(n):
    d.append(int(input()))

d.sort()

prev = 101
ans = 0
for i in reversed(d):
    if prev > i:
        ans += 1
        prev = i

print(ans)
