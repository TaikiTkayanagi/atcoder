n = int(input())
a = list(map(int, input().split()))

is_loop = True
ans = -1
while is_loop:
    ans += 1
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] //= 2
        else:
            is_loop = False
            break

print(ans)
