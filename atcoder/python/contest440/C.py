T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))

    M = 2 * W

    # i は 1..N の 1-index
    bucket = [0] * M
    for i, c in enumerate(C, start=1):
        bucket[i % M] += c

    # 円環上の長さ W の区間和の最小をスライドで求める
    b = bucket + bucket
    window = sum(b[0:W])
    ans = window
    for s in range(1, M):
        window += b[s + W - 1] - b[s - 1]
        if window < ans:
            ans = window

    print(ans)
