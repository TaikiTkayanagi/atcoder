N = int(input())
W, H, B = [], [], []
for _ in range(N):
    w, h, b = map(int, input().split())
    W.append(w)
    H.append(h)
    B.append(b)

cap = sum(W) // 2
base = sum(B)

# dp[w] = その重さで達成できる v の最大値（-inf 初期化）
INF = 10**30
dp = [-INF] * (cap + 1)
dp[0] = 0

for w, h, b in zip(W, H, B):
    v = h - b
    if v <= 0:
        # 入れても得しないのでスキップでもOK（入れても結果は同じ）
        continue
    for cw in range(cap, w - 1, -1):
        dp[cw] = max(dp[cw], dp[cw - w] + v)

ans = base + max(0, max(dp))  # 入れない選択も可
print(ans)
