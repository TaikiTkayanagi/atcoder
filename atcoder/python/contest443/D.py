import heapq


def solve():
    N = int(input())
    R = list(map(int, input().split()))

    # 優先度付きキュー: (現在の高さ, インデックス) を高さの昇順で管理
    pq = []
    for i in range(N):
        heapq.heappush(pq, (R[i], i))

    # 現在の各駒の位置を管理
    a = R.copy()

    # 上から順に処理
    while pq:
        ai, i = heapq.heappop(pq)

        # 古い情報の場合はスキップ（既に更新済み）
        if a[i] != ai:
            continue

        # 左隣の駒を調整
        if i > 0 and a[i - 1] > a[i] + 1:
            a[i - 1] = a[i] + 1
            heapq.heappush(pq, (a[i - 1], i - 1))

        # 右隣の駒を調整
        if i < N - 1 and a[i + 1] > a[i] + 1:
            a[i + 1] = a[i] + 1
            heapq.heappush(pq, (a[i + 1], i + 1))

    # 移動回数の合計を計算
    ans = sum(R[i] - a[i] for i in range(N))
    return ans


T = int(input())
for _ in range(T):
    print(solve())
