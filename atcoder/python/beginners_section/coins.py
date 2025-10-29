a = int(input())
b = int(input())
c = int(input())
x = int(input())

memo: dict[int, int] = {}
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            key = 500 * i + 100 * j + k * 50
            if key in memo:
                memo[key] = memo[key] + 1
            else:
                memo[key] = 1

print(0 if x not in memo else memo[x])
