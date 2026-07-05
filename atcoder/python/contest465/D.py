T = int(input())

ans = []
for _ in range(T):
    X, Y, K = map(int, input().split())

    x = X
    y = Y
    c = 0

    while x != y:
        if x > y:
            x //= K
        else:
            y //= K
        c += 1
    ans.append(c)

for a in ans:
    print(a)