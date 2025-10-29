N, Y = map(int, input().split())

if Y % 1000 != 0:
    print(-1, -1, -1)
    exit(0)

for i in range(N + 1):
    l = N - i
    for j in reversed(range(N + 1 - i)):
        if Y - ((10000 * i) + (5000 * (l - j)) + (1000 * j)) == 0:
            print(i, l-j, j)
            exit(0)
print(-1, -1, -1)
