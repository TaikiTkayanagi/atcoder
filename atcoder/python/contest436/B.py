N = int(input())

inner = [0] * N
a = [[0 for j in range(N)] for i in range(N)]

r = 0
c = (N - 1) // 2
k = 1

a[r][c] = k

for i in range(N * N - 1):
    k += 1
    tmp_r = (r - 1) % N
    tmp_c = (c + 1) % N

    if a[tmp_r][tmp_c] == 0:
        r = tmp_r
        c = tmp_c
    else:
        r = (r + 1) % N

    a[r][c] = k

for i in range(N):
    for j in range(N):
        if j + 1 == N:
            print(a[i][j], end="")
        else:
            print(a[i][j], end=" ")
    print()
