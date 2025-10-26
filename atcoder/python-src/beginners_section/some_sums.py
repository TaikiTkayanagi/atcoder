t = input().split()
n, a, b = map(int, input().split())

r = 0
for i in range(1, n+1):
    s = sum(list(map(int, str(i))))
    if s >= a and s <= b:
        r += i

print(r)
