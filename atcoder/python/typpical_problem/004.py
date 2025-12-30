H, W = map(int, input().split())

table = []
for _ in range(H):
    table.append(list(map(int, input().split())))

iterator_h = 0
h_memo = {}
iterator_w = 0
w_memo = {}
ans = [[0] * W for _ in range(H)]
while iterator_w < W:
    total = 0
    if iterator_h in h_memo.keys():
        total += h_memo[iterator_h]
    else:
        for i in range(W):
            total += table[iterator_h][i]
        h_memo[iterator_h] = total
    if iterator_w in w_memo.keys():
        total += w_memo[iterator_w]
    else:
        for i in range(H):
            total += table[i][iterator_w]
        w_memo[iterator_w] = total - h_memo[iterator_h]
    ans[iterator_h][iterator_w] = total - table[iterator_h][iterator_w]
    iterator_h = iterator_h + 1 if iterator_h < H else iterator_h
    if iterator_h >= H:
        iterator_h = 0
        iterator_w += 1


for a in ans:
    print(*a, sep=" ")
