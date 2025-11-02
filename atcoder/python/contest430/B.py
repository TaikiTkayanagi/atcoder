N, M = map(int, input().split())
grid = []

for i in range(N):
    grid.append(list(input()))

memo = []
for i in range(N):
    if i + M - 1 > N - 1:
        break
    for j in range(N):
        if j + M - 1 > N - 1:
            break
        tmp = ""
        for row_max in range(M):
            for col_max in range(M):
                tmp += grid[i+row_max][j+col_max]
        if not tmp in memo:
            memo.append(tmp)

print(len(memo))
